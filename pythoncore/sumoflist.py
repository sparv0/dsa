a = str(input("Enter numbers:"))
d = a.split()
c = 0
b = []
for i in range(len(d)):
    b.append(int(d[i]))
    c = sum(b)

print(c)