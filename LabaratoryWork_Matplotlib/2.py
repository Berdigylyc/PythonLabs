import matplotlib.pyplot as plt
def read(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        return [list(map(float, line.split())) for line in lines]

def plot(series):
    number = len(series) // 2

    x_min = min(min(series[i * 2]) for i in range(number))
    x_max = max(max(series[i * 2]) for i in range(number))
    y_min = min(min(series[i * 2 + 1]) for i in range(number))
    y_max = max(max(series[i * 2 + 1]) for i in range(number))

    d_x = (x_max - x_min) * 0.1
    d_y = (y_max - y_min) * 0.1

    for i in range(number):
        x = series[i * 2]
        y = series[i * 2 + 1]

        plt.plot(x, y, marker='o', markersize=1)
        plt.title(f"freym {i + 1}")

        plt.xlim(x_min - d_x, x_max + d_x)
        plt.ylim(y_min - d_y, y_max + d_y)

        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.minorticks_on()
        plt.grid(True, which='minor', linestyle=':', linewidth=0.5)
        plt.savefig(f"C:/Python/freym_{i + 1}.png")
        plt.show()
        plt.clf()

path = 'C:/Python/series.txt'
series = read(path)
plot(series)
