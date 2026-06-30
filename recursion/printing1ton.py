def print_number(n):
    if n == 0:
        return
    print(n , end = " ")
    print_number(n-1)


a = int(input("Enter number:"))
print_number(a)