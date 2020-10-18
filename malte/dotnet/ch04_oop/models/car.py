from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self, model_name: str, engine_type: str, cylinders: int, base_price: int) -> None:
        self.model_name: str = model_name
        self.engine_type: str = engine_type
        self.cylinders: int = cylinders
        self.base_price: int = base_price

    def drive(self):
        print(f"Car: The {self.model_name} dosn't start becuase you are out of gas money!")

    @abstractmethod
    def refuel(self):
        raise NotImplementedError("Lazy programmer didn't build a refueling option")

    def __str__(self):
        return f"This {self.model_name} drives on pure {self.engine_type}!! Get yours for only {self.base_price} SEK"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.model_name},{self.engine_type},{self.cylinders},{self.base_price})"
