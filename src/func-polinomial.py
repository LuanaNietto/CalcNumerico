import numpy as np
import matplotlib.pyplot as plt
# Polinomial de segundo grau

def f(x):
    return 1*x**3 - 4*x + 2

def bissecao(a, b, epsilon):
    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c  # Encontrou a raiz exata
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Intervalo para plotar o gráfico
x_vals = np.linspace(0.1, 2, 100)
y_vals = f(x_vals)

# Encontrar as raízes
raiz1 = bissecao(0.1, 0.5, 0.005)
raiz2 = bissecao(1, 2, 0.005)

print("Raiz 1:", raiz1)
print("Raiz 2:", raiz2)

plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(raiz1, color='red', linestyle='--', label='Raiz 1')
plt.axvline(raiz2, color='blue', linestyle='--', label='Raiz 2')
plt.title('Gráfico de f(x) e Raízes Aproximadas')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.savefig('meu_grafico_teste.png')
plt.show()
