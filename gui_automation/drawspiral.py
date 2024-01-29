import pyautogui as pag

pag.doubleClick()
distance = 200

def draw(d):
    while d > 0:
        # going right
        print(d, 0)
        pag.dragRel(d, 0, duration=0.5, button='left')
        d = d - 25

        # going down
        print(0, d)
        pag.dragRel(0, d, duration=0.5, button='left')

        # going left
        print(-d, 0)
        pag.dragRel(-d, 0, duration=0.5, button='left')
        d = d - 25

        # going up
        print(0, -d)
        pag.dragRel(0, -d, duration=0.5, button='left')
    

draw(distance)
