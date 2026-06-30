file = open("test.txt", "w")
file.write("hello")
file.close()
file = open("test.txt", "r")  # "r" mode = read
content = file.read()
print(content)
file.close()