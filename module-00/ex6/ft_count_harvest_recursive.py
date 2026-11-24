def ft_rec(n: int, days: int) -> None:
    if n > days:
        return
    print(f"Day {n}")
    ft_rec(n + 1, days)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    ft_rec(1, days)
    print("Harvest time!")
