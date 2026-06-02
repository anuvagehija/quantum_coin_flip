# coin flip
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")


def coin_flip(num_qubits=1, num_shots=1000):
    qc = QuantumCircuit(num_qubits, num_qubits)

    for i in range(num_qubits):
        qc.h(i)

    qc.measure(range(num_qubits), range(num_qubits))

    simulator = AerSimulator()
    result = simulator.run(qc, shots=num_shots).result()
    counts = result.get_counts(qc)
    return qc, counts


def save_histogram(counts, title, filename):
    # saves relative to wherever this script lives
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "output")
    os.makedirs(output_dir, exist_ok=True)
    fig = plot_histogram(counts, title=title)
    fig.savefig(
        os.path.join(output_dir, f"{filename}.png"), dpi=150, bbox_inches="tight"
    )
    plt.close(fig)
    print(f"Saved: {os.path.join(output_dir, filename)}.png")


if __name__ == "__main__":
    for n in [1, 2, 3]:
        qc, counts = coin_flip(num_qubits=n, num_shots=1000)

        print(f"\n--- {n} qubit(s) ---")
        print(counts)
        print(qc.draw())

        save_histogram(counts, f"{n}-Qubit Coin Flip (1000 shots)", f"coinflip_{n}q")
