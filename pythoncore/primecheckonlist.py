a = str(input("Enter elements of the list: "))
d = a.split()
e = []
for i in range(len(d)):
    e.append(int(d[i]))
for i in range(len(e)):
    target = e[i]
    c = 0
    b = target
    while b>0:
        if target%b == 0:
            c = c + 1
        b = b - 1
    if c == 2:
        print(target, "is prime")
    else:
        print(target, "is not prime")