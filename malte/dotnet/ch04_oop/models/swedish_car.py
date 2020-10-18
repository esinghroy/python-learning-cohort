from models.car import Car
class SwedishCar(Car):
    def drive(self):
        print("tøf tøf..")

    def refuel(self):
        print(f"Swedish Car: Go to basement and get some {self.engine_type}!")