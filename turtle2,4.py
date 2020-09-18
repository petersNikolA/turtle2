import turtle as tr
import numpy as np
tr.shape('turtle')
tr.speed(0)

def dvizhenie(y0, a, v):
    tr.penup()
    tr.goto(0, y0)
    tr.pendown()
    x = 0
    y = y0
    dt = 0.05
    vy = v * np.sin(a * np.pi / 180)
    tr.left(a)
    for t in range(10000000):
        x += v * np.cos(a * np.pi / 180) * dt
        vy += -10 * dt
        y +=  vy * dt - 10 * dt ** 2 / 2
        if y <= 0:
            y *= -1
            vy *= -1
        tr.goto(x, y)
    
y0 = int(input('введите начальную координату '))
a = int(input('введите угол '))
v = int(input('введите начальную скорость '))
dvizhenie(y0, a, v)
tr.exitonclick()