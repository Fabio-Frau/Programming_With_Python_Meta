with open("newfile3.txt", "r") as file:
    print(file.read())

with open("newfile3.txt", "r") as file:
    print(file.read(10))

with open("newfile3.txt", "r") as file:
    print(file.readline())

with open("newfile3.txt", "r") as file:
    print(file.readline(10))


with open("newfile3.txt", "r") as file:
    lines = file.readlines()
    print(len(lines))

    for line in lines:
        print(line)

        