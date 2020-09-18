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
inp = open('output.txt', 'r')
c0 = eval(inp.readline())
c1 = eval(inp.readline())
c4 = eval(inp.readline())
c7 = eval(inp.readline())
c = [c0, c1, c4, c7]
index(a, size)
tr.exitonclick()
