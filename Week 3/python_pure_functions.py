global_list = [1,2,3]

#not a pure function
def add_to(item):
    return global_list.append(item)

add_to(4)

print(global_list)

#pure function
def add_to_list(lst, item):
    n1 = lst.copy()
    n1.append(item)
    return n1


new = add_to_list(global_list,5)

print(global_list)
print(new)