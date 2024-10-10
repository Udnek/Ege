import turtle as t
t.tracer(0)

k = 40
t.down()
for i in range(12):
    t.right(60)
    t.forward(1*k)
    t.right(60)
    t.forward(1*k)
    t.right(270)

for x in range(-10, 10):
    for y in range(-10, 10):
        t.penup()
        t.setpos(x*k, y*k)
        t.pendown()
        t.dot(3)


t.mainloop()