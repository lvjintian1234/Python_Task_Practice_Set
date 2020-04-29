for i in range(20):
    for j in range(33):
        l=100-i-j
        if 5*i+3*j+l/3 ==100:
            print('公鸡有%d,母鸡有%d,小鸡有%d' % (i,j,l))
