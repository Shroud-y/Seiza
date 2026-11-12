from bike import get_bike_price
from datetime import datetime

def calc_max_time(balance, cost):
    return balance // cost

class Ride():
    def __init__(self, bike_type, balance):
        self.minute_price = get_bike_price(bike_type)

        self.max_time = calc_max_time(balance, self.minute_price)
        self.start_time = datetime.now()
    
    def end(self):
        finished_time = datetime.now()
        total_minutes = (finished_time - self.start_time).minutes()

        ride_cost = total_minutes * self.minute_price
        return ride_cost

    def exceeded(self):
        current_time = datetime.now()
        current_minutes = (current_time - self.start_time).minutes()

        return current_minutes < self.max_time