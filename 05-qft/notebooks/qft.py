"""Implementaciones de Qiskit para 05-qft.
Transformada de Fourier Cuántica: definición, propiedades, inversa."""

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, Operator
from qiskit.circuit.library import QFT as QFT_lib

sim = AerSimulator()

# ──────────────────────────────────────────────────────
# 1. QFT estándar (usando la implementación de Qiskit)
# ──────────────────────────────────────────────────────

def qft(n: int) -> QuantumCircuit:
    """Construye el circuito QFT para n qubits."""
    return QFT_lib(num_qubits=n)

def qft_inv(n: int) -> QuantumCircuit:
    """Construye el circuito QFT† (inversa de QFT)."""
    return QFT_lib(num_qubits=n, inverse=True)

# ──────────────────────────────────────────────────────
# 2. Verificación de propiedades
# ──────────────────────────────────────────────────────

def verificar_qft_cuadrado():
    """Verifica QFT²|x⟩ = |-x mod N⟩."""
    n = 3
    N = 2**n

    qft_3 = qft(n)
    operador_qft = Operator(qft_3)
    QFT_matrix = operador_qft.data

    QFT2 = QFT_matrix @ QFT_matrix

    for x in range(N):
        ket_x = np.zeros(N, dtype=complex)
        ket_x[x] = 1.0
        resultante = QFT2 @ ket_x
        estado_esperado = np.zeros(N, dtype=complex)
        estado_esperado[(-x) % N] = 1.0
        overlap = abs(np.vdot(estado_esperado, resultante))
        ok = "✓" if overlap > 0.999 else "✗"
        print(f"  |x={x}⟩ → QFT² → |{-x % N}⟩ : overlap = {overlap:.6f} {ok}")

def verificar_qft_cuarta():
    """Verifica QFT⁴ = I."""
    n = 3
    N = 2**n
    QFT_matrix = Operator(qft(n)).data
    QFT4 = np.linalg.matrix_power(QFT_matrix, 4)
    identidad = np.eye(N, dtype=complex)
    coincide = np.allclose(QFT4, identidad, atol=1e-10)
    print(f"  QFT⁴ ≈ I? {coincide}")

def verificar_qft_aplica():
    """Verifica QFT|x⟩ contra la definición."""
    n = 3
    N = 2**n
    QFT_matrix = Operator(qft(n)).data

    for x in range(N):
        ket_x = np.zeros(N, dtype=complex)
        ket_x[x] = 1.0
        resultante = QFT_matrix @ ket_x
        esperado = np.array([np.exp(2j * np.pi * x * y / N) / np.sqrt(N)
                             for y in range(N)])
        overlap = abs(np.vdot(esperado, resultante))
        ok = "✓" if overlap > 0.999 else "✗"
        print(f"  QFT|x={x}⟩ : overlap con fórmula = {overlap:.6f} {ok}")

# ──────────────────────────────────────────────────────
# 3. QFT como subrutina
# ──────────────────────────────────────────────────────

def qft_en_phase_estimation():
    """Muestra el circuito de QFT usado en phase estimation."""
    n = 3
    qft_circ = qft(n)
    qft_inv_circ = qft_inv(n)
    print("Circuito QFT (3 qubits, Qiskit library):")
    print(qft_circ.decompose().draw("text"))
    print("\nCircuito QFT† (3 qubits):")
    print(qft_inv_circ.decompose().draw("text"))


if __name__ == "__main__":
    print("=" * 55)
    print("05 - TRANSFORMADA DE FOURIER CUÁNTICA")
    print("=" * 55)

    print("\n--- Verificación QFT|x⟩ contra definición ---")
    verificar_qft_aplica()

    print("\n--- Verificación QFT² = P (inversión) ---")
    verificar_qft_cuadrado()

    print("\n--- Verificación QFT⁴ = I ---")
    verificar_qft_cuarta()

    print("\n--- Circuitos QFT y QFT† ---")
    qft_en_phase_estimation()
