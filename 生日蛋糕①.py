import turtle as t

t.screensize(200,200,"#e1b3ea") #画布为200*200的紫粉色
t.speed(1)                      #画笔速度为1

t.color("#cb8d64","#cb8d64")    #画笔与填充色皆为棕色
t.begin_fill()                  #开始填充蛋糕身体
t.right(90)
t.fd(120)
a = 1
for k in range(60):
    if k < 30:
        a += 0.2
    else:
        a -= 0.2
    t.forward(a)
    t.right(3)
t.setheading(90)
t.forward(132)
t.end_fill()

t.penup()                       #将画笔移至（0,0）
t.goto(0,0)

t.pendown()                     #画出蛋糕上表面
t.color("#ffffff","#ffffff")    #将画笔与填充色设置为白色
t.begin_fill()
b = 1                           #设置初始速度为1
for j in range(2):              #重复两次以画出椭圆
    for k in range(60):         #画出半个椭圆
        if k < 30:              #当k<30，也就是画前一半弧线
            b += 0.2            #让速度越走越快
        else:                   #画后一半弧线
            b -= 0.2            #让速度越走越慢
        t.forward(b)
        t.left(3)
t.end_fill()

t.right(270)                    #将画笔移至蛋糕表面
t.penup()
t.forward(80)

t.speed(10)                     #画笔速度设置为10
t.hideturtle()                  #隐藏画笔形状
t.color("#e01365","#e01365")    #将画笔与填充色设置为红色
t.begin_fill()                  #开始填充蜡烛
t.pendown()
t.right(90)                     #画出蜡烛烛身
t.fd(60)
t.left(90)
t.fd(16)
t.left(90)
t.fd(60)
t.rt(270)
t.fd(16)
t.setheading(90)

t.fd(60)                        #画出蜡烛烛芯
t.left(90)
t.fd(7)
t.right(90)
t.fd(3)
t.left(90)
t.fd(2)
t.left(90)
t.fd(3)
t.end_fill()

t.bk(3)                         #将画笔移至烛芯的正上方中心
t.left(90)
t.fd(1)

t.color("#fbfecf","#fbfecf")    #用荧黄色表示烛火
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.rt(90)
t.fd(63)
info = "丹丹生日快乐！"
t.left(90)
t.bk(80)
t.pencolor("pink")
for e in info:
    t.write(e,font=('宋体',20,'normal'))
    t.fd(25)

t.done()