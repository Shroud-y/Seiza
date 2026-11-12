


class Administrator:
    def __init__(self):
        self.profit = 0

    def get_profit(self, profit):
        self.profit += profit

    def bikes_on_stations(self, stations):
        bike_amount = {}
        for station in stations:
            bike_amount[station.id] = station.get_bike_amount()
        return bike_amount    