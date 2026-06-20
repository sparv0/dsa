a = str(input("Enter your numbers for the list:"))
b = a.split()
even = 0
odd = 0
c = []
for i in range(len(b)):
    c.append(int(b[i]))
for i in range(len(c)):
    if c[i] % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Total even numbers:" , even , "Total odd numbers:" , odd)