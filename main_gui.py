import tkinter as tk
from tkinter import messagebox
from test_login import test_login
from test_search_product import test_search_product, test_load

class TestSuiteGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Test Suite GUI")
        self.root.geometry("400x300")
        
        # Criação dos botões
        self.login_button = tk.Button(root, text="Executar Teste de Login", command=self.run_login_test)
        self.login_button.pack(pady=10)
        
        self.search_button = tk.Button(root, text="Executar Teste de Pesquisa", command=self.run_search_test)
        self.search_button.pack(pady=10)
        
        self.load_test_button = tk.Button(root, text="Executar Teste de Carga", command=self.run_load_test)
        self.load_test_button.pack(pady=10)
    
    def run_login_test(self):
        try:
            test_login()
            messagebox.showinfo("Resultado", "Teste de Login concluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao executar o teste de login: {e}")
    
    def run_search_test(self):
        try:
            test_search_product("smartphone")  # Substitua por um produto específico se desejar
            messagebox.showinfo("Resultado", "Teste de Pesquisa concluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao executar o teste de pesquisa: {e}")
    
    def run_load_test(self):
        product_names = ["smartphone", "notebook", "television", "air fryer", "headphones"]
        try:
            test_load(product_names)
            messagebox.showinfo("Resultado", "Teste de Carga concluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao executar o teste de carga: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TestSuiteGUI(root)
    root.mainloop()
