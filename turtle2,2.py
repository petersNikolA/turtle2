import turtle as tr
tr.shape('turtle')
import math as m

def index(a, size):
        tr.right(90)
        for i in range(len(a)):
            for j in range(len(c[a[i]])):
                f = c[a[i]]
                eval(f[j])
            tr.penup()
            tr.forward(size)
            tr.right(90)
            tr.pendown()

a = list(map(int, input().split()))
size = int(input())
c0 = ('tr.forward(2 * size)', 'tr.left(90)', 'tr.forward(size)', 'tr.left(90)',
 'tr.forward(2 * size)', 'tr.left(90)', 'tr.forward(size)',
 'tr.backward(size)', 'tr.right(180)')
c1 = ('tr.penup()', 'tr.forward(size)', 'tr.pendown()', 'tr.left(135)',
 'tr.forward(m.sqrt(2) * size)', 'tr.right(135)', 'tr.forward(2 * size)',
 'tr.backward(2 * size)', 'tr.left(90)')
c4 = ('tr.forward(size)', 'tr.left(90)', 'tr.forward(size)', 'tr.right(90)',
 'tr.forward(size)', 'tr.backward(2 * size)', 'tr.left(90)')
c7 = ('tr.left(90)', 'tr.forward(size)', 'tr.right(135)', 'tr.forward(m.sqrt(2) * size)',
 'tr.left(45)', 'tr.forward(size)', 'tr.penup()', 'tr.backward(2 * size)',
 'tr.left(90)', 'tr.forward(size)')
c = [c0, c1, c4, c7]
index(a, size)
tr.exitonclick()
