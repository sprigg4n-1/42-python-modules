def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file.txt")
    elif operation_number == 3:
        2 + "asdf"
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for n in range(5):
        print(f"Testing operation {n}...")
        try:
            garden_operations(n)
            print("Operation completed successfully")
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as e:
            print(f"Caught {e.__class__.__name__}: {e}")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
