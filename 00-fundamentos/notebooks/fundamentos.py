"""Implementaciones de Qiskit para 00-fundamentos.
Compuertas básicas, matrices unitarias y modelo de consultas."""

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.quantum_info import Operator, Statevector, partial_trace, entropy
from qiskit.visualization import plot_histogram

# ──────────────────────────────────────────────────────
# 1. Verificación de unitariedad
# ──────────────────────────────────────────────────────

def es_unitaria(matriz: np.ndarray, tol: float = 1e-10) -> bool:
    U = np.asarray(matriz, dtype=complex)
    n = U.shape[0]
    if U.shape != (n, n):
        return False
    prod = U.conj().T @ U
    return np.allclose(prod, np.eye(n), atol=tol)

def verificar_unitarias():
    """Verifica que las compuertas comunes son unitarias."""
    compuertas = {
        "H": [[1, 1], [1, -1]] / np.sqrt(2),
        "X": [[0, 1], [1, 0]],
        "Y": [[0, -1j], [1j, 0]],
        "Z": [[1, 0], [0, -1]],
        "S": [[1, 0], [0, 1j]],
        "T": [[1, 0], [0, np.exp(1j * np.pi / 4)]],
        "CNOT": [[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]],
        "Toffoli": np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0, 0, 0, 0],
                              [0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 1, 0, 0, 0, 0],
                              [0, 0, 0, 0, 1, 0, 0, 0],
                              [0, 0, 0, 0, 0, 1, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 1],
                              [0, 0, 0, 0, 0, 0, 1, 0]]),
    }
    for nombre, matriz in compuertas.items():
        ok = es_unitaria(matriz)
        print(f"{nombre:>8} | U†U = I? {ok}")

# ──────────────────────────────────────────────────────
# 2. Eigenvalores de matrices unitarias
# ──────────────────────────────────────────────────────

def eigenvalores_unitarias():
    """Muestra que los eigenvalores están en el círculo unitario."""
    names = ["H", "X", "Y", "Z", "S", "T"]
    mats = [
        np.array([[1, 1], [1, -1]]) / np.sqrt(2),
        np.array([[0, 1], [1, 0]]),
        np.array([[0, -1j], [1j, 0]]),
        np.array([[1, 0], [0, -1]]),
        np.array([[1, 0], [0, 1j]]),
        np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]]),
    ]
    for name, mat in zip(names, mats):
        evals = np.linalg.eigvals(mat)
        angulos = np.angle(evals)
        print(f"{name}: eigenvalores = {evals}, |λ| = {np.abs(evals)}, θ = {angulos}")

# ──────────────────────────────────────────────────────
# 3. Modelo de consultas: oracle de Deutsch-Jozsa
# ──────────────────────────────────────────────────────

def oracle_dj_constante(n: int) -> QuantumCircuit:
    """Oracle que devuelve siempre 0 (constante)."""
    qc = QuantumCircuit(n + 1)
    return qc

def oracle_dj_balanceada(n: int) -> QuantumCircuit:
    """Oracle balanceado: f(x) = x·s mod 2 con s = 1...1."""
    qc = QuantumCircuit(n + 1)
    s = "1" * n
    for i, bit in enumerate(s):
        if bit == "1":
            qc.cx(i, n)
    return qc

def demostrar_oracles():
    """Muestra los circuitos oracle."""
    n = 3
    print("Oracle constante (f=0):")
    print(oracle_dj_constante(n).draw("text"))
    print("\nOracle balanceado (s=111):")
    print(oracle_dj_balanceada(n).draw("text"))

# ──────────────────────────────────────────────────────
# 4. Simulación de compuertas con Statevector
# ──────────────────────────────────────────────────────

def simular_compuerta():
    """Aplica H y X a |0⟩ y muestra el statevector."""
    qc = QuantumCircuit(1)
    qc.h(0)
    qc.x(0)

    sv = Statevector(qc)
    print(f"Estado final: {sv}")
    print(f"Probabilidad |0⟩: {sv.probabilities()[0]:.4f}")
    print(f"Probabilidad |1⟩: {sv.probabilities()[1]:.4f}")


if __name__ == "__main__":
    print("=" * 55)
    print("00 - FUNDAMENTOS: Compuertas y unitariedad")
    print("=" * 55)

    print("\n--- Verificación de unitariedad ---")
    verificar_unitarias()

    print("\n--- Eigenvalores ---")
    eigenvalores_unitarias()

    print("\n--- Oracles de consulta ---")
    demostrar_oracles()

    print("\n--- Simulación básica ---")
    simular_compuerta()
