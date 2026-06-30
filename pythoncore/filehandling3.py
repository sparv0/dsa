a = str(input("Enter names:"))
b = a.split()
with open("test.txt" , "w") as file:
    for i in range(len(b)):
        file.write(b[i])
        file.write("\n")
with open("test.txt" , "r") as file:
    c = file.read()
    d = c.split("\n")
    e = len(d)
    for i in range(e):
        if d[i] != "":
            print("Name " + str(i+1) + ":" + d[i])