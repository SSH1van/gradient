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
    count = 0
    while count < num_xy:
        x, y = random.randint(left, right), random.randint(left, right)
        if [x, y] not in xy_values:
            xy_values.append([x, y])
            count += 1 
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
# массива для предотвращения зацикливания, длины шага альфа, шага конечных разностей h
left, right = -10, 10
num_xy = 500
xy_values = generator_xy([], num_xy, left, right, file)

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
    writeTerminalFile(f"Initial data:", x, y, z, None, file)

    # Цикл поиска экстремумов для разных начальных координат
    for step in range(n_steps):
        grad_x = (find_z(x + h, y) - find_z(x, y)) / h
        grad_y = (find_z(x, y + h) - find_z(x, y)) / h

        x -= alpha * grad_x
        y -= alpha * grad_y
        
        z = round(find_z(x, y), 4)
        if mas_loop.count(z) < 3 and z < 999999:
            if len(mas_loop) > 20:
                    mas_loop.pop(0)
            mas_loop.append(z)
        else:
            if mas_loop:
                min_z_loop = min(mas_loop)
                all_z_min.append(min_z_loop)
                writeTerminalFile(f"Final data:", x, y, min_z_loop, step, file)
            break

# Нахождение минимального значения из найденных экстремумов
z_min = min(all_z_min)
z_i = all_z_min.index(z_min)
x_min_initial, y_min_initial = xy_values[z_i][0], xy_values[z_i][1]

# Остановка таймера
end_time = time.time()
elapsed_time = round(end_time - start_time, 3)

# Вывод в файл и в командную строку
s = f"\nInitial data: x = {round(x_min_initial, 4)}, y = {round(y_min_initial, 4)}\nMIN: z = {round(z_min, 4)}\n\nElapsed time: {elapsed_time}"
file.write(s)
file.close()
print(s)