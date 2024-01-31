import pgzrun
from random import randint

apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")

def draw():
    screen.clear()
    screen.fill("pink")
    apple.draw()
    orange.draw()
    pineapple.draw()

def place_apple():
    apple.x = randint(50, 400)
    apple.y = randint(50, 400)

def place_orange():
    orange.x = randint(100, 800)
    orange.y = randint(100, 300)
place_orange()

def place_pineapple():
    pineapple.x = randint(90, 600)
    pineapple.y = randint(90, 400)
place_pineapple()
# place_apple()


def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shoot")
        place_apple()
    else:
        print("Missed")
    if orange.collidepoint(pos):
        print("Good shoot")
        place_orange()
    else:
        print("Missed")
    if pineapple.collidepoint(pos):
        print("Good shoot")
        place_pineapple()
    else:
        print("Missed")
pgzrun.go()