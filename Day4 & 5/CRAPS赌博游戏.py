"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注
"""

import random

principal=int(input("请输入您携带的本金： "))
dealer=principal

while principal>0 and dealer >0:
    print("您目前的本金为%d,庄家为%d" % (principal,dealer))
    needs_go_on = False
    while True:
        debut = int(input("请您下注"))
        if 0<debut<=principal and 0<debut<=dealer:
            break
    a=random.randint(1,6)
    b=random.randint(1,6)
    first=a+b
    print("您两枚骰子的点数为%d和%d，总和为%d" % (a,b,first))
    if first==7 or first==11:
        principal += debut
        dealer -= debut
        print("恭喜您获得胜利，您将获得%d,目前本金为%d" % (debut,principal))
    elif first==2 or first ==3 or first ==12:
        principal -=debut
        dealer += debut
        print("庄家获胜，您损失了%d,目前本金为%d" % (debut,principal))
    else:
        print("没有分出胜负，继续摇骰子")
        needs_go_on = True
    while needs_go_on:
        needs_go_on= False
        a=random.randint(1,6)
        b=random.randint(1,6)
        second=a+b
        print("您两枚骰子的点数为%d和%d，总和为%d" % (a,b,second))
        if first == second:
            principal += debut
            dealer -= debut
            print("恭喜您获得胜利，您将获得%d,目前本金为%d" % (debut,principal))
        elif second ==7:
            principal -=debut
            dealer += debut
            print("庄家获胜，您损失了%d,目前本金为%d" % (debut,principal))
        else:
            print("没有分出胜负，继续摇骰子")
            needs_go_on=True

if principal==0:
    print("你破产了，已经被卖到了非洲，请不要赌博")
else:
    print("你已经击败了庄家，但被恼羞成怒的赌场枪杀，请不要赌博")


