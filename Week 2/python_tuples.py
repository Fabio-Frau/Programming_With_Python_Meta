my_tuple = (1, "strings", 4.5, True)
print(my_tuple[1])
print(type(my_tuple))

my_tuple1 = 1, "strings", 4.5, True
print(my_tuple1[1])
print(type(my_tuple1))

print(my_tuple.count("strings"))

print(my_tuple.index(4.5))

for x in my_tuple:
    print(x)

