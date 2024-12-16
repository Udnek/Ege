import turtle as t
k = 14

t.tracer(0)
for i in range(2):
    t.forward(24*k)
    t.right(90)
    t.forward(10*k)
    t.right(90)
t.forward(3*k)
t.left(90)
t.forward(13*k)
t.right(90)
for i in range(2):
    t.forward(9*k)
    t.right(90)
    t.forward(32*k)
    t.right(90)

t.up()
for x in range(0, 40):
    for y in range(-25, 20):
        t.goto(x * k, y * k)
        t.dot(3)

t.done()