### highest common factor(hcf) Least common multiple(lcm)

a=int(input("请输入一个正整数: "))
b=int(input("请输入另一个正整数: "))
m=max(a,b)
for i in range(1,m+1):
    if a%i ==0 and b%i ==0:
        hcf=i

n=a*b
for i in range(n,m-1,-1):
    if i%a ==0 and i%b ==0:
        lcm=i

print("最大公约数%d, 最小公倍数%d" % (hcf,lcm))
