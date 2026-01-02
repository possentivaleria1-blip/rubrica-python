import tkinter as tk
from tkinter import simpledialog, messagebox, font
import os

# File contatti
file_contatti = "contatti.txt"

# Carica contatti
contatti = []
if os.path.exists(file_contatti):
    with open(file_contatti, "r", encoding="utf-8") as f:
        contatti = [line.strip() for line in f.readlines()]

# Funzioni principali
def aggiorna_lista():
    listbox.delete(0, tk.END)
    for c in sorted(contatti):
        listbox.insert(tk.END, c)

def aggiungi():
    nome = simpledialog.askstring("Nome", "Inserisci nome")
    cognome = simpledialog.askstring("Cognome", "Inserisci cognome")
    if nome and cognome:
        contatto = f"{nome} {cognome}"
        contatti.append(contatto)
        with open(file_contatti, "a", encoding="utf-8") as f:
            f.write(contatto + "\n")
        aggiorna_lista()

def elimina():
    selezionato = listbox.curselection()
    if selezionato:
        contatto = listbox.get(selezionato)
        contatti.remove(contatto)
        with open(file_contatti, "w", encoding="utf-8") as f:
            for c in contatti:
                f.write(c + "\n")
        aggiorna_lista()
    else:
        messagebox.showinfo("Rubrica", "Seleziona un contatto da eliminare")

def cerca():
    ricerca = simpledialog.askstring("Cerca", "Inserisci nome o cognome da cercare")
    if ricerca:
        risultati = [c for c in contatti if ricerca.lower() in c.lower()]
        if risultati:
            messagebox.showinfo("Risultati ricerca", "\n".join(risultati))
        else:
            messagebox.showinfo("Risultati ricerca", "Nessun contatto trovato.")

# Finestra principale
root = tk.Tk()
root.title("Rubrica Grafica Completa")
root.geometry("450x500")
root.configure(bg="#f0f0f0")

# Font personalizzato
font_lista = font.Font(family="Helvetica", size=12)

# Lista contatti
listbox = tk.Listbox(root, width=50, height=20, font=font_lista, bg="#ffffff", fg="#000000")
listbox.pack(pady=20)

# Frame pulsanti
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

tk.Button(frame, text="Aggiungi", width=12, bg="#4CAF50", fg="white", command=aggiungi).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="Elimina", width=12, bg="#f44336", fg="white", command=elimina).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="Cerca", width=12, bg="#2196F3", fg="white", command=cerca).grid(row=0, column=2, padx=5, pady=5)
tk.Button(frame, text="Chiudi", width=12, bg="#555555", fg="white", command=root.destroy).grid(row=0, column=3, padx=5, pady=5)

# Popola lista all'avvio
aggiorna_lista()

root.mainloop()
