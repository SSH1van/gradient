import sys
import time
import math

# Объявление функции
def find_z(x, y):
    return (1 * x + 1) ** 2 + (1 * y + 1) ** 2 + 1 * math.sin(x * y)

# Вывод в терминал и запись в файл
def writeTerminalFile(s, x, y, z, step, file):
    step_info = f"\nNumber of steps: {step}\n" if step else ""
    s += f" x = {round(x, 4)}, y = {round(y, 4)}, z = {round(z, 4)}{step_info}"
    
    file.write(s + "\n")
    print(s)

# Определение шага по x и y
def xy_step(x_start, x_end, y_start, y_end):
    x_len = x_end - x_start
    y_len = y_end - y_start
    x_step = x_len / 33
    y_step = y_len / 33
    return(x_step, y_step)

# Рекурсивная функция сетки координат
def grid(x_start, x_end, y_start, y_end):
    x_step, y_step = xy_step(x_start, x_end, y_start, y_end)

    min_value = float('inf')
    min_point = (None, None)

    x = x_start
    while x <= x_end:
        y = y_start
        while y <= y_end:
            value = find_z(x, y)
            if value < min_value:
                min_value = value
                min_point = (x, y)
            y += y_step
        x += x_step

    x, y = min_point
    
    if x == 0:
        x_start = -10
        x_end = 10
    else:
        x_start = x - abs(x)
        x_end = x + abs(x)

    if y == 0:
        y_start = -10
        y_end = 10
    else:
        y_start = y - abs(y)
        y_end = y + abs(y)

    x_step, y_step = xy_step(x_start, x_end, y_start, y_end)
    if (x_step + y_step) / 2 < 0.1:
        return min_point
    return grid(x_start, x_end, y_start, y_end)

# Запуск таймера, открытие файла для записи       
start_time = time.time()
file = open("output.txt", "w")

# Определение количества шагов, массива минимальных найденных значений функции, длины шага альфа, шага h
n_steps = sys.maxsize
mas_loop = []
alpha = 0.1
h = 0.0001
print("In process...")

# Определение начальных координат
x_start, x_end = -10, 10
y_start, y_end = -10, 10
x, y = grid(x_start, x_end, y_start, y_end)
x, y = 3, 4
z = find_z(x, y)
writeTerminalFile(f"Initial data:", x, y, z, None, file)

# Цикл поиска экстремума для начальных координат
for step in range(n_steps):
    grad_x = (find_z(x + h, y) - find_z(x, y)) / h
    grad_y = (find_z(x, y + h) - find_z(x, y)) / h

    x -= alpha * grad_x
    y -= alpha * grad_y
    
    # Проверяем что в массиве некоторое количество одинаковых значений
    z = round(find_z(x, y), 4)
    if mas_loop.count(z) < 3 and z < 999999:
        if len(mas_loop) > 20:
                mas_loop.pop(0)
        mas_loop.append(z)
    else:
        z_min = min(mas_loop)
        writeTerminalFile(f"Final data:", x, y, z_min, step, file) 
        break

# Остановка таймера
end_time = time.time()
elapsed_time = round(end_time - start_time, 3)

# Вывод в файл и в командную строку
s = f"Elapsed time: {elapsed_time}"
file.write(s)
file.close()
print(s)