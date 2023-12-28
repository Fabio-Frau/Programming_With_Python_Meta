def sum_of(a,b):
    return a + b


def sum_of_multi(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

def sum_of_kwargs(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum,2)


print(sum_of(4,5))

print(sum_of_multi(4,5,6))

print(sum_of_kwargs(coffee = 2.99, cake = 4.55, juice = 2.99))