from abc import ABC, abstractmethod

class PizzaError(Exception):
    pass

class Pizza:
    def __init__(self, toppings = []):
        for top in toppings:
            if not isinstance(top, Topping):
                raise PizzaError("Not a topping:" + top.__class__.__name__)
        self.toppings = toppings

    def price(self):
        return 100 + sum([top.price() for top in self.toppings])

    def __str__(self):
        return self.__class__.__name__ + " : " + str(self.price())

class Topping(ABC):
    @abstractmethod
    def price(self):
        pass
        
class Cheeze(Topping):
    pass

class Corn(Topping):
    def price(self):
        return 10

class Mushroom(Topping):
    def price(self):
        return 100
        

class LcdTv:
    def price(self):
        return 1000000
        
p1 = Pizza()
print(p1)
p2 = Pizza([Cheeze(), Corn()])
print(p2)
p3 = Pizza([Cheeze(), Cheeze(), Corn()])
print(p3)
p3 = Pizza([LcdTv(), Cheeze(), Cheeze(), Corn()])
print(p3)
