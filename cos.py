import numpy as np
import matplotlib.pyplot as plt

N = 10
p = np.pi
X1 = []
X2 = []
X3 = []
f1 = -3 * p
f2 = -p
f3 = p
step = p / 50
while f1 < -p and f2 < p and f3 < 3 * p:
    X1.append(f1)
    f1 += step
    X2.append(f2)
    f2 += step
    X3.append(f3)
    f3 += step


def f(X):
    y = []
    for x in X:
        y_arg = 0
        for k in range(1, 3):
            y_arg += (np.cos((k * x) / 3)) * (1 / (3 * p)) * ((54 / (k ** 3 - 9 * k)) * np.sin((p * k) / 3))
        for k in range(4, 10):
            y_arg += (np.cos((k * x) / 3)) * (1 / (3 * p)) * ((54 / (k ** 3 - 9 * k)) * np.sin((p * k) / 3))
        y.append((5 / 3) - 1/3 * np.cos(x) + y_arg)
    return y


fig, ax = plt.subplots()
ax.set_title(f'Ряд Фурье {N}-ого порядка')
ax.plot(X1 + X2 + X3, f(X1 + X2 + X3), label='Ряд Фурье', color='red')
ax.plot(X1, [2] * len(X1), color='black', linewidth=1)
ax.plot(X2, [1 - np.cos(x) for x in X2], label='$f(x)$', color='black', linewidth=1)
ax.plot(X3, [2] * len(X3), color='black', linewidth=1)
ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Y')
ax.legend()
plt.show()
