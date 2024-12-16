import turtle as t
k = 20

t.tracer(0)

for i in range(6):
    t.forward(k * 13)
    t.right(120)

t.up()
for x in range(0, 20):
    for y in range(-15, 1):
        t.goto(x * k, y * k)
        t.dot(3)

t.done()