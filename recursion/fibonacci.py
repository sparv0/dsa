def fibonacci(s):
    if s <=1:
        return s
    else:
        return fibonacci(s-1) + fibonacci(s-2)
            
n = int(input("Enter N:"))
for i in range(n):
    print(fibonacci(i))