# %%
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere

# 创建 2-qubit 电路
qc1 = QuantumCircuit(2)
# 先将 qubit 0 变为叠加态，否则相位移不可见
qc1.h(0)
# 应用 90 度相位移 (pi/2)
qc1.p(np.pi/2, 0) 

# 获取状态向量并绘图
state = Statevector.from_instruction(qc1)
plot_state_qsphere(state)
# %%
