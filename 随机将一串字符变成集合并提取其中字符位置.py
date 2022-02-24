z = set("nice to meet you!")            #设置集合
print(z)
a = list(z)             #集合转化为列表
print(a)
for i in range(len(a)):
    if a[i] != 't':
        continue
    print("t在%d处"%(i+1))