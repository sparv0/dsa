a = int(input("Enter a number:"))
b = 0
c = 0
if a == 0 :
    print(0)
else:
    a = abs(a)
    while a != 0:
        b = a%10
        c = c*10 + b
        a = a//10
    print(c)