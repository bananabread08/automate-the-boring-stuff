import pyautogui as pag

pag.doubleClick()

pag.typewrite('Hello World!', interval=0.2)

# with special keys
pag.typewrite(['left', 'shift', 'a'])

# press keys
pag.press('F1')
pag.hotkey('ctrl', 'o')
