from typing import List
from models.american_car import AmericanCar
from models.car import Car
from models.danish_car import DanishCar
from models.swedish_car import SwedishCar

def main():
    cars = create_cars()
    
    for car in cars:
        print(car)
        car.drive()
        car.refuel()
        print()

def create_cars() -> List[Car]:
    return [
        SwedishCar('Lada', 'potatisvin', 2, 3600),
        SwedishCar('Volvo', 'potatisvin', 6, 16000),
        DanishCar('Elert', 'sun', 0, 847),
        AmericanCar('Tesla', 'sun', 0, 99999),
        
    ]

if __name__ == '__main__':
    main()