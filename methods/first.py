import math
import time

# Запуск таймера
start_time = time.time()

# Объявление функции
def find_z(x, y):
    return (1 * x + 1) ** 2 + (1 * y + 1) ** 2 + 1 * math.sin(x * y)

# Определение начальных координат
x = 5
y = 2
z = find_z(x, y)
print(f"x = {x}, y = {y}, z = {z}")

# Определение, шага конечных разностей h, длины шага альфа, количества шагов
h = 0.0001
alpha = 0.01
n_steps = 500
print("In process...")

# Цикл поиска экстремума
for i in range(n_steps):
    grad_x = (find_z(x + h, y) - find_z(x, y)) / h
    grad_y = (find_z(x, y + h) - find_z(x, y)) / h

    x = x - alpha * grad_x
    y = y - alpha * grad_y
    z = find_z(x, y)

    try:
        print(f"Step {i + 1}: x = {round(x, 4)}, y = {round(y, 4)}")
        print(f"z = {round(z, 4)}\n")
    except ValueError:
        print("\nValueError! Completion of the program\n")
        break

# z = find_z(x, y)
# print(f"x = {x}, y = {y}, z = {z}")

# Остановка таймера, вывод в терминал
end_time = time.time()
elapsed_time = round(end_time - start_time, 1)
print('Elapsed time: ', elapsed_time)