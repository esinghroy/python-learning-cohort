from models.car import Car
class AmericanCar(Car):
    def drive(self):
        print("Zoooooom!")

    def refuel(self):
        print(f"American Car: You are out of credit :(")