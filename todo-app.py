# 1. Imports
import tkinter as tk
from tkinter import messagebox

# 2. Funções
# Função para adição de novas tarefas
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa")

# Função para remoção de tarefas
def remove_task():
    selected_task = listbox.curselection()
    task = listbox.get(selected_task)
    if task[0] != f"✔":
        try:
            listbox.delete(selected_task)
        except:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para remover!")
    else:
        confirmacao_exclusao =messagebox.askyesno("Aviso", "Tem certeza que deseja remover uma tarefa já concluída?")
        if confirmacao_exclusao:
            listbox.delete(selected_task)

# Função para marcar tarefas concluídas
def mark_completed():
    selected_task = listbox.curselection()
    task = listbox.get(selected_task)
    if task[0] != f"✔":
        try:
            listbox.delete(selected_task)
            listbox.insert(tk.END, f"✔ {task}")
        except:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para marcar como concluída!")
    else:
        messagebox.showwarning("Aviso", "Tarefa já concluída!")

# 3. Execução
# Janela principal
window_height = 400
window_width = 711
root = tk.Tk()

root.title("To-Do List")

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="#f0f0f0")

#Frame para organizar os widgets
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

# Campo de texto para adição de novas tarefas
entry = tk.Entry(frame, width=38, font=("Arial", 12))
entry.grid(row=0, column=0, padx=5, pady=5)

# Botão para adicionar tarefas
button = tk.Button(frame, text="Adicionar", width=10, font=("Arial", 10), bg="#4CAF50", fg="white", command=add_task)
button.grid(row=0, column=1, padx=5, pady=5)

# Lista para exibir as tarefas
listbox = tk.Listbox(frame, width=50, font=("Arial", 12), selectbackground="#a6a6a6")
listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

#Frame para os botões de remover e concluir tarefas
button_frame = tk.Frame(frame, bg="#f0f0f0")
button_frame.grid(row=2, column=0, columnspan=2, pady=10)

# Botão para concluir tarefas
complete_button = tk.Button(button_frame, text="Concluir", width=10, font=("Arial", 10), bg="#2196F3", fg="white", command=mark_completed)
complete_button.grid(row=0, column=0, padx=5)

# Botão para remover tarefas
remove_button = tk.Button(button_frame, text="Remover", width=10, font=("Arial", 10), bg="#FF5252", fg="white", command=remove_task)
remove_button.grid(row=0, column=1, padx=5)


root.mainloop()