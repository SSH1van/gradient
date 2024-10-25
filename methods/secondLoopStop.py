from sympy import *
import sys
import random
import time

# Нахождение среднего квадратичного экстремумов
def average(mas):
    average = sum(mas) / len(mas)
    summ = 0
    for element in mas:
        summ += (average - element) ** 2
    return(sqrt(summ / len(mas)))

# Вывод в терминал и запись в файл
def writeTerminalFile(s, x_val, y_val, z_val, step, file):
    s = f"x = {round(x_val, 4)}, y = {round(y_val, 4)}, z = {round(z_val, 4)}\nNumber of steps: {step}\n"
    file.write(s + "\n")
    print(s)
        
start_time = time.time()

file = open("output.txt", "w")

# Объявление функции
x, y = symbols('x y')
z = (1 * x + 1) ** 2 + (1 * y + 1) ** 2 + 1 * sin(x * y)
file.write(f"Function: {z}\n")

# Определение начальных координат, количества шагов, массива минимальных найденных значений функции, длины шага альфа, скорости убывания бетта
xy_values = [[random.randint(-5, 5) for _ in range(2)] for _ in range(50)]

# xy_values = [[-3, 4], [0, 2], [-1, 2], [-1, 1], [1, 2], [-2, 1], [0, 1], [1, 1], [1, 0], [2, 1], [2, 2], [-1, -1]]
# Example loop:
# xy_values = [[3, -5], [0, 2], [-1, 2]]

n_steps = sys.maxsize
all_z_min = []
alpha = 0.1
h = 0.0001
print("In process...")

# Цикл перебора начальных координат
for xy_val in xy_values:
    z_val = 0
    x_val, y_val = xy_val[0], xy_val[1]
    z_loop = 1
    z_bool = True
    
    s = f"Initial data: x = {round(x_val, 4)}, y = {round(y_val, 4)}"
    file.write(s + "\n")
    print(s)

    # Цикл поиска экстремумов для разных начальных координат
    for step in range(n_steps):
        grad_x = (z.subs({x: x_val + h, y: y_val}).evalf() - z.subs({x: x_val, y: y_val}).evalf()) / h
        grad_y = (z.subs({x: x_val, y: y_val + h}).evalf() - z.subs({x: x_val, y: y_val}).evalf()) / h

        x_val = x_val - alpha * grad_x
        y_val = y_val - alpha * grad_y

        old_grad_x = grad_x
        old_grad_y = grad_y

        if round(z_val, 4) != round(z.subs({x: x_val, y: y_val}).evalf(), 4) and z_val < 999999 and round(z_loop, 4) != round(z.subs({x: x_val, y: y_val}).evalf(), 4):
            z_val = z.subs({x: x_val, y: y_val}).evalf()

            if z_bool:
                z_loop = z_val
                z_bool = False
            else:
                z_bool = True
        else:
            all_z_min.append(z_val)
            writeTerminalFile(s, x_val, y_val, z_val, step, file)
            break

    # Условие остановки или добавления новых точек
    # if len(all_z_min) % 3 == 0: 
    #     if len(all_z_min) == 9: 
    #         break
    #     elif average(all_z_min) < 0.01:
    #         xy_values.extend([[random.randint(-5, 5) for _ in range(2)] for _ in range(3)])
    #     else: 
    #         break


# Нахождение минимального значения из найденных экстремумов
z_min = min(all_z_min)
z_i = all_z_min.index(z_min)

end_time = time.time()
elapsed_time = round(end_time - start_time, 1)

s = f"Initial data: x = {round(xy_values[z_i][0], 4)}, y = {round(xy_values[z_i][1], 4)}\nMIN: z = {round(z_min, 4)}\n\nElapsed time: {elapsed_time}"
file.write(s)
file.close()
print(s)