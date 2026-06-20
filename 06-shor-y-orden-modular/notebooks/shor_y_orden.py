"""Implementaciones de Qiskit para 06-shor-y-orden-modular.
Orden modular, Shor simplificado y factorización."""

import math
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, Operator

sim = AerSimulator()

# ──────────────────────────────────────────────────────
# 1. Cálculo clásico del orden modular
# ──────────────────────────────────────────────────────

def orden_modular(a: int, N: int, max_r: int = 1000) -> int | None:
    """Encuentra el orden r de a módulo N: a^r ≡ 1 (mod N)."""
    if math.gcd(a, N) != 1:
        return None
    for r in range(1, max_r + 1):
        if pow(a, r, N) == 1:
            return r
    return None

def orden_via_crt(a: int, N: int) -> int | None:
    """Calcula el orden usando CRT si N es compuesto."""
    factores = factorizar(N)
    if factores is None:
        return orden_modular(a, N)

    ordenes = []
    for p, e in factores:
        m = p**e
        r_p = orden_modular(a % m, m)
        if r_p is None:
            return None
        ordenes.append(r_p)
    return np.lcm.reduce(ordenes)

def factorizar(n: int) -> list[tuple[int, int]] | None:
    """Factoriza n en primos (método simple de prueba de divisiones)."""
    if n < 2:
        return None
    factores = []
    temp = n
    for p in range(2, int(math.isqrt(temp)) + 1):
        if temp % p == 0:
            e = 0
            while temp % p == 0:
                temp //= p
                e += 1
            factores.append((p, e))
    if temp > 1:
        factores.append((temp, 1))
    return factores if factores else None

def demo_orden():
    """Demuestra cálculo de orden modular."""
    for a, N in [(13, 231), (3, 12155), (2, 15)]:
        r = orden_modular(a, N)
        print(f"  orden({a} mod {N}) = {r}")
        if r:
            print(f"    {a}^{r} mod {N} = {pow(a, r, N)}")

# ──────────────────────────────────────────────────────
# 2. Factorización vía orden (Shor clásico)
# ──────────────────────────────────────────────────────

def factorizar_via_orden(N: int, a: int = None) -> list[int] | None:
    """Intenta factorizar N usando el orden de a mod N."""
    if a is None:
        for a_candidate in range(2, N):
            if math.gcd(a_candidate, N) != 1:
                return [math.gcd(a_candidate, N), N // math.gcd(a_candidate, N)]
            r = orden_modular(a_candidate, N)
            if r and r % 2 == 0:
                if pow(a_candidate, r // 2, N) != N - 1:
                    p = math.gcd(pow(a_candidate, r // 2, N) - 1, N)
                    q = math.gcd(pow(a_candidate, r // 2, N) + 1, N)
                    if 1 < p < N and 1 < q < N:
                        return sorted([p, q])
    else:
        r = orden_modular(a, N)
        if r and r % 2 == 0 and pow(a, r // 2, N) != N - 1:
            p = math.gcd(pow(a, r // 2, N) - 1, N)
            q = math.gcd(pow(a, r // 2, N) + 1, N)
            if 1 < p < N:
                return sorted([p, q])
    return None

def demo_factorizacion():
    """Factoriza números usando orden modular."""
    for N, a in [(15, 2), (21, 2), (12155, 3)]:
        factores = factorizar_via_orden(N, a)
        print(f"  N={N}, a={a} → factores: {factores}")
        if factores:
            print(f"    {factores[0]} × {factores[1]} = {factores[0] * factores[1]}")

# ──────────────────────────────────────────────────────
# 3. Circuito de exponenciación modular (simplificado)
# ──────────────────────────────────────────────────────

def multiplicacion_modular_circuito(a: int, N: int, n_qubits: int) -> QuantumCircuit:
    """Crea un circuito que implementa |x⟩ → |a·x mod N⟩ (simplificado)."""
    qc = QuantumCircuit(n_qubits)
    for i in range(n_qubits):
        if (a * (2**i)) % N != 0:
            qc.x(i)
    return qc

def exponenciacion_modular_circuito(a: int, N: int, n_qubits: int, potencia: int) -> QuantumCircuit:
    """Circuito para U|x⟩ = |a^potencia · x mod N⟩."""
    exp = pow(a, potencia, N)
    qc = QuantumCircuit(n_qubits)
    for i in range(n_qubits):
        if (exp * (2**i)) % N != 0:
            qc.x(i)
    return qc

def circuito_shor_simplificado():
    """Muestra una versión conceptual del circuito de Shor."""
    n_count = 4
    n_target = 3
    a, N = 2, 15

    qr_c = QuantumRegister(n_count, "control")
    qr_t = QuantumRegister(n_target, "target")
    cr = ClassicalRegister(n_count)
    qc = QuantumCircuit(qr_c, qr_t, cr)

    qc.h(qr_c)
    qc.x(qr_t[0])

    for i in range(n_count):
        potencia = 2**i
        qc.compose(
            exponenciacion_modular_circuito(a, N, n_target, potencia).control(),
            qubits=[qr_c[i]] + list(qr_t),
            inplace=True,
        )

    qc.measure(qr_c, cr)
    print("Circuito de Shor (simplificado conceptual):")
    print(qc.draw("text", fold=-1))

# ──────────────────────────────────────────────────────
# 4. Demostración de costo
# ──────────────────────────────────────────────────────

def costo_shor(n: int):
    """Muestra la complejidad de Shor."""
    from qiskit.circuit.library import QFT

    n_qubits = n  # tamaño del número a factorizar
    print(f"  n = {n_qubits} qubits para representar N")
    print(f"  Exponenciación modular:  O({n_qubits}³)")
    print(f"  QFT:                     O({n_qubits}²)")
    print(f"  Euclides (clásico):      O({n_qubits}²)")
    print(f"  Costo total cuántico:    O({n_qubits}³)")
    print(f"  Mejor clásico conocido:  sub-exponencial")


if __name__ == "__main__":
    print("=" * 55)
    print("06 - SHOR Y ORDEN MODULAR")
    print("=" * 55)

    print("\n--- Cálculo del orden modular ---")
    demo_orden()

    print("\n--- Factorización vía orden ---")
    demo_factorizacion()

    print("\n--- Circuito de Shor (simplificado) ---")
    circuito_shor_simplificado()

    print("\n--- Costo y eficiencia ---")
    costo_shor(2048)
