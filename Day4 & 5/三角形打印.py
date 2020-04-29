row3=int(input("请再再次输入行数： "))
for i in range(row3):
    for j in range(2*row3-1):
        if j>=row3-1-i and j<=row3-1+i:
            print("*",end="")
        else:
            print(" ",end="")
    print()


