import time


for x in range(10):
    print(x)
    for y in range(10):
        print(y)

print("---------------------")
list1 = [1,2,3,4,5,6,7,8,9]
list2 = [1,2,3,4,5,6,7,8,9]

count = 0
for x in list1:
    count += 1

print(count)
print("---------------------")

for x in list1:
    count += 1
    for y in list2:
        count += 1

print(count)
print("---------------------")

for x in list1:
    for y in list2:
        print(y, end = " ")
    print()
print("---------------------")

for i in range(10):
    for j in range(10):
        print(0, end = " ")
    print()
print("---------------------")


start_time = time.time()

for i in range(10):
    for j in range(10):
        print(0, end = " ")
    print()

print(round((time.time() - start_time),2))

print("---------------------")


start_time = time.time()

for i in range(1000):
    for j in range(1000):
        print(0, end = " ")
    print()

print(round((time.time() - start_time),2))