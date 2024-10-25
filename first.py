from sympy import *
import time

start_time = time.time()

# Объявление функции
x, y = symbols('x y')
z = (1 * x + 1) ** 2 + (1 * y + 1) ** 2 + 1 * sin(x * y)

# Нахождение частных производных
dz_dx = diff(z, x)
dz_dy = diff(z, y)
print(f"dz_dx = {dz_dx}, dz_dy = {dz_dy}")

# Определение начальных координат
x_val = 5
y_val = 2
z_val = z.subs({x: x_val, y: y_val}).evalf()
print(f"x = {x_val}, y = {y_val}, z = {z_val}")

# Определение длины шага альфа и количества шагов
alpha = 0.01
n_steps = 1000
print("In process...")

# Цикл поиска экстремума
for i in range(n_steps):
    grad_x = dz_dx.subs({x: x_val, y: y_val}).evalf()
    grad_y = dz_dy.subs({x: x_val, y: y_val}).evalf()

    x_val = (x_val - alpha * grad_x).evalf()
    y_val = (y_val - alpha * grad_y).evalf()
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