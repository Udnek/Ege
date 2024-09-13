import turtle as t
t.down()
t.speed(1000000000)

k = 20

t.right(45)
for _ in range(7):
    t.forward(5 * k)
    t.right(45)
    t.forward(10 * k)
    t.right(135)

t.up()
for x in range(0, 10):
    for y in range(-15, 1):
        t.goto(x * k, y * k)
        t.dot(9)

t.done()