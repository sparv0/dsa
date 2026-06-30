with open("test.txt", "w") as file:
    file.write("name")
with open("test.txt" , "r") as file:
    a = file.read()
    print(a)