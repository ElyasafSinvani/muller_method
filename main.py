import matplotlib.pyplot as plt
import numpy as np
import cmath

# Realization of the function, its we want to find the roots
def f(x):
    return x ** 3 - x ** 2 - x - 1
# Realization of the parabola for intermediate results until the root is found
def P(x, a, b, c):
    return a * x ** 2 + b * x + c

x1 = 0
x2 = 1
x3 = 2
# xnm2 = -2
# xnm1 = -1
# xn = 0
epsilon = 10 ** -7
i = 0
print("n\txn\t\tf(xn)")
print("1\t" + str(x1) + "\t\t" + str(f(x1)))
print("2\t" + str(x2) + "\t\t" + str(f(x2)))
print("3\t" + str(x3) + "\t\t" + str(f(x3)))
while (abs(f(x3)) > epsilon):
    q = (x3 - x2) / (x2 - x1)
    a = q * f(x3) - q * (1 + q) * f(x2) + q ** 2 * f(x1)
    b = (2 * q + 1) * f(x3) - (1 + q) ** 2 * f(x2) + q ** 2 * f(x1)
    c = (1 + q) * f(x3)
    y = np.linspace(-5, 5)  # טווח להדפסה
    plt.plot(y, P(y, a, b, c))
    plt.show()
    # see which x intercept is better
    r = x3 - (x3 - x2) * ((2 * c) / (b + cmath.sqrt(b ** 2 - 4 * a * c)))
    s = x3 - (x3 - x2) * ((2 * c) / (b - cmath.sqrt(b ** 2 - 4 * a * c)))
    if (abs(f(r)) < abs(f(s))):
        xplus = r
    else:
        xplus = s
    if xplus.imag == 0j:  # result is real number
        xplus = xplus.real
        print(str(i + 4) + "\t" + str(round(xplus, 5)) + "\t\t" + str(round(f(xplus), 5)))
    else:
        print(str(i + 4) + "\t{:.4f}".format(xplus) + "\t{:.4f}".format(f(xplus)))
    x1 = x2
    x2 = x3
    x3 = xplus
    i = i + 1
print(str(i) + " iterations")

y = np.linspace(-5, 5)  # טווח להדפסה
plt.plot(y, f(y))
plt.show()

# when root is complex double check complex conjugate
if isinstance(xplus, complex):
    conjugate = complex(xplus.real, -xplus.imag)
    if abs(f(conjugate)) < epsilon:
        print("and \t{:.4f}".format(conjugate) + "\t{:.4f}".format(f(conjugate)))
