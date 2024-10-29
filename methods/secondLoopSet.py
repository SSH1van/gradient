import sys
import time
import math
import random

# Объявление функции
def find_z(x, y):
    return (1 * x + 1) ** 2 + (1 * y + 1) ** 2 + 1 * math.sin(x * y)

# Генератор уникальных и случайных координат в заданном количестве, в заданном диапазоне
def generator_xy(xy_values, num_xy, left, right, file):
    right -= left
    max_num_xy = (right + 1) ** 2 - len(xy_values)
    if num_xy > max_num_xy:
        num_xy = max_num_xy
        s = f"The maximum number of coordinates has been changed to {num_xy}\n"
        print(s)
        file.write(s)

    right += left  
    while len(xy_values) < num_xy:
        xy_values.add((random.randint(left, right), random.randint(left, right)))
    return xy_values

# Вывод в терминал и запись в файл
def writeTerminalFile(s, x, y, z, step, file):
    step_info = f"\nNumber of steps: {step}\n" if step else ""
    s += f" x = {round(x, 4)}, y = {round(y, 4)}, z = {round(z, 4)}{step_info}"
    
    file.write(s + "\n")
    print(s)

# Запуск таймера, открытие файла для записи       
start_time = time.time()
file = open("output.txt", "w")

# Определение начальных координат, количества шагов, массива минимальных найденных значений функции,
# массива для предотвращения зацикливания, длины шага альфа, шага h 
left, right = -10, 10
num_xy = 500
xy_values = set()
xy_values = generator_xy(xy_values, num_xy, left, right, file)

# xy_values = [[-3, 4], [0, 2], [-1, 2], [-1, 1], [1, 2], [-2, 1], [0, 1], [1, 1], [1, 0], [2, 1], [2, 2], [-1, -1]]

# Example loop:
# (0.4 * x) ** 2 + (0.3 * y) ** 2 - 1 * math.sin(x * y)
# xy_values = [[3, 4], [0, 2], [-1, 2]]

n_steps = sys.maxsize
all_xyz_min = set()
mas_loop = []
alpha = 0.1
h = 0.0001
print("In process...")

# Цикл перебора начальных координат
while xy_values:
    xy_value = xy_values.pop()
    x, y = xy_value[0], xy_value[1]
    z = find_z(x, y)

    writeTerminalFile(f"Initial data:", x, y, z, None, file)

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
            min_z_loop = min(mas_loop)
            all_xyz_min.add((min_z_loop, round(x, 4), round(y, 4)))
            writeTerminalFile(f"Final data:", x, y, min_z_loop, step, file)
            break

# Нахождение минимального значения из найденных экстремумов
xyz_min = min(all_xyz_min)
z_min, x_min, y_min = xyz_min

# Остановка таймера
end_time = time.time()
elapsed_time = round(end_time - start_time, 3)

# Вывод в файл и в командную строку
s = f"\nFinal data: x = {x_min}, y = {y_min}\nMIN: z = {z_min}\n\nElapsed time: {elapsed_time}"
file.write(s)
file.close()
print(s)