import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return 2 * x

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()




# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Інтеграл: ", result, error)

import random

# Розміри прямокутника
w = 2  # ширина прямокутника
h = 4  # висота прямокутника

def is_inside(w, h, x, y):
    """Перевіряє, чи знаходиться точка (x, y) всередині трикутника."""
    return y <= (h / w) * x

# Генерація випадкових точок
points = [(random.uniform(0, w), random.uniform(0, h)) for _ in range(1500)]

# Відбір точок, що знаходяться всередині трикутника
inside_points = [point for point in points if is_inside(w, h, point[0], point[1])]

# Кількість усіх точок та точок всередині
N = len(points)
M = len(inside_points)

# Теоретична площа трикутника та площа, обчислена методом Монте-Карло
S = (w * h) / 2  # Теоретична площа
Sm = (M / N) * (w * h)  # Площа за методом Монте-Карло

# Виведення результатів
print(f"Кількість точок всередині трикутника: {M}, загальна кількість точок: {N}")
print(f"Теоретична площа трикутника: {S}, площа за методом Монте-Карло: {Sm}")

print("Похибка:", abs(S - Sm))
print("Відносна похибка:", abs(S - Sm) / S * 100, "%")
print('Для функції яку мені легко перевірити бачима що метод обчислення площі за допомогою Монте-Карло працює без великої похибки')