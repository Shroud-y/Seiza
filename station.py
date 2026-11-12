station_id_list = list(range(1, 100))

def get_available_station_id():
    return station_list.pop(0)

class Station():
    def __init__(self):
        self.id = get_available_station_id()
        self.bikes = []
    
    def get_bikes_amount(self):
        return len(self.bikes)
    
    def get_bike(self, requested_type = None):
        for bike in self.bikes:
            if bike.bike_type == requested_type:
                if requested_type == "electric" and bike.battery < 20:
                    continue
                self.bikes.remove(bike)
                return bike
        
        return None
    
    def leave_bike(self, bike):
        self.bikes.append(bike)
    