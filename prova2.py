import os
import tkinter as tk
import time
from tkinter import messagebox
import subprocess
import pyautogui
from PIL import Image, ImageTk
from tkinter import font

##### Definizione delle funzioni ############################################################

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


##### Se è in alto a sinistra ###############################################################

pyautogui.click(50,50)

''' # ciclo infinito 
while(True):
    pyautogui.write('AutoDucker in control! Duck The System!', interval=0.25)
    pyautogui.press('enter')
'''

##### Creazione della finestra di dialogo con l'utente ######################################

window = tk.Tk()

#Titolo
window.title("DuckTheSystem")

#Dimensione
window.geometry("1000x950")

#Icona
ico = Image.open('duck.jpg')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)

#Testo
label = tk.Label(window, text="\n For how many minutes do you want to DuckTheSystem?")
font_tuple = ("Segoe UI", 10, "bold")
label.pack()
label.configure(font = font_tuple)
'''
your_font = font.nametofont("TkDefaultFont")  # Get default font value into Font object
print(your_font.actual())
{'family': 'Segoe UI', 'size': 9, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0} # default
'''

#Input di testo
entry = tk.Entry(window)
entry.pack() # questo aggiunge lo spazio in cui scrivere nella finestra di dialogo
entry.insert(0, "30") # questo è pre-impostato
entry.pack(pady = 30)

#Tick
var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='I am aware I will DuckTheSystem', variable=var1, onvalue=1, offvalue=0)
c1.pack()

c2 = tk.Checkbutton(window, text='I swear I wont tell anybody who gave me this tool', variable=var2, onvalue=1, offvalue=0)
c2.pack()

#Bottone
button = tk.Button(window, text="Let's DuckTheSystem!", command=start_program)
button.pack(pady=30)

#Gif
#img = ImageTk.PhotoImage(Image.open("dontgiveaduck.gif"),format = 'gif -index %i' %(i)for i in range(frameCnt)])
#panel = tk.Label(window, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")

frameCnt = 12
frames = [ImageTk.PhotoImage(file='dontgiveaduck.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label2.configure(image=frame)
    window.after(100, update, ind)
label2 = tk.Label(window)
label2.pack()
window.after(0, update, 0)


window.mainloop()

##### Apertura del file #####################################################################

file_name = 'file5.txt'

if not os.path.exists(file_name):
    with open(file_name, 'w') as file:
        pass
os.system(f"notepad.exe {file_name}")