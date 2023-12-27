string = "Looping"
for item in string:
    print(item)

favorites = ["Creme Brulee", "Apple Pie", "Churros", "Tiramisù", "Chocolate Cake"]

for i in range(10):
    print("Looping .. ", i)

for item in favorites:
    print("I like this dessert " + item)


count = 0
while (count < len(favorites)):
    print("I like this dessert " + favorites[count])
    count += 1