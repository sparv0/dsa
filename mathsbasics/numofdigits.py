a = int(input("Enter a number:"))
count = 0
if a == 0 :
    print(1)
else:
    a = abs(a)
    while a != 0:
        a = a//10
        count = count + 1
    print(count)