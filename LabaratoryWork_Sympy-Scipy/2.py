import scipy as sc
import matplotlib.pyplot as plt

path = 'values.txt'
with open (path,'r') as f:
    data = f.readlines()

k = int(data[0])
A = [[float(elm) for elm in line.split()] for line in data[1:k+1]]
B = [[float(elm) for elm in line.split()] for line in data[k+1:k+2]]
b = B[0]
x = sc.linalg.solve(A,b, lower=False, overwrite_a=False, overwrite_b=False, check_finite=True, assume_a='gen', transposed=False)

n = ([i for i in range (k)])
plt.bar(n, x, width=0.4, bottom=None,  align='center', data=None)
plt.grid(True)
plt.savefig('1.jpg')
plt.show()
