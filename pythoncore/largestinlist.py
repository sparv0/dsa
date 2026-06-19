a = str(input("Enter numbers:"))
d = a.split()
b = []
for i in range(len(d)):
    b.append(int(d[i]))
c = b[0]
for i in range(len(b)):
    if c == b[i]:
        c = b[i];
    elif c > b[i]:
        c = c
    else:
        c = b[i];
print(c)