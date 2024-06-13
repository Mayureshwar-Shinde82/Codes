num = int(input("Enter num :"))
count = 0
if num >0:
    a = num/4
    print(a)
    if num == a**2:
        print(num, "is perfect square")
    else:
        print(num, "not perfect square")