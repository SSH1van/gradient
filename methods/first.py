from sympy import *
import time

start_time = time.time()

# Объявление функции
x, y = symbols('x y')
z = (1 * x + 1) ** 2 + (1 * y + 1) ** 2 + 1 * sin(x * y)

# Определение начальных координат
x_val = 5
y_val = 2
z_val = z.subs({x: x_val, y: y_val}).evalf()
print(f"x = {x_val}, y = {y_val}, z = {z_val}")

# Определение длины шага альфа и количества шагов
h = 0.0001
alpha = 0.01
n_steps = 500
print("In process...")

# Цикл поиска экстремума
for i in range(n_steps):
    grad_x = (z.subs({x: x_val + h, y: y_val}).evalf() - z.subs({x: x_val, y: y_val}).evalf()) / h
    grad_y = (z.subs({x: x_val, y: y_val + h}).evalf() - z.subs({x: x_val, y: y_val}).evalf()) / h


    x_val = x_val - alpha * grad_x
    y_val = y_val - alpha * grad_y
    z_val = z.subs({x: x_val, y: y_val}).evalf()

    try:
        print(f"Step {i+1}: x = {round(x_val, 4)}, y = {round(y_val, 4)}")
        print(f"z = {round(z_val, 4)}\n")
    except ValueError:
        print("\nValueError! Completion of the program\n")
        break

# z_val = z.subs({x: x_val, y: y_val}).evalf()
# print(f"x_val = {x_val}, y_val = {y_val}, z_val = {z_val}")

end_time = time.time()
elapsed_time = round(end_time - start_time, 1)
print('Elapsed time: ', elapsed_time)