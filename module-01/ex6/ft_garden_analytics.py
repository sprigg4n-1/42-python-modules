class Plant:
    class Stats():
        grow_count: int = 0
        age_count: int = 0
        show_count: int = 0

        def add_grow(self) -> None:
            self.grow_count += 1

        def add_age(self) -> None:
            self.age_count += 1

        def add_show(self) -> None:
            self.show_count += 1

        def display(self) -> None:
            print(f"Stats: {self.grow_count} grow, {self.age_count} age,"
                  f" {self.show_count} show")

    def __init__(self, name: str, height: float,
                 days_old: int, growth_rate: float = 0.8) -> None:
        self.name = name
        self._height = 0.0
        self._days_old = 0
        self.set_height(height)
        self.set_age(days_old)
        self.growth_rate = growth_rate
        self._stats = Plant.Stats()

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
        self._stats.add_show()
        print(f"{self.name}: {self._height}cm, {self._days_old} days old")

    def grow(self, growth_amount: float | None = None) -> None:
        self._stats.add_grow()
        if growth_amount is None:
            growth_amount = self.growth_rate
        self._height = round(self._height + self.growth_rate, 1)

    def age(self, days_amount: int = 1) -> None:
        self._stats.add_age()
        self._days_old += days_amount

    def show_stats(self) -> None:
        self._stats.display()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        if days > 365:
            return True
        return False

    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 days_old: int, color: str, growth_rate: float = 0.8) -> None:
        super().__init__(name, height, days_old, color, growth_rate)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds += 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


class TreeStats(Plant.Stats):
    def __init__(self) -> None:
        super().__init__()
        self.count_produce_shade = 0

    def add_produce_shade(self) -> None:
        self.count_produce_shade += 1

    def display(self) -> None:
        super().display()
        print(f" {self.count_produce_shade} shade")


class Tree(Plant):
    _stats: TreeStats

    def __init__(self, name: str, height: float,
                 days_old: int, trunk_diameter: float,
                 growth_rate: float = 0.8) -> None:
        super().__init__(name, height, days_old, growth_rate)
        self.trunk_diameter = round(trunk_diameter, 1)
        self._stats = TreeStats()

    def produce_shade(self) -> None:
        self._stats.add_produce_shade()
        print(f"Tree {self.name} produces a shade of {self._height}cm long"
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

    def grow(self, growth_amount: float | None = None) -> None:
        super().grow(growth_amount)
        self.nutritional_value += 0.5

    def age(self, days_amount: int = 1) -> None:
        super().age(days_amount)
        self.nutritional_value += 0.5


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.show_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    for days in (30, 400):
        print(f"Is {days} days more than a year? -> "
              f"{Plant.is_older_than_year(days)}")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)

    print("=== Anonymous")
    anonymous = Plant.anonymous_plant()
    anonymous.show()
    display_plant_stats(anonymous)
