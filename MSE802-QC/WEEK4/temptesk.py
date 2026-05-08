# %%
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere

# create a quantum circuit with 2 qubits
qc1 = QuantumCircuit(2)
qc1.h(0)
qc1.p(np.pi/2, 0) 

# get the state vector and plot the qsphere
state = Statevector.from_instruction(qc1)
plot_state_qsphere(state)
# %%
