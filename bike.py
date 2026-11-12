def get_bike_price(bike_type:str)->int:
    prices ={
        "regular":2,
        "electric":5
    }
    return prices.get(bike_type,2)

class Bike:
    def __init__(self, bike_type:str, number:int, battery:int=100):
        self.bike_type = bike_type
        self.number = number
        self.price = get_bike_price(self.bike_type)
        self.status = "available"
        self.battery = battery if self.bike_type = "electric" else 100
    def change_status(self, new_status:str):
        self.status = new_status
        return self.status
