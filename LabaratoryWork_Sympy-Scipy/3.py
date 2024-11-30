import sympy as sp
from sympy.abc import x
import scipy as sc
import numpy as np
import matplotlib.pyplot as plt

y = sp.Function('y')
t = np.linspace(0,10)
result = sp.dsolve(sp.Derivative(y(x),x)+2*y(x), y(x),ics={y(0): sp.sqrt(2)})

result_func = sp.lambdify(x, result.rhs, 'numpy')
values = np.array(result_func(t))

def func (y,t):
    f = -y * 2 + t*0
    return f
y = np.transpose(sc.integrate.odeint(func, np.sqrt(2), t))
y = y[0]


plt.figure(figsize=(12, 6))
plt.plot(t, y)
plt.plot(t,values )
plt.xlabel("t")
plt.ylabel("y")
plt.title("Сравнение решений SymPy и SciPy")
plt.grid()
plt.savefig('1.jpg')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(t, (values - y))
plt.xlabel("t")
plt.ylabel("Разность решений")
plt.title("Разность решений SymPy и SciPy")
plt.grid()
plt.savefig('2.jpg')
plt.show()