import numpy as np
import matplotlib.pyplot as plt

N = 50
p = np.pi
X1 = []
X2 = []
X3 = []
X4 = []
f1 = -3 * p
f2 = -p
f3 = 0
f4 = p
step = p / 50
while f1 < -p and f4 < 3 * p:
    X1.append(f1)
    f1 += step
    X4.append(f4)
    f4 += step
while f2 < 0 and f3 < p:
    X2.append(f2)
    f2 += step
    X3.append(f3)
    f3 += step


def f(X):
    y = []
    for x in X:
        y_arg = 0
        for k in range(1, 3):
            y_arg += (np.sin((k * x) / 3)) * (-1 / (3 * p)) * (
                        (54 / (k ** 3 - 9 * k)) * np.cos((p * k) / 3) + (12 * (-1) ** k) / k + 54 / (k ** 3 - 9 * k))
        for k in range(4, N):
            y_arg += (np.sin((k * x) / 3)) * (-1 / (3 * p)) * (
                        (54 / (k ** 3 - 9 * k)) * np.cos((p * k) / 3) + (12 * (-1) ** k) / k + 54 / (k ** 3 - 9 * k))
        y.append(4 / (3 * p) * np.sin(x) + y_arg)
    return y


fig, ax = plt.subplots()
ax.set_title(f'Ряд Фурье {N}-ого порядка')
ax.plot(X1 + X2 + X3 + X4, f(X1 + X2 + X3 + X4), label='Ряд Фурье', color='red')
ax.plot(X1, [-2] * len(X1), color='black', linewidth=1)
ax.plot(X2, [-1 + np.cos(x) for x in X2], label='$f(x)$', color='black', linewidth=1)
ax.plot(X3, [1 - np.cos(x) for x in X3], color='black', linewidth=1)
ax.plot(X4, [2] * len(X4), color='black', linewidth=1)
ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Y')
ax.legend()
plt.show()
