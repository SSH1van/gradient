from sympy import *

def getFuntion(x, y):
    return 2 * x ** 2 + y ** 2 - 1

x, y = symbols('x y')
dz_dx = diff(2 * x ** 2 + y ** 2 - 1, x)
dz_dy = diff(2 * x ** 2 + y ** 2 - 1, y)
print(dz_dx)
print(dz_dy)

x_val = 1
y_val = 1

alpha = 0.01
n_steps = 500
for i in range(n_steps):
    grad_x = dz_dx.subs({x: x_val, y: y_val})
    grad_y = dz_dy.subs({x: x_val, y: y_val})
    
    x_val = x_val - alpha * grad_x
    y_val = y_val - alpha * grad_y

    z = getFuntion(x_val, y_val)
    print(f"Шаг {i+1}: x = {x_val}, y = {y_val}")
    print(z)

# z = getFuntion(x_val, y_val)
# print(z)