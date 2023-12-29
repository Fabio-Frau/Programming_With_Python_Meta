from abc import ABC, abstractmethod

class SomeAbstractClass(ABC):
    @abstractmethod
    def some_abstract_method(self):
        pass


class Employee(ABC):
    @abstractmethod
    def donate(self):
        pass

class Donation(Employee):
    def donate(self):
        a = input("How much would you line to donate: ")
        return a
    

amounts = []
john = Donation()
j = john.donate()
amounts.append(j)

peter = Donation()
p = peter.donate()
amounts.append(p)

print(amounts)