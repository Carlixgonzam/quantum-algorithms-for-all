"""Implementaciones de Qiskit para 01-costo-de-circuitos-y-compuertas.
Tamaño, profundidad, conjuntos universales y simulación booleana."""

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.quantum_info import Operator
from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import CollectMultiQBlocks

# ──────────────────────────────────────────────────────
# 1. Tamaño y profundidad de un circuito
# ──────────────────────────────────────────────────────

def construir_circuito_ejemplo() -> QuantumCircuit:
    """Circuito de 5 qubits: tamaño=10, profundidad=4."""
    qc = QuantumCircuit(5)
    qc.h(0)
    qc.cx(0, 1)
    qc.h(2)
    qc.cx(2, 3)
    qc.cx(0, 2)
    qc.h(4)
    qc.cx(1, 4)
    qc.cx(3, 4)
    qc.h(3)
    qc.measure_all()
    return qc

def metricas_circuito(qc: QuantumCircuit):
    """Calcula tamaño y profundidad de un circuito."""
    size = qc.size()
    depth = qc.depth()
    print(f"  Tamaño (número de compuertas):    {size}")
    print(f"  Profundidad (capas paralelas):    {depth}")
    print(f"  Número de qubits:                 {qc.num_qubits}")
    return size, depth

# ──────────────────────────────────────────────────────
# 2. Conjuntos universales de compuertas
# ──────────────────────────────────────────────────────

def demostrar_conjunto_universal():
    """Muestra que {H, T, CNOT} aproxima cualquier compuerta."""
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.t(0)
    qc.t(1)
    qc.cx(0, 1)
    qc.tdg(1)
    qc.cx(0, 1)
    qc.t(0)
    qc.tdg(1)
    qc.h(0)

    op = Operator(qc)
    print("Circuito con H, T, CNOT:")
    print(qc.draw("text"))
    print(f"Matriz resultante (2-qubit):\n{op.data.round(4)}")

# ──────────────────────────────────────────────────────
# 3. Simulación de circuitos booleanos reversibles
# ──────────────────────────────────────────────────────

def circuito_and_reversible() -> QuantumCircuit:
    """AND reversible con Toffoli: |a⟩|b⟩|0⟩ → |a⟩|b⟩|a∧b⟩."""
    qc = QuantumCircuit(3, 1)
    qc.ccx(0, 1, 2)
    qc.measure(2, 0)
    return qc

def circuito_or_reversible() -> QuantumCircuit:
    """OR reversible usando De Morgan: a∨b = ¬(¬a ∧ ¬b)."""
    qc = QuantumCircuit(4, 1)
    qc.x(0)
    qc.x(1)
    qc.ccx(0, 1, 2)
    qc.x(2)
    qc.measure(2, 0)
    return qc

def demostrar_simulacion_booleana():
    """Demuestra cómo simular compuertas booleanas con 1 qubit extra."""
    print("Circuito AND reversible (Toffoli):")
    print(circuito_and_reversible().draw("text"))

    print("\nCircuito OR reversible (De Morgan + Toffoli):")
    print(circuito_or_reversible().draw("text"))

# ──────────────────────────────────────────────────────
# 4. Análisis de distintas bases de compuertas
# ──────────────────────────────────────────────────────

def comparar_bases():
    """Compara circuitos implementados con diferentes conjuntos universales."""
    def make_circuit(base_gate):
        qc = QuantumCircuit(2)
        if base_gate == "cx":
            qc.h(0)
            qc.cx(0, 1)
        elif base_gate == "cz":
            qc.h(0)
            qc.h(1)
            qc.cz(0, 1)
            qc.h(1)
        elif base_gate == "iswap":
            qc.iswap(0, 1)
        return qc

    for nombre in ["cx", "cz", "iswap"]:
        qc = make_circuit(nombre)
        print(f"Base con {nombre:>6} | tamaño={qc.size():>2}, profundidad={qc.depth():>2}")


if __name__ == "__main__":
    print("=" * 55)
    print("01 - COSTO DE CIRCUITOS Y COMPUERTAS")
    print("=" * 55)

    print("\n--- Métricas de circuito ejemplo ---")
    qc = construir_circuito_ejemplo()
    print(qc.draw("text"))
    metricas_circuito(qc)

    print("\n--- Conjunto universal {H, T, CNOT} ---")
    demostrar_conjunto_universal()

    print("\n--- Simulación booleana reversible ---")
    demostrar_simulacion_booleana()

    print("\n--- Comparación de bases ---")
    comparar_bases()
