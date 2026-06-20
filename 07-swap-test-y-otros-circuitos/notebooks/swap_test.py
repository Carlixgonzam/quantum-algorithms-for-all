"""Implementaciones de Qiskit para 07-swap-test-y-otros-circuitos.
Swap test, circuitos de estado GHZ, W, y teleportación."""

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, partial_trace, entropy
from qiskit.visualization import plot_histogram

sim = AerSimulator()

# ──────────────────────────────────────────────────────
# 1. Swap Test
# ──────────────────────────────────────────────────────

def swap_test(qc: QuantumCircuit, qr_control: QuantumRegister,
              qr_a: QuantumRegister, qr_b: QuantumRegister):
    """Agrega un swap test al circuito dado."""
    n = len(qr_a)
    qc.h(qr_control)
    for i in range(n):
        qc.cswap(qr_control, qr_a[i], qr_b[i])
    qc.h(qr_control)

def swap_test_completo(estado_a: list | np.ndarray,
                       estado_b: list | np.ndarray) -> dict:
    """Ejecuta un swap test completo entre dos estados de 1 qubit."""
    qr_c = QuantumRegister(1, "c")
    qr_a = QuantumRegister(1, "a")
    qr_b = QuantumRegister(1, "b")
    cr = ClassicalRegister(1)
    qc = QuantumCircuit(qr_c, qr_a, qr_b, cr)

    qc.initialize(estado_a, qr_a)
    qc.initialize(estado_b, qr_b)

    swap_test(qc, qr_c, qr_a, qr_b)
    qc.measure(qr_c, cr)

    qc = transpile(qc, sim)
    result = sim.run(qc, shots=8192).result()
    return result.get_counts()

def swap_test_demo():
    """Swap test con pares de estados conocidos."""
    pares = [
        ("|0⟩ y |0⟩ (idénticos)", [1, 0], [1, 0]),
        ("|0⟩ y |1⟩ (ortogonales)", [1, 0], [0, 1]),
        ("|+⟩ y |+⟩ (idénticos)", [1, 1] / np.sqrt(2), [1, 1] / np.sqrt(2)),
        ("|+⟩ y |−⟩ (ortogonales)", [1, 1] / np.sqrt(2), [1, -1] / np.sqrt(2)),
        ("|0⟩ y |+⟩ (solapamiento 1/√2)", [1, 0], [1, 1] / np.sqrt(2)),
    ]

    for nombre, a, b in pares:
        counts = swap_test_completo(a, b)
        p1 = counts.get("1", 0) / 8192
        overlap = abs(np.vdot(a, b)) ** 2
        p1_teorica = 0.5 * (1 - overlap)
        print(f"  {nombre:45s}  P(1)={p1:.4f}  (teórica: {p1_teorica:.4f})")

# ──────────────────────────────────────────────────────
# 2. Estado GHZ
# ──────────────────────────────────────────────────────

def estado_ghz(n: int) -> QuantumCircuit:
    """Crea un estado GHZ de n qubits."""
    qc = QuantumCircuit(n)
    qc.h(0)
    for i in range(1, n):
        qc.cx(0, i)
    return qc

def ghz_demo():
    """Crea y mide un estado GHZ de 4 qubits."""
    n = 4
    qc = estado_ghz(n)
    qc.measure_all()

    print(f"  Circuito GHZ-{n}:")
    print(qc.draw("text"))

    qc = transpile(qc, sim)
    result = sim.run(qc, shots=2048).result()
    counts = result.get_counts()

    prob_0000 = counts.get("0" * n, 0) / 2048
    prob_1111 = counts.get("1" * n, 0) / 2048
    print(f"  P(0000) = {prob_0000:.4f}")
    print(f"  P(1111) = {prob_1111:.4f}")
    print(f"  Otras mediciones: {sum(v for k, v in counts.items() if k not in ['0000', '1111']) / 2048:.4f}")

# ──────────────────────────────────────────────────────
# 3. Estado W
# ──────────────────────────────────────────────────────

def estado_w(n: int) -> QuantumCircuit:
    """Crea un estado W de n qubits: (|100...⟩ + |010...⟩ + ... + |...001⟩)/√n."""
    qc = QuantumCircuit(n)
    qc.ry(2 * np.arccos(1 / np.sqrt(n)), 0)
    for i in range(1, n):
        qc.cx(i - 1, i)
        remaining = n - i - 1
        if remaining > 0:
            angle = 2 * np.arccos(1 / np.sqrt(remaining + 1))
            qc.cry(angle, i - 1, i)
        else:
            pass
    return qc

def w_demo():
    """Crea y verifica un estado W de 3 qubits."""
    n = 3
    qc = estado_w(n)
    sv = Statevector(qc)
    print(f"  Estado W-{n}:")
    for i, amp in enumerate(sv.data):
        if abs(amp) > 1e-10:
            print(f"    |{format(i, f'0{n}b')}⟩ : amplitud = {amp:.4f}")

# ──────────────────────────────────────────────────────
# 4. Teleportación cuántica
# ──────────────────────────────────────────────────────

def teleportacion() -> dict:
    """Circuito de teleportación cuántica."""
    qr = QuantumRegister(3, "q")
    cr_clasico = ClassicalRegister(2, "med")
    cr_target = ClassicalRegister(1, "out")
    qc = QuantumCircuit(qr, cr_clasico, cr_target)

    # Estado a teleportar: |1⟩
    qc.x(0)

    # Entrelazar Alice-Bob (qubits 1,2)
    qc.h(1)
    qc.cx(1, 2)

    # Alice: Bell measurement
    qc.cx(0, 1)
    qc.h(0)
    qc.measure(0, 0)
    qc.measure(1, 1)

    # Bob: correcciones condicionales
    with qc.if_test((cr_clasico, 1)):  # m0=1 → Z
        qc.z(2)
    with qc.if_test((cr_clasico, 2)):  # m1=1 → X
        qc.x(2)
    with qc.if_test((cr_clasico, 3)):  # ambos → ZX
        qc.z(2)
        qc.x(2)

    qc.measure(2, 2)

    qc = transpile(qc, sim)
    result = sim.run(qc, shots=2048).result()
    counts = result.get_counts()
    return counts

def teleportacion_demo():
    """Ejecuta teleportación y verifica que el output es |1⟩."""
    counts = teleportacion()
    prob_1 = sum(v for k, v in counts.items() if k[0] == "1") / 2048
    print(f"  P(qubit destino = |1⟩) = {prob_1:.4f}  (esperado ~1.0)")


if __name__ == "__main__":
    print("=" * 55)
    print("07 - SWAP TEST Y OTROS CIRCUITOS")
    print("=" * 55)

    print("\n--- Swap test ---")
    swap_test_demo()

    print("\n--- Estado GHZ ---")
    ghz_demo()

    print("\n--- Estado W ---")
    w_demo()

    print("\n--- Teleportación cuántica ---")
    teleportacion_demo()
