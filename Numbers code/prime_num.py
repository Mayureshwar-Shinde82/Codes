num = 10

if num <= 1:
    print("Invalid input")
    
for i in range(2,num):
    if num%i == 0:
        print("Not a prime")
        break
    
else:
    print("Prime")
    
    