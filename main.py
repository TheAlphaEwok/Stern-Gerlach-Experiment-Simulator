from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a simple 1-qubit circuit
qc = QuantumCircuit(1, 1)
qc.h(0)            # Hadamard gate (superposition)
qc.measure(0, 0)   # Measure in Z basis

# Set up the Aer simulator
simulator = AerSimulator()

# Run the circuit on the simulator
result = simulator.run(qc, shots=1000).result()

# Get measurement counts
counts = result.get_counts(qc)
print(counts)

# Plot the results
plot_histogram(counts)
plt.show()
