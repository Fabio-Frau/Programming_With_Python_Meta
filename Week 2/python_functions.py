def sum(x, y):
    return x + y

print(sum(2,2))


bill = 175.00
tax_rate = 15
total_tax = (bill * tax_rate) / 100

print("Total tax", total_tax)


def calculate_tax(bill, tax_rate):
    return round(((bill * tax_rate) / 100),2)

print("Total tax", calculate_tax(100,10))