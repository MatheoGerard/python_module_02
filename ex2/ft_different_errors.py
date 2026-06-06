def garden_operations(operation_number) -> None:
    print(f"Testing operation {operation_number}...")
    word: str = "abc"
    file_to_open: str = "/non/existent/file"
    nb: int = 42
    try:
        if operation_number == 0:
            int(word)
        elif operation_number == 1:
            x: float = 1 / 0
            print(x)
        elif operation_number == 2:
            open(file_to_open)
        elif operation_number == 3:
            y: int = word + nb
            print(y)
        else:
            print("Operation completed successfully")
            return
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")


def test_error_types() -> None:
    garden_operations(0)
    garden_operations(1)
    garden_operations(2)
    garden_operations(3)
    garden_operations(4)
    print()


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("All tests completed - program didn't crash!")
