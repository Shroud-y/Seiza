import station, bike, client, admin

def main():
    admin = admin.Administrator()

    station_a = station.Station()
    station_b = station.Station()

    bike_1 = bike.Bike('regular', 1)
    bike_2 = bike.Bike('electric', 2, 100)
    bike_3 = bike.Bike('electric', 3, 75)
    bike_4 = bike.Bike('regular', 4)

    station_a.leave_bike(bike_1)
    station_b.leave_bike(bike_2)
    station_b.leave_bike(bike_4)
    station_a.leave_bike(bike_3)

    Anna = client.Client('Anna', 150)
    Ivan = client.Client('Ivan', 250)

main()