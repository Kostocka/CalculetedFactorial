import numpy as np
import matplotlib.pyplot as plt

def get_user_input():
    expr = input("Введите функцию от x (пример: x**2): ")
    a = float(input("Введите левую границу интегрирования (a): "))
    b = float(input("Введите правую границу интегрирования (b): "))
    n = int(input("Введите количество шагов (n): "))
    return expr, a, b, n

def f(x, expr):
    return eval(expr)

def integrate(expr, a, b, n):
    x = np.linspace(a, b, n + 1)     
    y = f(x, expr)          
    h = (b - a) / n
    area = (y[0] + 2 * sum(y[1:-1]) + y[-1]) * h / 2
    return area, x, y

def plot_function(x, y, expr, a, b, area):
    plt.figure(figsize=(10, 6))
    
    x_smooth = np.linspace(a, b, 500)
    y_smooth = f(x_smooth, expr)
    plt.plot(x_smooth, y_smooth, label=f'f(x) = {expr}', color='blue')

    plt.plot(x, y, 'o', color='red')

    for i in range(len(x) - 1):
        xs = [x[i], x[i], x[i+1], x[i+1]]
        ys = [0, y[i], y[i+1], 0]
        plt.fill(xs, ys, 'orange', alpha=0.3, edgecolor='black')

    plt.title(f"Интеграл от {a} до {b} ≈ {area:.5f}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    expr, a, b, n = get_user_input()
    # print(expr , a ,b,n)
    try:
        area, x, y = integrate(expr, a, b, n)
        print(f"Площадь под графиком: {area:.5f}")
        plot_function(x, y, expr, a, b, area)
    except Exception as e:
        print("Ошибка при вычислении:", e)

if __name__ == "__main__":
    main()