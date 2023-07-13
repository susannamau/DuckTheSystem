import tkinter as tk
import time
from tkinter import messagebox
import subprocess
import pyautogui

def open_notepad_and_write(string):
    subprocess.Popen(["notepad.exe"])
    time.sleep(1)  # Attendere un secondo per consentire il caricamento di Notepad
    pyautogui.typewrite(string)

def start_program():
    time_in_minutes = entry.get()
    try:
        time_in_minutes = int(time_in_minutes)
        time_in_seconds = time_in_minutes * 60
        messagebox.showinfo("Programma in esecuzione", f"Il programma funzionerà per {time_in_minutes} minuti.")
        time.sleep(time_in_seconds)
        messagebox.showinfo("Fine del programma", "Il programma è terminato.")
        open_notepad_and_write("Tempo trascorso: {} minuti".format(time_in_minutes))
    except ValueError:
        messagebox.showerror("Errore", "Inserisci un numero valido in minuti.")

window = tk.Tk()
window.title("Programma di esempio")
window.geometry("1000x800")

label = tk.Label(window, text="Inserisci il tempo in minuti:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Avvia", command=start_program)
button.pack()

window.mainloop()