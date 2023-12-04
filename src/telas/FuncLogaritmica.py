import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Logaritmica:
    def __init__(self):
        pass

    @staticmethod
    def calcular_logaritmo(x):
        return np.log(x)

class CalculadoraLogaritmicaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Função Logarítmica")        
        self.criar_widgets()

    def criar_widgets(self):
        ttk.Label(self.root, text="Valor Inicial:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.entrada_inicio = ttk.Entry(self.root)
        self.entrada_inicio.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Valor Final:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.entrada_fim = ttk.Entry(self.root)
        self.entrada_fim.grid(row=1, column=1, padx=10, pady=5)

        botao_calcular = ttk.Button(self.root, text="Calcular", command=self.calcular_e_plotar)
        botao_calcular.grid(row=2, column=0, columnspan=2, pady=10)

        self.figura, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.figura, master=self.root)
        self.widget_canvas = self.canvas.get_tk_widget()
        self.widget_canvas.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.resultado_var = tk.StringVar()
        self.resultado_var.set("")
        ttk.Label(self.root, textvariable=self.resultado_var, foreground='red').grid(row=4, column=0, columnspan=2, pady=5)

    def calcular_e_plotar(self):
        try:
            valor_inicial = float(self.entrada_inicio.get())
            valor_final = float(self.entrada_fim.get())

            x_vals = np.linspace(valor_inicial, valor_final, 100)
            y_vals = Logaritmica.calcular_logaritmo(x_vals)

            self.ax.clear()

            self.ax.plot(x_vals, y_vals, label='log(x)')
            self.ax.set_title('Gráfico da Função Logarítmica')
            self.ax.set_xlabel('x')
            self.ax.set_ylabel('log(x)')
            self.ax.legend()
            self.ax.grid(True)

            self.canvas.draw()

        except ValueError:
            self.resultado_var.set("Entrada inválida. Certifique-se de inserir números.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraLogaritmicaApp(root)
    root.mainloop()
