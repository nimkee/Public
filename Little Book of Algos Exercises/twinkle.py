from time import sleep
from turtle import Turtle
def twinkle():
    print("Twinkle, twinkle little star,")
    sleep(3)
    print("How I wonder what you are")
    sleep(3)

def upabove():
    print("Up above the world so high")
    sleep(3)
    print("Like a diamond in the sky")
    sleep(3)

t = Turtle()

for side in range(4):
    t.forward(100)
    t.right(90)
