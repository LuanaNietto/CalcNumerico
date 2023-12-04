import tkinter as tk
from FuncLogaritmica import CalculadoraLogaritmicaApp
from FuncPolinomial import Polinomial
class TelaInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("Escolha 1 das funções")

        func_log = tk.Button(root, text="Função Logarítmica", command= self.func_log)
        func_log.pack(pady=10)

        func_poli = tk.Button(root, text="Função polinomial de 2ªGrau", command= self.func_poli)
        func_poli.pack(pady=10)

    def func_log(self):
        root1 = tk.Tk()
        CalculadoraLogaritmicaApp(root1)

    def func_poli(self):
        root1 = tk.Tk()
        Polinomial(root1)    

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaInicial(root)
    root.mainloop()
