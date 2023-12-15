class Visitor:    
    def __init__(self, name):
        self.name = name
        self.trips = []
        self.parks = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, name):
        if (isinstance(name, str)) and (1 <= len(name) < 15) and (not hasattr(self, "name")):
            self._name = name
        else:
            raise NameError("Name must be a string from 1 to 15 characters long")

    def access_current_trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self.trips.append(new_trip)
        return self.trips
            
    
    def access_current_parks(self, new_park=None):
        from classes.nationalpark import NationalPark
        if new_park and isinstance(new_park, NationalPark) and new_park not in self.parks:
            self.parks.append(new_park)
        return self.parks