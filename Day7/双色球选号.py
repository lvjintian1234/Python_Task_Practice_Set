import random
red = [x for x in range(1,34)]
blue = [x for x in range(1,17)]

comb_red=[]
for i in range(6):
    r=int(input("请输入您选择的红色球号: "))
    comb_red.append(r)

comb_red.sort()
print(comb_red)

comb_blue=int(input("请输入您选择的蓝色球号： "))

result_red=[]
for i in range(6):
    index = random.randint(1,33)-1
    result_red.append(red[index])
result_red.sort()

index=random.randint(1,16)-1
result_blue=blue[index]

count_red=0
count_blue=0

if comb_blue == result_blue:
    count_blue += 1

for i in range(6):
    if comb_red[i]==result_red[i]:
        count_red +=1

if count_blue ==1:
    if count_red ==6:
        print("一等奖")
    elif count_red==5:
        print("三等奖")
    elif count_red==4:
        print("四等奖")
    elif count_red==3:
        print("五等奖")
    elif count_red==0:
        print("六等奖")
    else:
        print("没有中奖")
elif count_blue==0:
    if count_red ==6:
        print("二等奖")
    elif count_red==5:
        print("四等奖")
    elif count_red==4:
        print("五等奖")
    else:
        print("没有中奖")

