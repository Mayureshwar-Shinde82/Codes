def is_palindrome(num):
    
    if num<0:
        return "Invalid Input"
    
    original_num = num
    rev_num = 0
    
    while num>0:
        a = num%10
        rev_num = rev_num*10 + a
        num = num // 10
    
    return original_num == rev_num

number = int(input("Enter num: ")) 
s = is_palindrome(number)

if  s == True:
    print(number," is palindrome") 
else:
    print(number," not palindrome") 
    