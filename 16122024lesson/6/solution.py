import turtle as t
k = 20
t.tracer(0)
t.down()

def cyc(r, a, b):
    t.up()
    #t.setpos(t.xcor()-a, t.ycor()-b)
    t.down()
    if a == 0:
        if b == 5: ang = -90
        else: ang = 90
    elif a == 5: ang = -180
    else: ang = 0
    t.setheading(ang)
    t.circle(r*k, -180)

for i in range(5):
    cyc(5, 0, 5)
    cyc(5, 5, 0)
    cyc(5, 0, -5)
    cyc(5, -5, 0)

for i in range(-30, 30):
    for j in range(-30, 30):
        t.up()
        t.setpos(i*k, j*k)
        t.down()
        t.dot(2)

t.done()