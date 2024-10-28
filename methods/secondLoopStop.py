import sys
import time
import math
import random

# Объявление функции
def find_z(x, y):
    return (1 * x + 1) ** 2 + (1 * y + 1) ** 2 + 1 * math.sin(x * y)

# Генератор уникальных и случайных координат в заданном количестве, в заданном диапазоне
def generator_xy(xy_values, num_xy, left, right, file):
    max_num_xy = (abs(left) + abs(right) + 1) ** 2 - len(xy_values)
    if num_xy > max_num_xy:
        num_xy = max_num_xy
        s = f"The maximum number of coordinates has been changed to {num_xy}\n"
        print(s)
        file.write(s)
        
    count = 0
    while count < num_xy:
        x, y = random.randint(left, right), random.randint(left, right)
        if [x, y] not in xy_values:
            xy_values.append([x, y])
            count += 1 
    return xy_values

# Вывод в терминал и запись в файл
def writeTerminalFile(s, x, y, z, step, file):
    s = f"x = {round(x, 4)}, y = {round(y, 4)}, z = {round(z, 4)}\nNumber of steps: {step}\n"
    file.write(s + "\n")
    print(s)

# Запуск таймера, открытие файла для записи       
start_time = time.time()
file = open("output.txt", "w")

# Определение начальных координат, количества шагов, массива минимальных найденных значений функции,
# массива для предотвращения зацикливания, длины шага альфа, шага h 
xy_values = generator_xy([], 500, -5, 5, file)

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

# Остановка таймера
end_time = time.time()
elapsed_time = round(end_time - start_time, 3)

# Вывод в файл и в командную строку
s = f"\nInitial data: x = {round(xy_values[z_i][0], 4)}, y = {round(xy_values[z_i][1], 4)}\nMIN: z = {round(z_min, 4)}\n\nElapsed time: {elapsed_time}"
file.write(s)
file.close()
print(s)