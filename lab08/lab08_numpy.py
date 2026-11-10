import numpy as np

# ============================================================
# Задание 1. Создание векторов и матриц
# ============================================================

hours = np.arange(0, 22, 3)              # 0, 3, 6, ..., 21
line = np.linspace(0, 1, 5)              # 5 равноудалённых от 0 до 1
zeros = np.zeros(6, dtype=int)           # шесть нулей целого типа
unknown_table = np.full((2, 3), -1)      # матрица 2×3 из -1
identity = np.eye(3)                     # единичная 3×3

print("=== Задание 1 ===")
print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

# ============================================================
# Задание 2. Индексы и срезы в векторе
# ============================================================

print("\n=== Задание 2 ===")
print("третий элемент:", hours[2])
print("последний элемент:", hours[-1])
print("индексы 2–5:", hours[2:6])
print("каждый второй:", hours[::2])
print("в обратном порядке:", hours[::-1])

# ============================================================
# Задание 3. Строки и столбцы таблицы
# ============================================================

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("\n=== Задание 3 ===")
print("shape:", temperatures.shape)
print("ndim:", temperatures.ndim)
print("size:", temperatures.size)
print("вторая строка, третий столбец:", temperatures[1, 2])
print("первая строка:", temperatures[0])
print("последний столбец:", temperatures[:, -1])
print("первые две строки без первого столбца:\n", temperatures[:2, 1:])
print("центральный фрагмент 2×2:\n", temperatures[0:2, 1:3])

# ============================================================
# Задание 4. Прямоугольные срезы
# ============================================================

matrix = np.arange(1, 26).reshape(5, 5)

print("\n=== Задание 4 ===")
print("matrix:\n", matrix)

first_three = matrix[:3]
print("первые три строки:\n", first_three, "\nshape:", first_three.shape)

last_two = matrix[-2:]
print("последние две строки:\n", last_two, "\nshape:", last_two.shape)

first_two_cols = matrix[:, :2]
print("первые два столбца:\n", first_two_cols, "\nshape:", first_two_cols.shape)

middle = matrix[1:4, 2:5]
print("строки 1–3, столбцы 2–4:\n", middle, "\nshape:", middle.shape)

corner = matrix[-2:, -2:]
print("правый нижний угол 2×2:\n", corner, "\nshape:", corner.shape)

# ============================================================
# Задание 5. Изменение массива с помощью срезов
# ============================================================

# Примеры из условия
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

# .copy() нужна, потому что срез и присваивание меняют исходный массив.
# Если написать changed_hours = hours, это будет ссылка на тот же массив,
# и hours тоже изменится. .copy() создаёт независимую копию данных.
changed_hours = hours.copy()
changed_hours[2:5] = 99      # индексы 2, 3, 4
changed_hours[::2] = -1      # каждый второй, начиная с первого (индексы 0, 2, 4, 6)

print("\n=== Задание 5 ===")
print("changed_hours:", changed_hours)
print("исходный hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0          # вся вторая строка (индекс 1) — нули
changed_matrix[:, -1] = -1        # последний столбец — -1
changed_matrix[1:4, 1:4] = 100    # центральный блок 3×3 — 100

print("changed_matrix:\n", changed_matrix)
print("исходная matrix:\n", matrix)

# ============================================================
# Задание 6. Изменение формы
# ============================================================

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("\n=== Задание 6 ===")
print("numbers.shape:", numbers.shape)
print("table.shape:", table.shape)
print("transposed.shape:", transposed.shape)

# reshape(3, 4) работает, потому что 3 * 4 = 12 — столько же элементов,
# сколько в numbers. reshape(5, 3) вызвал бы ошибку: 5 * 3 = 15 ≠ 12.