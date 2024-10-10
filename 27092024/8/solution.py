import turtle as t
t.tracer(0)
k = 20

t.down()
for i in range(6):
    t.forward(10*k)
    t.left(60)


for x in range(-10, 20):
    for y in range(-10, 20):
        t.penup()
        t.setpos(x*k, y*k)
        t.pendown()
        t.dot(5, "red")

t.done()

#268