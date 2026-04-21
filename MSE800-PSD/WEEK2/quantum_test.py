# %%
import qiskit as qk
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector
import numpy as np
import math


qc1 = QuantumCircuit(1, 1)

# Apply Hadamard gate
qc1.h(0)

# Measure the qubit
qc1.measure(0, 0)

print("Circuit:")
display(qc1.draw(output='mpl'))

simulator = AerSimulator()
job = simulator.run(qc1, shots=1024)
result = job.result()
counts = result.get_counts(qc1)

print("Measurement counts:", counts)
plot_histogram(counts)


# %%
