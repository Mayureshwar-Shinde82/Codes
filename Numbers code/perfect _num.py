num = int(input("Enter num: "))


sum = 0   
for i in range(1,num):
    if num%i == 0:
        sum += i

if num<=0:
    print("Not perfect num")
 
elif sum == num:
    print(f"{num}, is Perfect Number")
else:
    print(f"{num}, is not perfect num")