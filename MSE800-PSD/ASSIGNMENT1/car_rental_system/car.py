
class Car:
    def __init__(self, car_id, make, model, year, mileage, available_now, min_period, max_period, price_per_day):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available_now = available_now
        self.min_period = min_period
        self.max_period = max_period
        self.price_per_day = price_per_day

    def __str__(self):
        return f"carID: {self.car_id}, carBrand: {self.make}, carModel: {self.model}, carYear: {self.year}, Mileage: {self.mileage}, Price/Day: {self.price_per_day}, Available: {self.available_now}"
