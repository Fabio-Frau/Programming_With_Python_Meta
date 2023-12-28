#global scope
my_global = 10

def fn1():
    enclosed_variable =8

    def fn2():
        local_variable = 5
        print("Access the global", my_global)
        print("Access the enclosed", enclosed_variable)

    fn2()


fn1()
#print("Cannot access the local", local_variable)