class Trip:
    _all = []

    def __init__(self, start, destination,Driver):
        self.start = start
        self.destination = destination
        self.driver=Driver
        Trip.all().append(self)
        
    @property
    def start(self):
        return self._start
    @start.setter
    def start(self,value):
        self._start=value
        
    @property
    def destination(self):
        return self._destination
    @destination.setter
    def destination(self,value):
        self._destination=value
        
    @property
    def driver(self):
        return self._driver
    @driver.setter
    def driver(self,value):
        self._driver=value
        
    @classmethod
    def all(cls):
        return cls._all