from ride import Ride
from admin import get_profit

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

    def return_bike(self, bike_name):
        profit = self.active_rides[bike_name].end()
        reduce_balance(profit)

    def reduce_balance(self, num):
        self.balance -= num
        get_profit(num)