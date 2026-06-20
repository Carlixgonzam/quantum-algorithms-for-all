"""Implementaciones de Qiskit para 02-deutsch-jozsa-y-simon.
Algoritmos: Deutsch original, Deutsch-Jozsa moderno, Simon."""

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

sim = AerSimulator()

# ──────────────────────────────────────────────────────
# 1. Deutsch original (1985) — sin phase kickback
# ──────────────────────────────────────────────────────

def circuito_deutsch_original(oracle: QuantumCircuit) -> QuantumCircuit:
    """Circuito Deutsch original (2° qubit en |0⟩, no |−⟩)."""
    qc = QuantumCircuit(2, 1)
    qc.h(0)
    qc.compose(oracle, inplace=True)
    qc.h(0)
    qc.measure(0, 0)
    return qc

def oracle_deutsch_constante() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    return qc

def oracle_deutsch_balanceada() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    qc.cx(0, 1)
    return qc

def deutsch_original():
    """Ejecuta Deutsch original y muestra la diferencia."""
    qc_const = circuito_deutsch_original(oracle_deutsch_constante())
    qc_bal = circuito_deutsch_original(oracle_deutsch_balanceada())

    qc_const = transpile(qc_const, sim)
    qc_bal = transpile(qc_bal, sim)

    result_const = sim.run(qc_const, shots=1024).result()
    result_bal = sim.run(qc_bal, shots=1024).result()

    p0_const = result_const.get_counts().get("0", 0) / 1024
    p0_bal = result_bal.get_counts().get("0", 0) / 1024

    print(f"  Constante: P(0) = {p0_const:.3f}  (esperado 1.0)")
    print(f"  Balanceada: P(0) = {p0_bal:.3f}  (esperado 0.5)")

# ──────────────────────────────────────────────────────
# 2. Deutsch-Jozsa moderno — con phase kickback
# ──────────────────────────────────────────────────────

def oracle_dj(n: int, tipo: str, s: str = None) -> QuantumCircuit:
    """Oracle para Deutsch-Jozsa moderno."""
    qc = QuantumCircuit(n + 1)
    if tipo == "constante":
        if s == "1":
            qc.x(n)
    elif tipo == "balanceado":
        for i, bit in enumerate(s):
            if bit == "1":
                qc.cx(i, n)
    return qc

def algoritmo_dj(n: int, tipo: str, s: str = None) -> dict:
    """Circuito completo de Deutsch-Jozsa."""
    qc = QuantumCircuit(n + 1, n)
    qc.x(n)
    qc.h(range(n + 1))
    qc.compose(oracle_dj(n, tipo, s), inplace=True)
    qc.h(range(n))
    qc.measure(range(n), range(n))

    qc = transpile(qc, sim)
    result = sim.run(qc, shots=1024).result()
    counts = result.get_counts()
    return counts

def deutsch_jozsa_moderno():
    """Ejecuta Deutsch-Jozsa moderno con oracle constante y balanceado."""
    n = 3
    s = "101"

    print(f"\n  n={n}, s={s}")
    print("  Oracle constante (f=0):")
    counts_const = algoritmo_dj(n, "constante", "0")
    print(f"    {counts_const}")
    print(f"    ¿mide 000? → {'Constante ✓' if '000' in counts_const else 'Balanceada ✓'}")

    print("  Oracle balanceado:")
    counts_bal = algoritmo_dj(n, "balanceado", s)
    print(f"    {counts_bal}")
    print(f"    ¿mide 000? → {'Constante' if '000' in counts_bal else 'Balanceada ✓'}")

# ──────────────────────────────────────────────────────
# 3. Deutsch-Jozsa sin promesa
# ──────────────────────────────────────────────────────

def funcion_parcial(n: int, bits_uno: int) -> QuantumCircuit:
    """Oracle donde exactamente `bits_uno` inputs tienen f(x)=1.
    Usa el primer qubit como flag: si x < bits_uno, f(x)=1."""
    qc = QuantumCircuit(n + 1)
    # Construimos un marcador para x < bits_uno usando comparador cuántico
    # Simplificación: usamos un oracle que marca los primeros `bits_uno` estados
    for x in range(bits_uno):
        bin_str = format(x, f"0{n}b")
        for i, bit in enumerate(bin_str):
            if bit == "0":
                qc.x(i)
        qc.mcx(list(range(n)), n)
        for i, bit in enumerate(bin_str):
            if bit == "0":
                qc.x(i)
    return qc

def dj_sin_promesa():
    """Muestra que DJ es probabilístico sin la promesa."""
    n = 3
    N = 2**n
    for frac in [0.0, 0.25, 0.5]:
        bits_uno = int(frac * N)
        oracle = funcion_parcial(n, bits_uno)
        qc = QuantumCircuit(n + 1, n)
        qc.x(n)
        qc.h(range(n + 1))
        qc.compose(oracle, inplace=True)
        qc.h(range(n))
        qc.measure(range(n), range(n))
        qc = transpile(qc, sim)
        counts = sim.run(qc, shots=4096).result().get_counts()
        p_zero = counts.get("0" * n, 0) / 4096
        k = bits_uno
        p_teorica = ((N - 2 * k) / N) ** 2
        print(f"  k={k}/{N} (f=1 en {frac*100:.0f}%) → P(0^n) = {p_zero:.4f}  (teórica = {p_teorica:.4f})")

# ──────────────────────────────────────────────────────
# 4. Algoritmo de Simon
# ──────────────────────────────────────────────────────

def oracle_simon(n: int, s: str) -> QuantumCircuit:
    """Oracle de Simon: f(x) = f(y) si y = x ⊕ s."""
    qc = QuantumCircuit(2 * n)
    if s == "0" * n:
        for i in range(n):
            qc.cx(i, n + i)
    else:
        for i in range(n):
            qc.cx(i, n + i)
        for i in range(n):
            if s[i] == "1":
                for j in range(n):
                    qc.cx(i, n + j)
    return qc

def algoritmo_simon(n: int, s: str, shots: int = 1024) -> list:
    """Ejecuta una ronda de Simon y devuelve mediciones de y."""
    qc = QuantumCircuit(2 * n, n)
    qc.h(range(n))
    qc.compose(oracle_simon(n, s), inplace=True)
    qc.h(range(n))
    qc.measure(range(n), range(n))

    qc = transpile(qc, sim)
    result = sim.run(qc, shots=shots).result()
    counts = result.get_counts()
    return list(counts.keys())

def simon_demo():
    """Demostración del algoritmo de Simon."""
    n = 3
    s = "110"
    print(f"\n  n={n}, s={s}")
    mediciones = algoritmo_simon(n, s)
    print(f"  Mediciones y (primeras 8): {mediciones[:8]}")
    for y in mediciones[:5]:
        y_bits = [int(b) for b in y]
        producto = sum(y_bits[i] * int(s[i]) for i in range(n)) % 2
        print(f"    y={y}, y·s mod 2 = {producto}  {'✓' if producto == 0 else '✗'}")

# ──────────────────────────────────────────────────────
# 5. Simon sin promesa
# ──────────────────────────────────────────────────────

def oracle_simon_sin_promesa(n: int) -> QuantumCircuit:
    """Oracle donde cada preimagen tiene tamaño 2^(n-1)."""
    qc = QuantumCircuit(2 * n)
    for i in range(n):
        qc.cx(i, n + i)
    return qc

def simon_sin_promesa():
    """Simon sin promesa: no garantiza y·s=0."""
    n = 3
    mediciones = algoritmo_simon(n, "0" * n, shots=2048)
    print(f"\n  Mediciones (sin promesa): {mediciones[:10]}")


if __name__ == "__main__":
    print("=" * 55)
    print("02 - DEUTSCH-JOZSA Y SIMON")
    print("=" * 55)

    print("\n--- Deutsch original (1985) ---")
    deutsch_original()

    print("\n--- Deutsch-Jozsa moderno ---")
    deutsch_jozsa_moderno()

    print("\n--- Deutsch-Jozsa sin promesa ---")
    dj_sin_promesa()

    print("\n--- Algoritmo de Simon ---")
    simon_demo()

    print("\n--- Simon sin promesa ---")
    simon_sin_promesa()
