import sys
import time
import math
import random

# Объявление функции
def find_z(x, y):
    return (1 * x + 1) ** 2 + (1 * y + 1) ** 2 + 1 * math.sin(x * y)

# Вывод в терминал и запись в файл
def writeTerminalFile(s, x, y, z, step, file):
    s = f"x = {round(x, 4)}, y = {round(y, 4)}, z = {round(z, 4)}\nNumber of steps: {step}\n"
    file.write(s + "\n")
    print(s)
        
start_time = time.time()
file = open("output.txt", "w")

# Определение начальных координат, количества шагов, массива минимальных найденных значений функции,
# массива для предотвращения зацикливания, длины шага альфа, шага h 
xy_values = [[random.randint(-5, 5) for _ in range(2)] for _ in range(500)]

# xy_values = [[-3, 4], [0, 2], [-1, 2], [-1, 1], [1, 2], [-2, 1], [0, 1], [1, 1], [1, 0], [2, 1], [2, 2], [-1, -1]]
# Example loop:
# (0.4 * x) ** 2 + (0.3 * y) ** 2 - 1 * math.sin(x * y)
# xy_values = [[3, 4], [0, 2], [-1, 2]]

n_steps = sys.maxsize
all_z_min = []
mas_loop = []
alpha = 0.1
h = 0.0001
print("In process...")

# Цикл перебора начальных координат
for xy_val in xy_values:
    x, y = xy_val[0], xy_val[1]
    z = find_z(x, y)
    s = f"Initial data: x = {round(x, 4)}, y = {round(y, 4)}"
    file.write(s + "\n")
    print(s)

    # Цикл поиска экстремумов для разных начальных координат
    for step in range(n_steps):
        grad_x = (find_z(x + h, y) - find_z(x, y)) / h
        grad_y = (find_z(x, y + h) - find_z(x, y)) / h

        x = x - alpha * grad_x
        y = y - alpha * grad_y
        
        if not round(find_z(x, y), 4) in mas_loop and z < 999999:
            z = find_z(x, y)
            if len(mas_loop) > 20:
                    mas_loop.pop(0)
            mas_loop.append(round(z, 4))
        else:
            if mas_loop:
                all_z_min.append(min(mas_loop))
            else:
                all_z_min.append(z)
            writeTerminalFile(s, x, y, all_z_min[-1], step, file)
            break

# Нахождение минимального значения из найденных экстремумов
z_min = min(all_z_min)
z_i = all_z_min.index(z_min)

end_time = time.time()
elapsed_time = round(end_time - start_time, 1)

s = f"\nInitial data: x = {round(xy_values[z_i][0], 4)}, y = {round(xy_values[z_i][1], 4)}\nMIN: z = {round(z_min, 4)}\n\nElapsed time: {elapsed_time}"
file.write(s)
file.close()
print(s)