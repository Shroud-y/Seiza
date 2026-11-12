from station import Station
from bike import Bike
from client import Client
from admin import Administrator

def main():
    Admin = Administrator()

    station_a = Station()
    station_b = Station()

    bike_1 = Bike('regular', 1)
    bike_2 = Bike('electric', 2)
    bike_3 = Bike('electric', 3)
    bike_4 = Bike('regular', 4)

    station_a.leave_bike(bike_1)
    station_b.leave_bike(bike_2)
    station_b.leave_bike(bike_4)
    station_a.leave_bike(bike_3)

    Anna = Client('Anna', 150)
    Ivan = Client('Ivan', 250)

    Anna.get_bike(1, 'regular')
    Anna.return_bike(1)

    Anna.get_bike(2, 'electric')
    Anna.return_bike(1)

    Ivan.get_bike(4, 'regular')
    Ivan.return_bike(1)






