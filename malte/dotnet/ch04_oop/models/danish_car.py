from models.car import Car
class DanishCar(Car):
    def drive(self):
        print("Det køre bare!!!!")

    def refuel(self):
        print(f"Danish Car: Skal du ha' en pølse med?")