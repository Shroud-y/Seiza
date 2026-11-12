from ride import Ride
import admin
import station


class Client:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.active_rides = {}

    def __str__(self):
        return (f"Name: {self.name}"
                f"\nBalance: {self.balance}")

    def add_bike(self, bike, bike_type):
        bike_name = bike.name
        self.active_rides[bike_name] = Ride(bike_type, self.balance)
        station.get_bike(bike_type)

    def return_bike(self, bike, station):
        bike_name = bike.name
        profit = self.active_rides[bike_name].end()
        station.leave_bike(bike)
        self.reduce_balance(profit)

    def reduce_balance(self, num):
        self.balance -= num
        admin.get_profit(num)