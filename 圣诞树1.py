import math
import turtle


turtle.screensize(600,800)#画布为800*600像素
turtle.pensize()
turtle.speed(1)#画笔速度1

#提笔，将画笔移至（0,150）
turtle.penup()
turtle.left(180)
turtle.goto(0,150)

#顶端球
turtle.pendown()
turtle.color("red","red")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

#将画笔移至（0,100）便于下一步绘制
turtle.penup()
turtle.goto(0,100)

#第一层树
a = 200 * math.sqrt(3)#第一层树最长边
turtle.pendown()
turtle.color("green","green")
turtle.begin_fill()
turtle.left(150)
turtle.forward(200)#右边边
turtle.right(150)
turtle.forward(a)#最长边
turtle.left(30)
turtle.backward(200)#左边边
turtle.end_fill()

#将画笔移至（0，0）便于下一步绘制
turtle.penup()
turtle.goto(0,0)

#第二层树
turtle.pendown()
turtle.begin_fill()
turtle.goto(230,-120)
turtle.goto(-230,-120)
turtle.goto(0,0)
turtle.end_fill()

#将画笔移至（0,-120）便于下一步绘制
turtle.penup()
turtle.goto(0,-120)

#第三层树
turtle.pendown()
turtle.begin_fill()
turtle.goto(280,-270)
turtle.goto(-280,-270)
turtle.goto(0,-120)
turtle.end_fill()

#将画笔移至（-80,-270）便于下一步绘制
turtle.penup()
turtle.goto(-80,-270)

#树干
turtle.pendown()
turtle.color("saddlebrown","saddlebrown")
turtle.begin_fill()
turtle.goto(-80,-400)
turtle.goto(80,-400)
turtle.goto(80,-270)
turtle.end_fill()

turtle.hideturtle()

turtle.done()
turtle.mianloop()
