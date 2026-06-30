def print_name(n, name):
    if n == 0:
        return
    print(name, end=" ")
    print_name(n-1, name)

name = str(input("Enter the name:"))
a = int(input("Enter number of times you want the name to repeat:"))
print_name(a, name)