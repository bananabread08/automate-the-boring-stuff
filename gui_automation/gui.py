import pyautogui as pag

width, height = pag.size()

print(pag.position())

# move cursor to position
# (x, y, duration)
pag.moveTo(10, 10)

# move relative to current postion
# (x-offset, y-offset)
pag.moveRel(200, 0)

# actions
pag.click(100, 100)
# pag.doubleClick, rightClick, etc.
