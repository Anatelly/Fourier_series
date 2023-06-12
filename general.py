import numpy as np
import matplotlib.pyplot as plt

N=5
p = np.pi
X1 = []
X2 = []
f1 = 0
f2 = p
step = p / 50
while f1 < p+step:
    X1.append(f1)
    f1 += step
while f2 < 3 * p:
    X2.append(f2)
    f2 += step


def f(X):
    y = []
    for x in X:
        y_arg = 0
        for k in range(1, N):
            y_arg += (np.cos((2 * k * x) / 3)) * (2 / (3 * p)) * ((27 / (8 * k ** 3 - 18 * k)) * np.sin((2 * p * k) / 3)
                                                                  ) - (np.sin((2 * x * k) / 3)) * (2 / (3 * p)) * (
                             (27 / (8 * k ** 3 - 18 * k)) * np.cos((2 * p * k) / 3) +
                             (24 * k ** 2 - 27) / (8 * k ** 3 - 18 * k))
        y.append((5 / 3) + y_arg)
    return y

fig, ax = plt.subplots()
ax.set_title(f'Общий ряд Фурье {N}-ого порядка')
ax.plot(X1 + X2, f(X1 + X2), label='Ряд Фурье', color='red')
ax.plot(X1, [1 - np.cos(x) for x in X1], label='$f(x)$', color='black', linewidth=1)
ax.plot(X2, [2] * len(X2), color='black', linewidth=1)
ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Y')
ax.legend()
plt.show()
