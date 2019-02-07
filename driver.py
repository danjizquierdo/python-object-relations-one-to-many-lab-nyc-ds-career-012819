from trip import Trip
class Driver:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name=value
    def my_trips(self):
        return [trip for trip in Trip.all() if trip.driver==self]

    def my_trip_summaries(self):
        return [f'Went from {trip.start} to {trip.destination}' for trip in self.my_trips()]
