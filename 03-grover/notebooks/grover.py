"""Implementaciones de Qiskit para 03-grover.
Algoritmo de búsqueda de Grover: geometría, iteraciones, casos extremos."""

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, Operator
from qiskit.circuit.library import MCXGate, ZGate

sim = AerSimulator()

# ──────────────────────────────────────────────────────
# 1. Oracle y difusor de Grover
# ──────────────────────────────────────────────────────

def mcz_gate(n: int) -> QuantumCircuit:
    """Multi-control Z (CC...CZ) usando Z.control()."""
    qc = QuantumCircuit(n)
    if n == 1:
        qc.z(0)
    else:
        qc.append(ZGate().control(n - 1), range(n))
    return qc

def oracle_grover(n: int, objetivo: int) -> QuantumCircuit:
    """Marca |objetivo⟩ con fase -1.
    En Qiskit qubit 0 = LSB, por eso desplazamos bits."""
    qc = QuantumCircuit(n)
    for qb in range(n):
        if not (objetivo >> qb) & 1:
            qc.x(qb)
    qc.compose(mcz_gate(n), inplace=True)
    for qb in range(n):
        if not (objetivo >> qb) & 1:
            qc.x(qb)
    return qc

def difusor_grover(n: int) -> QuantumCircuit:
    """Operador de difusión D = 2|s⟩⟨s| - I."""
    qc = QuantumCircuit(n)
    qc.h(range(n))
    qc.x(range(n))
    qc.compose(mcz_gate(n), inplace=True)
    qc.x(range(n))
    qc.h(range(n))
    return qc

# ──────────────────────────────────────────────────────
# 2. Circuito completo de Grover
# ──────────────────────────────────────────────────────

def grover(n: int, objetivo: int, iteraciones: int, shots: int = 4096) -> dict:
    """Circuito completo de Grover."""
    qc = QuantumCircuit(n, n)
    qc.h(range(n))
    for _ in range(iteraciones):
        qc.compose(oracle_grover(n, objetivo), inplace=True)
        qc.compose(difusor_grover(n), inplace=True)
    qc.measure(range(n), range(n))

    qc = transpile(qc, sim, optimization_level=1)
    result = sim.run(qc, shots=shots).result()
    return result.get_counts()

# ──────────────────────────────────────────────────────
# 3. Verificación con statevector
# ──────────────────────────────────────────────────────

def grover_sv(n: int, objetivo: int, iteraciones: int) -> Statevector:
    """Grover sin medición, devuelve statevector."""
    qc = QuantumCircuit(n)
    qc.h(range(n))
    for _ in range(iteraciones):
        qc.compose(oracle_grover(n, objetivo), inplace=True)
        qc.compose(difusor_grover(n), inplace=True)
    return Statevector(qc)

def verificar_grover():
    """Verifica que Grover funciona con statevector (sin ruido de muestreo)."""
    n = 3
    objetivo = 5  # |101⟩
    N = 2**n
    M = 1

    sv = grover_sv(n, objetivo, 0)
    p0 = sv.probabilities()[objetivo]
    print(f"  t=0: P(|{objetivo:0{n}b}⟩) = {p0:.4f}  (esperado {1/N:.4f})")

    t_opt = int(np.round(np.pi / 4 * np.sqrt(N / M) - 0.5))
    sv = grover_sv(n, objetivo, t_opt)
    p_opt = sv.probabilities()[objetivo]
    P_teorica = np.sin((2 * t_opt + 1) * np.arcsin(np.sqrt(M / N))) ** 2
    print(f"  t={t_opt} (óptimo): P(|{objetivo:0{n}b}⟩) = {p_opt:.4f}  (teórica: {P_teorica:.4f})")

# ──────────────────────────────────────────────────────
# 4. Número óptimo de iteraciones
# ──────────────────────────────────────────────────────

def iteraciones_optimas(N: int, M: int) -> int:
    """Calcula el número óptimo de iteraciones de Grover."""
    theta = np.arcsin(np.sqrt(M / N))
    t = int(np.round((np.pi / (4 * theta)) - 0.5))
    return max(t, 0)

def probar_iteraciones():
    """Muestra el efecto del número de iteraciones.
    El oracle marca un solo estado (M=1)."""
    n = 5
    N = 2**n
    M = 1
    objetivo = 7
    t_opt = iteraciones_optimas(N, M)

    print(f"  N={N}, M={M}, θ={np.arcsin(np.sqrt(M/N)):.4f}")
    print(f"  Iteraciones óptimas: t = {t_opt}")

    for t in [0, 1, t_opt, t_opt + 2, 2 * t_opt]:
        sv = grover_sv(n, objetivo, t)
        prob_objetivo = sv.probabilities()[objetivo]
        P_teorica = np.sin((2 * t + 1) * np.arcsin(np.sqrt(M / N))) ** 2
        print(f"  t={t:>2} | P(objetivo) = {prob_objetivo:.4f}  (teórica: {P_teorica:.4f})")

# ──────────────────────────────────────────────────────
# 5. Caso balanceado (M = N/2)
# ──────────────────────────────────────────────────────

def oracle_multi_sol(n: int) -> QuantumCircuit:
    """Oracle que marca M = N/2 estados (|q₀=1⟩)."""
    qc = QuantumCircuit(n)
    qc.h(0)
    qc.cx(0, 1)
    return qc

def caso_balanceado():
    """Grover cuando la mitad de los elementos son solución.
    Oracle: marca estados con q₀=1 (M = N/2)."""
    n = 2
    N = 2**n
    M = N // 2

    qc = QuantumCircuit(n)
    qc.h(range(n))
    qc.compose(oracle_multi_sol(n), inplace=True)

    print(f"  Caso balanceado: N={N}, M={M}")
    for t in range(5):
        qc_t = QuantumCircuit(n)
        qc_t.h(range(n))
        for _ in range(t):
            qc_t.compose(oracle_multi_sol(n), inplace=True)
            qc_t.compose(difusor_grover(n), inplace=True)
        sv = Statevector(qc_t)
        # Probabilidad de medir un estado con q₀=1
        prob = sum(sv.probabilities()[i] for i in range(N) if i & (1 << (n - 1)))
        P_teorica = np.sin((2 * t + 1) * np.arcsin(np.sqrt(M / N))) ** 2
        print(f"  t={t} | P(q₀=1 | solución) = {prob:.4f}  (teórica: {P_teorica:.4f})")

# ──────────────────────────────────────────────────────
# 6. Periodic demonstration
# ──────────────────────────────────────────────────────

def periodicidad():
    """Muestra que Grover es periódico: la probabilidad sube y baja."""
    n = 3
    N = 2**n
    M = 1
    objetivo = 3

    print(f"  N={N}, M={M}")
    for t in range(0, 10):
        sv = grover_sv(n, objetivo, t)
        prob = sv.probabilities()[objetivo]
        P_teorica = np.sin((2 * t + 1) * np.arcsin(np.sqrt(M / N))) ** 2
        marca = ""
        if prob > 0.9:
            marca = " ← máxima"
        elif prob < 0.1:
            marca = " ← mínima"
        print(f"  t={t} | P(objetivo) = {prob:.4f} (teórica: {P_teorica:.4f}){marca}")


if __name__ == "__main__":
    print("=" * 55)
    print("03 - ALGORITMO DE GROVER")
    print("=" * 55)

    print("\n--- Verificación con statevector ---")
    verificar_grover()

    print("\n--- Iteraciones óptimas ---")
    probar_iteraciones()

    print("\n--- Caso balanceado M=N/2 ---")
    caso_balanceado()

    print("\n--- Periodicidad de Grover ---")
    periodicidad()
