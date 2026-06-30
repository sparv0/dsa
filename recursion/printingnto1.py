def print_number(n):
    if n == 0:
        return
    print_number(n-1)
    print(n , end = " ")

a = int(input("Enter number:"))
print_number(a)