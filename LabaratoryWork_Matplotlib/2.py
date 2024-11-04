import matplotlib.pyplot as plt

def read(path):
    with open(path, 'r') as file:
        lines = file.readlines() 
        return [list(map(float, line.split())) for line in lines]

def plot(series):
   
    number = len(series) // 2  
    for i in range(number):
      
        x = series[i * 2]  
        y = series[i * 2 + 1]  
        
      
        plt.plot(x, y, marker='o', markersize=1)  
        plt.title(f"freym {i + 1}") 
        plt.xlim(min(x) - 5, max(x) + 5)  
        plt.ylim(min(y) - 5, max(y) + 5) 
        plt.grid()  
        plt.savefig(f"C:/Python/freym_{i + 1}.png") 
        plt.show()
        plt.clf()
path = 'C:/Python/series.txt' 
series = read(path) 
plot(series) 
