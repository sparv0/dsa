a = str(input("Enter your numbers for the list:"))
b = a.split()
even = 0
odd = 0
c = []
for i in range(len(b)):
    c.append(int(b[i]))
d = c[0]
e = float('-inf')
if len(c) <= 1:
    print("Invalid  no. of elements in the list")
else:    
    for i in range(1 , len(c)):
        if c[i] > d:
            e = d
            d = c[i]
        elif c[i] > e:
            e = c[i]
    print(e)