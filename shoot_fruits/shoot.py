import pgzrun
from random import randint

apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 300)
    apple.y = randint(10, 200)

# place_apple()

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shoot")
        place_apple()
    else:
        print("Missed")
pgzrun.go()