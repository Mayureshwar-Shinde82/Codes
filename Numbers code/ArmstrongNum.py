user_input = int(input("Enter num: "))
sum = 0
num = user_input
print(num)
while num>0:
    a = num % 10
    sum += a**3
    print(sum)
    num //= 10
    
    
if sum == user_input:
    print(sum," is Armstrong Number") 
else:
    print(num," is not an Armstrong NUmber")
    
 
