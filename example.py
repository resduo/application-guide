from qiskit.circuit.library import XGate
gate = XGate()
print(gate.to_matrix())             # X gate
print(gate.power(1/2).to_matrix())  # √X gate
print(gate.control(1).to_matrix())  # CX (controlled X) gate