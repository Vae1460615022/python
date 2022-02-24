import turtle as t

t.speed(10)
t.begin_fill()
t.color("red","red")
for i in range(5):
    t.fd(100)
    t.left(36)
    t.fd(100)
    t.rt(108)
t.hideturtle()
t.end_fill()
t.done()