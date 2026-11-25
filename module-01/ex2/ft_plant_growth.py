class Plant:
    name: str
    height: float
    lifespan: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.lifespan} days old")

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.lifespan += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.lifespan = 30
    rose.show()

    init_height = rose.height
    for n in range(1, 8):
        print(f"=== Day {n} ===")
        rose.grow()
        rose.age()
        rose.show()

    print(f"Growth this week: {round(rose.height - init_height, 1)}cm")
