a=float(input("请输入长度: "))
u=str(input("请输入单位（cm 或者 inch）: "))
if u=="inch":
    A=a*2.54
    print("%.2f英寸等于%.2f厘米" % (a,A))
elif u=="cm":
    A=a/2.54
    print("%.2f厘米等于%.2f英寸" % (a,A))
else:
    print("请输入正确的单位")



