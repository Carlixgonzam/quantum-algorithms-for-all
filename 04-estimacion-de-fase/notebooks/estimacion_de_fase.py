"""Implementaciones de Qiskit para 04-estimacion-de-fase.
Estimación de fase: eigenvectores, circuito completo, costo."""

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, Operator
from qiskit.circuit.library import UnitaryGate

sim = AerSimulator()

# ──────────────────────────────────────────────────────
# 1. Phase kickback con 1 qubit de control
# ──────────────────────────────────────────────────────

def phase_kickback_1qb(U: np.ndarray) -> Statevector:
    """Aplica U controlada a |+⟩|ψ⟩ y devuelve el estado del control."""
    n = int(np.log2(U.shape[0]))
    qc = QuantumCircuit(n + 1)
    qc.h(0)
    ctrl_U = UnitaryGate(U).control()
    qc.append(ctrl_U, list(range(n + 1)))
    return Statevector(qc)

def phase_kickback_identidad():
    """U = I → el control queda en |+⟩."""
    I = np.eye(2)
    sv = phase_kickback_1qb(I)
    print(f"  U=I:    control = {sv.to_dict()}")
    print(f"  P(0)={sv.probabilities()[0]:.3f}, P(1)={sv.probabilities()[1]:.3f}")

def phase_kickback_hadamard():
    """U = H, con |ψ⟩ = eigenvector de H con λ=±1."""
    H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    qc = QuantumCircuit(2, 1)
    qc.h(0)
    qc.h(1)
    ctrl_H = UnitaryGate(H).control()
    qc.append(ctrl_H, [0, 1])
    qc.measure(0, 0)
    qc = transpile(qc, sim)
    result = sim.run(qc, shots=4096).result()
    counts = result.get_counts()
    print(f"  U=H:    mediciones control = {counts}")
    print(f"  P(0)={counts.get('0',0)/4096:.3f}")

# ──────────────────────────────────────────────────────
# 2. Phase estimation con 1 qubit de control
# ──────────────────────────────────────────────────────

def phase_estimation_1qubit(U: np.ndarray, eigenvector: np.ndarray) -> tuple:
    """Estima la fase de U usando 1 qubit de control."""
    qc = QuantumCircuit(2, 1)
    qc.h(0)
    qc.initialize(eigenvector, 1)
    ctrl_U = UnitaryGate(U).control()
    qc.append(ctrl_U, [0, 1])
    qc.h(0)
    qc.measure(0, 0)

    qc = transpile(qc, sim)
    result = sim.run(qc, shots=8192).result()
    counts = result.get_counts()
    p0 = counts.get("0", 0) / 8192

    # De la fórmula: P(0) = (1 + cos(2πφ)) / 2
    cos_theta = 2 * p0 - 1
    theta = np.arccos(cos_theta)
    # La fase φ = θ / (2π)
    phi = theta / (2 * np.pi)
    return phi, p0

def fase_de_u_t():
    """Estima la fase de la compuerta T.
    T|1⟩ = e^{iπ/4}|1⟩ → fase φ = 1/8 = 0.125
    T|0⟩ = |0⟩           → fase φ = 0
    """
    T = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]])
    phi, p0 = phase_estimation_1qubit(T, [0, 1])  # |1⟩ es eigenvector con fase no trivial
    print(f"  P(0) = {p0:.4f}")
    print(f"  Fase estimada φ = {phi:.4f} (esperada 1/8 = 0.125)")

# ──────────────────────────────────────────────────────
# 3. Phase estimation multi-qubit (3 qubits de control)
# ──────────────────────────────────────────────────────

def phase_estimation_multiq(U: np.ndarray, m: int, eigenvector: np.ndarray) -> str:
    """Estimación de fase con m qubits de control."""
    n = int(np.log2(U.shape[0]))
    qr_c = QuantumRegister(m, "c")
    qr_t = QuantumRegister(n, "t")
    cr = ClassicalRegister(m)
    qc = QuantumCircuit(qr_c, qr_t, cr)

    qc.h(qr_c)
    qc.initialize(eigenvector, qr_t)

    for i in range(m):
        power = 2**i
        U_pow = np.linalg.matrix_power(U, power)
        ctrl_U_pow = UnitaryGate(U_pow).control()
        qc.append(ctrl_U_pow, [qr_c[i]] + list(qr_t))

    qc.append(QFTGate(m).inverse(), qr_c)

    qc.measure(qr_c, cr)

    qc = transpile(qc, sim)
    result = sim.run(qc, shots=4096).result()
    counts = result.get_counts()

    max_outcome = max(counts, key=counts.get)
    phi_estimado = int(max_outcome, 2) / (2**m)
    return phi_estimado, counts

from qiskit.circuit.library import QFTGate

def inverse_of_qft(n: int) -> QuantumCircuit:
    """Circuito de QFT† usando QFTGate."""
    qc = QuantumCircuit(n)
    qc.append(QFTGate(n).inverse(), range(n))
    return qc

def fase_de_s_gate():
    """Estima la fase de S (φ=1/4). Usa |1⟩ como eigenvector."""
    S = np.array([[1, 0], [0, 1j]])
    m = 3
    phi, counts = phase_estimation_multiq(S, m, [0, 1])  # |1⟩ tiene fase no trivial
    print(f"  Fase estimada φ = {phi:.4f} (esperada 0.25)")
    print(f"  Mediciones: {dict(list(counts.items())[:5])}")

# ──────────────────────────────────────────────────────
# 4. Desglose de costo
# ──────────────────────────────────────────────────────

def costo_phase_estimation(m: int, costo_U: int = 1):
    """Calcula el costo de cada parte de phase estimation."""
    print(f"  m={m} qubits de control")
    print(f"    Hadamards:       {m}")
    print(f"    Controlled-U^k:  {sum(2**i for i in range(m)) * costo_U}")
    print(f"    QFT†:            O({m**2})")
    print(f"    Mediciones:      {m}")


if __name__ == "__main__":
    print("=" * 55)
    print("04 - ESTIMACIÓN DE FASE")
    print("=" * 55)

    print("\n--- Phase kickback con U=I ---")
    phase_kickback_identidad()

    print("\n--- Phase kickback con U=H ---")
    phase_kickback_hadamard()

    print("\n--- Phase estimation 1 qubit (U=T) ---")
    fase_de_u_t()

    print("\n--- Phase estimation multi-qubit (U=S) ---")
    fase_de_s_gate()

    print("\n--- Desglose de costo ---")
    costo_phase_estimation(4)
