import turtle as tr
tr.shape('turtle')
from random import *
tr.speed(0)

def sluchaino():
    while True:
        tr.forward(randint(1, 30))
        a = random()
        if a >= 0.5:
            tr.right(randint(30, 360))
        else:
            tr.left(randint(30, 360))


sluchaino()
tr.exitonclick()       