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


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 10.0, 5)
    print("Plant created: ", end="")
    rose.show()

    new_height = 25.0
    new_age = 30

    if rose.set_height(new_height):
        print(f"Height updated: {rose.get_height()}cm")

    if rose.set_age(new_age):
        print(f"Age updated: {rose.get_age()} days")

    new_height = -1
    new_age = -2

    if not rose.set_height(new_height):
        print("Height update rejected")

    if not rose.set_age(new_age):
        print("Age update rejected")

    print("Current state: ", end="")
    rose.show()
