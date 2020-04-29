y=int(input("请输入年份： "))
if y%4 ==0 and y%100 != 0:
    print("%d年是闰年" % y)
else:
    print("%d年不是闰年" % y)
