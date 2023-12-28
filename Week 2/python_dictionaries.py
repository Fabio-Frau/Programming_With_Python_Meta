sample_dict = {1: "Coffee", 2: "Tea", 3: "Juice"}
print(sample_dict[1])

sample_dict[2] = "Mint Tea"
print(sample_dict)

del sample_dict[3]
print(sample_dict)

my_d = {1 : "Test", "Name" : "Jim"}
print(type(my_d))

print(my_d[1])
print(my_d["Name"])

my_d[2] = "Test 2"
print(my_d)


my_d[1] = "Not a test"
print(my_d)

del my_d[1]
print(my_d)

for x in my_d:
    print(x)

for key, values in my_d.items():
    print(str(key) + " : " + str(values))