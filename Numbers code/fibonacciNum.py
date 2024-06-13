def Fibonacci_Num(num):
    a = 0
    b = 1
    series = []
    if num < 0:
        return "Incorrect input"
    
    elif num == 0:
        series.append(a)
        return series
        
    
    elif num ==1 :
        series.append(b)
        return series
        
    else:
        series.append(a)
        series.append(b)
        for i in range(2,num):
           c = a + b 
           a = b
           b = c
           series.append(b)
           
            
        return series
    
num = int(input("Enter num: "))
obj = Fibonacci_Num(num)
print(obj)
for i in obj:
    print(i)

# def fibonacci_series(n):
#     series = []
#     a, b = 0, 1
#     for _ in range(n):
#         series.append(a)
#         a, b = b, a + b
#     return series

# # Number of terms to generate
# n_terms = int(input("num :  "))
# fib_series = fibonacci_series(n_terms)
# print(f"The first {n_terms} terms of the Fibonacci series are: {fib_series}")

    
 
    