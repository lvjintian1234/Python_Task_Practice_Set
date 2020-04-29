for i in range(1,10001):
    count=0
    for j in range(1,i):
        if i%j==0:
            count+=j
    if count==i:
        print(i)
