import matplotlib.pyplot as plt

def read(path):
    with open(path, 'r') as file:
        N = int(file.readline())  
        points = []
        for _ in range(N):
            point = tuple(map(float, file.readline().split()))
            points.append(point)
    return points

def plot(points): 
    x, y = zip(*points)
    
    plt.scatter(x, y, color='blue', s=100)  
    plt.title("feirverk")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axis('equal')  
    plt.grid()  
    plt.show()  

path = 'C:/Python/001.txt'
points = read(path)
plot(points)
