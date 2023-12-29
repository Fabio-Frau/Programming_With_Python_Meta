menu = ["espresso", "mocha", "latte", "capuccino", "cortado", "americano"]

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee
    

map_coffee = map(find_coffee, menu)
print(map_coffee)

for x in map_coffee:
    print(x)


filer_coffee = filter(find_coffee, menu)
print(filer_coffee)

for x in filer_coffee:
    print(x)