import pyautogui

pyautogui.click(50, 50)

while True:
    st = "AutoDucker in control! Duck The System!"
    pyautogui.write(st, interval=0.25)
    for i in st:
        pyautogui.press("backspace")

# tkinter
