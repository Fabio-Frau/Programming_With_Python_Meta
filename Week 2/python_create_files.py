with open("newfile.txt", mode = "w") as file:
    file.write("This is a new file")


with open("newfile2.txt", mode = "w") as file:
    file.writelines(["This is a second text file", "This is another line"])

with open("newfile3.txt", mode = "w") as file:
    file.writelines(["This is a second text file", "\nThis is another line"])

with open("newfile3.txt", mode = "a") as file:
    file.writelines(["\nAppending new line", "\nAppending new line"])

try:
    with open("sample/newfile.txt", "a") as file:
        file.writelines(["\nAppending new line", "\nAppending new line"])
except FileNotFoundError as e:
    print("ERROR", e)