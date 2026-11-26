def input_temperature(temp_str: str) -> int:
    temp_n = int(temp_str)

    if temp_n < 0:
        raise ValueError(f"{temp_n}°C is too cold for plants (min 0°C)")
    if temp_n > 40:
        raise ValueError(f"{temp_n}°C is too hot for plants (max 40°C)")

    return temp_n


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    numbers = ["25", "abc", "100", "-50"]

    for n in numbers:
        print(f"Input data is '{n}'")
        try:
            temp = input_temperature(n)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
