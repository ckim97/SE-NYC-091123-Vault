class NationalPark:
    def __init__(self, name):
        self.name = name
        self.current_visitations = {}
        self.trips = []
        self.visitors = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if (isinstance(name, str)) and (not hasattr(self, "name")):
            self._name = name
        else:
            raise NameError("Name must be a string")
        
    def access_current_trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self.trips.append(new_trip)
        return self.trips
    
    def access_current_visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if new_visitor and isinstance(new_visitor, Visitor) and new_visitor not in self.visitors:
            self.visitors.append(new_visitor)
        if isinstance(new_visitor, Visitor) and new_visitor not in self.current_visitations:
            self.current_visitations[new_visitor] = 1
        elif isinstance(new_visitor, Visitor) and new_visitor in self.current_visitations:
            self.current_visitations[new_visitor] += 1
        return self.visitors

    def calculate_all_trips(self):
        return len(self.trips)
    
    def check_most_frequent_visitor(self):
        from classes.trip import Trip
        max_key = max(self.current_visitations, key=self.current_visitations.get)
        return max_key
        
        


        
        

        
