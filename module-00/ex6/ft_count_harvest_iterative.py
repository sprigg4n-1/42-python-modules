def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))

    for n in (1, days + 1):
        print(f"Day {n}")
    print("Harvest time!")
