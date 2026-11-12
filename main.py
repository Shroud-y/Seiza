import station.py, bike.py, Client.py

def main():
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



