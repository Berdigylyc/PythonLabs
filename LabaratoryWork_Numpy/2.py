import numpy as np
import matplotlib.pyplot as plt

input_path = 'signals\\signal03.dat'

def read_data(file_path):
    data = np.loadtxt(file_path)
    return data

def getting_average(data, step):
    averaged_data = np.copy(data)
    for i in range(1, len(data)):
        averaged_data[i] = np.mean(data[max(0, i - step + 1):i + 1])
    return averaged_data

def plot_data(original_data, averaged_data, title="Original and averaged signal"):
    plt.figure(figsize=(10, 6))

    plt.plot(original_data, label='Original Data', color='blue', alpha=0.6)
    plt.plot(averaged_data, label='Averaged Data', color='red', alpha=0.8)

    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.savefig('3.jpg')
    plt.show()

def process_data(input_file_path, step=10):
    data = read_data(input_file_path)
    averaged_data = getting_average(data, step)
    plot_data(data, averaged_data, title=f"Signal averaged by step={step}")

process_data(input_path)
