# 1. Imports
import tkinter as tk
import json
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("711x400")
        self.root.configure(bg="#f0f0f0")
        
        self.center_window()

        self.setup_ui()

        self.load_tasks()

    # 2. Funções
    # Função para centralizar a janela na tela
    def center_window(self):
        window_width = 711
        window_height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Confiuração da UI
    def setup_ui(self):
        """Configura a interface gráfica."""
        # Frame principal
        self.frame = tk.Frame(self.root, bg="#f0f0f0")
        self.frame.pack(pady=20)

        # Campo de entrada para novas tarefas
        self.entry = tk.Entry(self.frame, width=38, font=("Arial", 12))
        self.entry.grid(row=0, column=0, padx=5, pady=5)

        # Botão para adicionar tarefas
        self.add_button = tk.Button(
            self.frame, text="Adicionar", width=10, font=("Arial", 10),
            bg="#4CAF50", fg="white", command=self.add_task
        )
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        # Lista para exibir as tarefas
        self.listbox = tk.Listbox(
            self.frame, width=50, font=("Arial", 12), selectbackground="#a6a6a6"
        )
        self.listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Barra de rolagem
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.grid(row=1, column=2, sticky="ns")
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Frame para os botões de remover e concluir
        self.button_frame = tk.Frame(self.frame, bg="#f0f0f0")
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        # Botão para concluir tarefas
        self.complete_button = tk.Button(
            self.button_frame, text="Concluir", width=10, font=("Arial", 10),
            bg="#2196F3", fg="white", command=self.complete_task
        )
        self.complete_button.grid(row=0, column=0, padx=5)

        # Botão para remover tarefas
        self.remove_button = tk.Button(
            self.button_frame, text="Remover", width=10, font=("Arial", 10),
            bg="#FF5252", fg="white", command=self.remove_task
        )
        self.remove_button.grid(row=0, column=1, padx=5)

        # Botão para editar tarefas
        self.edit_button = tk.Button(
            self.button_frame, text="Editar", width=10, font=("Arial", 10),
            bg="#a8b319", fg="white", command=self.edit_task
        )
        self.edit_button.grid(row=1, column=0, padx=5, pady=5)

        # Botão para limpar tarefas
        self.clear_button = tk.Button(
            self.button_frame, text="Limpar", width=10, font=("Arial", 10),
            bg="#FF5252", fg="white", command=self.clear_tasks
        )
        self.clear_button.grid(row=1, column=1, padx=5, pady=5)

    # Função para salvar as tarefas em um arquivo JSON    
    def save_tasks(self):
        tasks = self.listbox.get(0, tk.END)
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)

    #Função para carregar as tarefas do arquivo JSON
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                tasks = json.load(f)
                for task in tasks:
                    self.listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

    # Função para adição de novas tarefas
    def add_task(self):
        task = self.entry.get()
        if task:
            if task.lower() not in [item.lower() for item in self.listbox.get(0, tk.END)]:
                self.listbox.insert(tk.END, task.capitalize())
                self.entry.delete(0, tk.END)
                self.save_tasks()
            else:
                messagebox.showwarning("Aviso", "Esta tarefa já existe!")
        else:
            messagebox.showwarning("Aviso", "Digite uma tarefa")

    # Função para remoção de tarefas
    def remove_task(self):
        selected_task = self.listbox.curselection()
        task = self.listbox.get(selected_task)
        if task[0] != f"✔":
            try:
                self.listbox.delete(selected_task)
                self.save_tasks()
            except:
                messagebox.showwarning("Aviso", "Selecione uma tarefa para remover!")
        else:
            remove_confirmation =messagebox.askyesno("Aviso", "Tem certeza que deseja remover uma tarefa já concluída?")
            if remove_confirmation:
                self.listbox.delete(selected_task)
                self.save_tasks()

    # Função para marcar tarefas concluídas
    def complete_task(self):
        selected_task = self.listbox.curselection()
        task = self.listbox.get(selected_task)
        if task[0] != f"✔":
            try:
                self.listbox.delete(selected_task)
                self.listbox.insert(tk.END, f"✔ {task}")
                self.save_tasks()
            except:
                messagebox.showwarning("Aviso", "Selecione uma tarefa para marcar como concluída!")
        else:
            messagebox.showwarning("Aviso", "Tarefa já concluída!")

    #  Função para editar tarefas
    def edit_task(self):
        try:
            selected_task = self.listbox.curselection()
            task = self.listbox.get(selected_task)
            new_task = simpledialog.askstring("Editar Tarefa", "Editar tarefa:", initialvalue=task)
            if new_task:
                self.listbox.delete(selected_task)
                self.listbox.insert(selected_task, new_task)
                self.save_tasks()
        except:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para editar!") 
    
    #  Função para limpar tarefas
    def clear_tasks(self):
        try:
            clear_confirmation = messagebox.askyesno("Aviso", "Tem certeza que deseja limpar todas as tarefas?")
            if clear_confirmation:
                self.listbox.delete(0, tk.END)
                self.save_tasks()
        except:
            messagebox.showwarning("Aviso", "Não há tarefas para limpar!")


# 3. Execução
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()