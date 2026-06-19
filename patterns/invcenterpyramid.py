for i in range(5):
    for c in range(i):
        print(" " , end="")
    for j in range(5-i):
        print("*", end =" ")
    print()