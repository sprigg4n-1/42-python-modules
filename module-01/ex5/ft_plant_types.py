class Plant:
    def __init__(self, name: str, height: float,
                 days_old: int, growth_rate: float = 0.8) -> None:
        self.name = name
        self._height = 0.0
        self._days_old = 0
        self.set_height(height)
        self.set_age(days_old)
        self.growth_rate = growth_rate

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        self._height = height
        return True

    def get_age(self) -> int:
        return self._days_old

    def set_age(self, days: int) -> bool:
        if days < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        self._days_old = days
        return True

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._days_old} days old")

    def grow(self) -> None:
        self._height = round(self._height + self.growth_rate, 1)

    def age(self) -> None:
        self._days_old += 1


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 days_old: int, color: str, growth_rate: float = 0.8) -> None:
        super().__init__(name, height, days_old, growth_rate)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 days_old: int, trunk_diameter: float,
                 growth_rate: float = 0.8) -> None:
        super().__init__(name, height, days_old, growth_rate)
        self.trunk_diameter = round(trunk_diameter, 1)

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self._height}cm long"
              f" and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 days_old: int, harvest_season: str,
                 growth_rate: float = 0.8) -> None:
        super().__init__(name, height, days_old, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value: float = 0.0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {round(self.nutritional_value)}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "Red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 2.1)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
