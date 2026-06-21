a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
smaller = min(a, b)
while smaller >=1:
    if a%smaller == 0 and b%smaller == 0:
        print("The Gcd is :", smaller)
        break
    else:
        smaller = smaller - 1