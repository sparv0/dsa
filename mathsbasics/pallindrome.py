a = int(input("Enter a number:"))
d = a
b = 0
c = 0
if a == 0 :
    print("the given number is a pallindrome")
else:
    a = abs(a)
    while d != 0:
        b = d%10
        c = c*10 + b
        d = d//10
        
    if c == a :
        print("the given number is a pallindrome")
    else :
        print("The given number is not a pallindrome")