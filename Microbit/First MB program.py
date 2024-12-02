# Write your code here :-)
from microbit import *

while not button_a.was_pressed():
    display.scroll("I'm bored")
    if button_b.was_pressed():
        display.scroll("That's a little better")
display.scroll("Hit me one more time!")
