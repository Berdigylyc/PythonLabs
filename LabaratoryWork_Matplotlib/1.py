import matplotlib.pyplot as plt

def read_points(file_path):
    with open(file_path, 'r') as file:
        N = int(file.readline())  
        points = []
        for _ in range(N):
            point = tuple(map(float, file.readline().split()))
            points.append(point)
    return points

def plot_points(points): 
    x, y = zip(*points)
    
    plt.scatter(x, y, color='blue', s=100)  
    plt.title("Point Distribution")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.axis('equal')  
    plt.grid()  
    plt.show()  

file_path = 'C:/Python/001.txt'
points = read_points(file_path) 
plot_points(points)  