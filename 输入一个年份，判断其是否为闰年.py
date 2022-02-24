Year = int(input("输入以年份为单位的值："))
if  Year % 4 == 0 and Year % 100 != 0 and Year % 400 == 0:
 print("%d为闰年"%(Year))
else:
 print("%d不为闰年"%(Year))