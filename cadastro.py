import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from cachorro import Cachorro
from gato import Gato

animais = []

def cadastrar_animal():
    nome = entry_nome.get()
    idade = entry_idade.get()
    tipo = var_tipo.get()
    porteraca = entry_porteraca.get()

    if not (nome and idade and porteraca):
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    try:
        idade = int(idade)
    except ValueError:
        messagebox.showerror("Erro", "Idade deve ser um número!")
        return

    if tipo == "Cachorro":
        animal = Cachorro(nome, idade, porteraca)
    elif tipo == "Gato":
        animal = Gato(nome, idade, porteraca)
    else:
        messagebox.showerror("Erro", "Tipo de animal inválido!")
        return

    animais.append(animal)
    messagebox.showinfo("Sucesso", f"{tipo} cadastrado com sucesso!")
    atualizar_lista()

def atualizar_lista():
    listbox.delete(0, tk.END)
    for animal in animais:
        listbox.insert(tk.END, animal.mostrar())

janela = tk.Tk()
janela.title("Cadastro de Animais")
janela.geometry("400x300")

notebook = ttk.Notebook(janela)
notebook.pack(expand=1, fill="both")

tab_cadastro = ttk.Frame(notebook)
notebook.add(tab_cadastro, text="Cadastro")

tab_lista = ttk.Frame(notebook)
notebook.add(tab_lista, text="Lista de Animais")

ttk.Label(tab_cadastro, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_nome = ttk.Entry(tab_cadastro)
entry_nome.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

ttk.Label(tab_cadastro, text="Idade:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_idade = ttk.Entry(tab_cadastro)
entry_idade.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

ttk.Label(tab_cadastro, text="Porte/Raça:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_porteraca = ttk.Entry(tab_cadastro)
entry_porteraca.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

ttk.Label(tab_cadastro, text="Tipo:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
var_tipo = tk.StringVar(value="Cachorro")
ttk.Radiobutton(tab_cadastro, text="Cachorro", variable=var_tipo, value="Cachorro").grid(row=3, column=1, sticky="w", padx=10)
ttk.Radiobutton(tab_cadastro, text="Gato", variable=var_tipo, value="Gato").grid(row=3, column=1, sticky="e", padx=10)

ttk.Button(tab_cadastro, text="Cadastrar", command=cadastrar_animal).grid(row=4, column=0, columnspan=2, pady=10)

listbox = tk.Listbox(tab_lista, font=("Arial", 12))
listbox.pack(expand=1, fill="both", padx=10, pady=10)

ttk.Button(tab_lista, text="Atualizar Lista", command=atualizar_lista).pack(pady=5)

janela.mainloop()
