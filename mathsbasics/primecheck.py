a = int(input("Enter a number:"))
b = a 
c = 0
while b >0:
    if a%b == 0:
        c = c + 1
    b = b -1
if c == 2:
    print("The number is prime")
else:
    print("The number is not prime")