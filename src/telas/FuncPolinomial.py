import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Polinomial:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Polinomial")

        self.frame = ttk.Frame(master, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.label_a = ttk.Label(self.frame, text="Coeficiente a:")
        self.label_a.grid(row=0, column=0, sticky=tk.W)
        self.entry_a = ttk.Entry(self.frame)
        self.entry_a.grid(row=0, column=1)

        self.label_b = ttk.Label(self.frame, text="Coeficiente b:")
        self.label_b.grid(row=1, column=0, sticky=tk.W)
        self.entry_b = ttk.Entry(self.frame)
        self.entry_b.grid(row=1, column=1)

        self.label_c = ttk.Label(self.frame, text="Coeficiente c:")
        self.label_c.grid(row=2, column=0, sticky=tk.W)
        self.entry_c = ttk.Entry(self.frame)
        self.entry_c.grid(row=2, column=1)

        self.btn_calcular = ttk.Button(self.frame, text="Calcular", command=self.calcular_e_plotar)
        self.btn_calcular.grid(row=3, column=0, columnspan=2)

        self.label_resultado = ttk.Label(self.frame, text="")
        self.label_resultado.grid(row=4, column=0, columnspan=2)

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    def resolver_polinomio(self, a, b, c):
        delta = b**2 - 4*a*c
        if delta >= 0:
            x1 = (-b + np.sqrt(delta)) / (2*a)
            x2 = (-b - np.sqrt(delta)) / (2*a)
            return x1, x2
        else:
            return None

    def plotar_grafico(self, a, b, c, x_range=(-10, 10), num_pontos=100):
        x_vals = np.linspace(x_range[0], x_range[1], num_pontos)
        y_vals = a*x_vals**2 + b*x_vals - c
        return x_vals, y_vals

    def calcular_e_plotar(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            c = float(self.entry_c.get())

            raizes = self.resolver_polinomio(a, b, c)
            if raizes:
                self.label_resultado["text"] = f"Raízes: {raizes[0]:.2f} e {raizes[1]:.2f}"

                x_vals, y_vals = self.plotar_grafico(a, b, c)
                self.ax.clear()
                self.ax.plot(x_vals, y_vals, label=f'{a}x^2 + {b}x - {c}')
                self.ax.axhline(0, color='black', linewidth=0.5)
                self.ax.axvline(raizes[0], color='red', linestyle='--', label=f'Raiz 1: {raizes[0]:.2f}')
                self.ax.axvline(raizes[1], color='blue', linestyle='--', label=f'Raiz 2: {raizes[1]:.2f}')
                self.ax.legend()
                self.canvas.draw()
            else:
                self.label_resultado["text"] = "Raízes complexas."

        except ValueError:
            self.label_resultado["text"] = "Por favor, insira valores válidos."

if __name__ == "__main__":
    root = tk.Tk()
    app = Polinomial(root)
    root.mainloop()
