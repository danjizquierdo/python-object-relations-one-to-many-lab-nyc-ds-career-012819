from car import Car

class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name=value
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        self._age=value
        
    def find_my_cars(self):
        return [car for car in Car.all() if car.owner==self]
