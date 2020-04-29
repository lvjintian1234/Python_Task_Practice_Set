import math
a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))
if a+b>c and a+c>b and b+c>a:
    C=a+b+c
    s=C/2
    S=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("该三角形周长为%.2f,面积为%.2f" % (C,S))
else:
    print("无法构成三角形")

