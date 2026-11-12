


class Administrator:
    def __init__(self):
        self.profit = 0

    def get_profit(self, profit):
        self.profit += profit

    def bikes_on_stations(self, stations):
        for station in stations:
            pass

admin = Administrator()

admin.get_profit(25)

print(admin.profit)