import turtle


turtle.screensize(800,600)#画布为800*600像素
turtle.pensize()
turtle.pencolor("pink")#画笔为粉色
turtle.speed(1)#画笔速度1

#将画笔移至（0,75）
turtle.penup()
turtle.left(90)#画笔朝正上
turtle.forward(75)



turtle.pendown()
turtle.fillcolor("pink")
turtle.begin_fill()
turtle.circle(180,180)#画出爱心的左上半部分
turtle.circle(360,180)#画出爱心的下半部分
turtle.circle(180,180)#画出爱心的右上半部分
turtle.end_fill()

#画笔回到原点，以半径50画圆，无关代码，延时
turtle.forward(75)
turtle.circle(50)
turtle.circle(50)
turtle.circle(50)
turtle.circle(50)
turtle.circle(50)
turtle.circle(50)
turtle.circle(50)
turtle.circle(50)
turtle.circle(50)

turtle.mianloop()
turtle.done()