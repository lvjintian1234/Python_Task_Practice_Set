a=int(input("请输入一个正整数: "))
count=0
for x in range(1,a+1):
    if a%x == 0:
        count +=1

if count==2:
    print("%d是一个素数" % a)
else:
    print("%d不是一个素数" % a)
