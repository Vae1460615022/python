import turtle as t

t.speed(10)
t.screensize(800,600)
t.pencolor("red")

t.fillcolor("red")              #画国旗背景
t.begin_fill()
t.fd(200)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(400)
t.rt(90)
t.fd(200)
t.end_fill()

t.goto(-155,-70)                #画大星星
t.begin_fill()
t.color("yellow","yellow")
for i in range(5):
    t.fd(36)
    t.rt(36)
    t.fd(36)
    t.rt(108)
t.end_fill()

t.penup()                       #画第一个小星星
t.goto(-80,-30)
t.pendown()
t.begin_fill()
t.color("yellow","yellow")
for i in range(5):
    t.fd(10)
    t.rt(36)
    t.fd(10)
    t.rt(108)
t.end_fill()

t.penup()                       #画第二个小星星
t.goto(-83,-56)
t.pendown()
t.begin_fill()
t.color("yellow","yellow")
for i in range(5):
    t.fd(10)
    t.rt(36)
    t.fd(10)
    t.rt(108)
t.end_fill()

t.penup()                       #画第三个小星星
t.goto(-87,-82)
t.pendown()
t.begin_fill()
t.color("yellow","yellow")
for i in range(5):
    t.fd(10)
    t.rt(36)
    t.fd(10)
    t.rt(108)
t.end_fill()

t.penup()                       #画第四个小星星
t.goto(-92,-108)
t.pendown()
t.begin_fill()
t.color("yellow","yellow")
for i in range(5):
    t.fd(10)
    t.rt(36)
    t.fd(10)
    t.rt(108)
t.end_fill()

t.hideturtle()
t.done()