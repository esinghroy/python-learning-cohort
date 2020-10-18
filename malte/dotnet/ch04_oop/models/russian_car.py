from models.car import Car
class RussianCar(Car):
    def refuel(self):
        print(f"Russian Car: Go to supermarket and get some {self.engine_type}!")