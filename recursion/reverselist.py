def list_reverse(c):
    if len(c) == 0 or len(c) == 1:
        return c
    else:
        reversed_rest = list_reverse(c[1:])
        reversed_rest.append(c[0])
        return reversed_rest
a = str(input("Enter list elements:"))
b = a.split()
c = []
for i in range(len(b)):
    c.append(int(b[i]))
print(list_reverse(c))