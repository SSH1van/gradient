from sympy import *
import sys
import random
import time

start_time = time.time()

file = open("output.txt", "w")

# Объявление функции
x, y = symbols('x y')
z = (1 * x + 1) ** 2 + (1 * y + 1) ** 2 + 1 * sin(x * y)

#z = (0.4 * x + 0.3) ** 4 + (0.5 * y + 0.1) ** 2 + 1 * sin(x * y)

file.write(f"Function: {z}\n")

# Нахождение частных производных
dz_dx = diff(z, x)
dz_dy = diff(z, y)
s = f"dz_dx = {dz_dx}, dz_dy = {dz_dy}\n"
file.write(s + "\n")
print(s)

# Определение начальных координат, количества шагов, массива минимальных найденных значений функции, длины шага альфа, скорости убывания бетта
xy_values = [[random.randint(-5, 5) for _ in range(2)] for _ in range(8)]
n_steps = sys.maxsize
all_z_min = []
alpha_0 = 0.01
betta_0 = 0.001
print("In process...")

# Цикл перебора начальных координат
for xy_val in xy_values:
    z_val = 0
    x_val, y_val = xy_val[0], xy_val[1]
    
    s = f"Initial data: x = {round(x_val, 4)}, y = {round(y_val, 4)}"
    file.write(s + "\n")
    print(s)

    # Цикл поиска экстремумов для разных начальных координат
    for i in range(n_steps):
        grad_x = dz_dx.subs({x: x_val, y: y_val}).evalf()
        grad_y = dz_dy.subs({x: x_val, y: y_val}).evalf()
        grad_f = sqrt(grad_x ** 2 + grad_y ** 2 + 1)

        betta = betta_0 * grad_f
        alpha =  alpha_0 * exp(-betta * i)

        x_val = (x_val - alpha * grad_x).evalf()
        y_val = (y_val - alpha * grad_y).evalf()

        if (z_val != z.subs({x: x_val, y: y_val}).evalf()) and i < 1000:
            z_val = z.subs({x: x_val, y: y_val}).evalf()
        else:
            all_z_min.append(z_val)
            s = f"x = {round(x_val, 4)}, y = {round(y_val, 4)}, z = {round(z_val, 4)}\nNumber of steps: {i}\n"
            file.write(s + "\n")
            print(s)
            break

# Нахождение минимального значения из найденных экстремумов
z_min = min(all_z_min)
z_i = all_z_min.index(z_min)

end_time = time.time()
elapsed_time = round(end_time - start_time, 1)

s = f"MIN: z = {round(z_min, 4)}\nInitial data: x = {round(xy_values[z_i][0], 4)}, y = {round(xy_values[z_i][1], 4)}\n\nElapsed time: {elapsed_time}"
file.write(s)
file.close()
print(s)