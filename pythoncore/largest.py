a = int(input("enter 1st number:"))
b = int(input("enter 2nd number:"))
c = int(input("enter 3rd number:"))
if a>b and a>c :
    print("a is the greatest")
elif b>a and b>c:
    print("b is the greatest")
elif c>a and c>b:
    print("c is the greatest")
else:
    print("Any two number or all three numbers are equal or invalid input")