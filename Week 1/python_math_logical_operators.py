print(2 + 2)
print(2 - 2)
print(35 / 5)
print( 35 * 5)


a = True
b = True

if a and b:
    print("All True")

b = False

if a and b:
    print("All True second")

if a or b:
    print("At least one is True")

a = False

if a or b:
    print("Both false")

if not(a) or not(b):
    print("Not operator used")

a = True
b = True

if not(a) or not(b):
    print("Not operator used with a and b both True")