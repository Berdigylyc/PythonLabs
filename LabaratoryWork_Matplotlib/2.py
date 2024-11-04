import matplotlib.pyplot as plt

def read_time_series(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines() 
        return [list(map(float, line.split())) for line in lines]

def plot(series):
   
    num_frames = len(series) // 2  
    for i in range(num_frames):
      
        x = series[i * 2]  
        y = series[i * 2 + 1]  
        
      
        plt.plot(x, y, marker='o', markersize=1)  
        plt.title(f"Frame {i + 1}") 
        plt.xlim(min(x) - 5, max(x) + 5)  
        plt.ylim(min(y) - 5, max(y) + 5) 
        plt.grid()  
        plt.show()
        plt.savefig("Frame")
file_path = 'C:/Python/series.txt' 
series = read_time_series(file_path) 
plot(series) 
