class Car:
    _all = []

    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
        Car.all().append(self)
    
    @property
    def make(self):
        return self._make
    @make.setter
    def make(self, value):
        self._make=value
    @property
    def model(self):
        return self._model
    @model.setter
    def model(self,value):
        self._model=value
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self,value):
        self._year=value
    @classmethod
    def all(cls):
        return cls._all
    
    def be_owned(self,Owner):
        self.owner=Owner
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self,value):
        self._owner=value