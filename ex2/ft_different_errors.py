def garden_operations(operation_number) -> None:
    print(f"Testing operation {operation_number}...")
    word: str = "bonjour"
    file_to_open: str = "no_file.txt"
    nb: float = 42.0
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
    except ValueError:
        print(
            "Caught ValueError: "
            f"invalid literal for int() with base 10: '{word}'"
        )
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print(
            "Caught FileNotFoundError: "
            f"[Errno 2] No such file or directory: '{file_to_open}'"
        )
    except TypeError:
        print(
            "Caught TypeError: can only "
            f"concatenate str (not '{nb.__class__.__name__}') to str"
        )


def test_error_types():
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
