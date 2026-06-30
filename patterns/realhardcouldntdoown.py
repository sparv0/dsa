for i in range(4):
    for j in range(i+1):
        print(j+1, end="")
    for k in range(8 - 2*(i+1)):
        print(" ", end="")
    for j in range(i+1, 0, -1):
        print(j, end="")
    print()