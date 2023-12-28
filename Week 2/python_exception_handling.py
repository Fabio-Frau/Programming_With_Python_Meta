def divide_by(a, b):
    return a / b

print(divide_by(40, 4))

try:
    print(divide_by(40, 0))
except Exception as e:
    print("Something went wrong", e)
    print(e.__class__)

try:
    print(divide_by(40, 0))
except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")
    print(e.__class__)



try:
    print(divide_by(40, 0))
except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")
    print(e.__class__)
except Exception as e:
    print(e, "something went wrong")

