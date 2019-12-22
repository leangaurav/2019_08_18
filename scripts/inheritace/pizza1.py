class Pizza:
        
    def price(self):
        return 100
        
    def __str__(self):
        return self.__class__.__name__ + " : " + str(self.price())
        
class CheezePizza(Pizza):
    def price(self):
        return 20 + super().price()

class CornPizza(Pizza):
    def price(self):
        return 10 + super().price()
        
        
p1 = Pizza()
print(p1)

p2 = CheezePizza()
print(p2)

p3 = CornPizza()
print(p3)