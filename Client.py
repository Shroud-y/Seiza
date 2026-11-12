from ride import Ride

class Client:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.active_rides = {}

    def __str__(self):
        return (f"Name: {self.name}"
                f"\nBalance: {self.balance}")

    def get_bike(self, bike_name, bike_type):
        self.active_rides[bike_name] = Ride(bike_type, self.balance)