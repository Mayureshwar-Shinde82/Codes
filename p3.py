Num = int(input("Enter num: 700"))
Num1 = 0
Num2 = 1
if Num == 1:
    print(Num1)
else:
    for i in range(2,Num+1):
        Num3 = Num1 + Num2
        Num1 = Num2
        Num2 = Num3
        print(Num3,end=" ")