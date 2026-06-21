a = int(input("Enter a number:"))
d = a 
e = a
b = 0
c = 0
count = 0
if a == 0 :
    print(1)
else:
    d = abs(d)
    e = abs(e)
    a = abs(a)
    while a != 0:
        a = a//10
        count = count + 1
    while d!=0 :
        b = d%10
        c = c + (b**count)
        d = d//10
    if c == e:
        print("The given number is armstrong")
    else:
        print("The given number is not armstrong")