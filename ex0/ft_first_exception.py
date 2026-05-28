def input_temperature(temp_str: str) -> int:
    temp_int: int = int(temp_str)
    return temp_int


def test_temperature() -> None:
    temp_str: str = "25"
    print(f"Input data is '{temp_str}'")
    try:
        print(f"Temperature is now {input_temperature(temp_str)}")
    except ValueError:
        print(
            "Caught input_temperature error: "
            f"invalid literal for int() with base 10: '{temp_str}'"
        )
    print()
    temp_str = "abc"
    print(f"Input data is '{temp_str}'")
    try:
        print(f"Temperature is now {input_temperature(temp_str)}")
    except ValueError:
        print(
            "Caught input_temperature error: "
            f"invalid literal for int() with base 10: '{temp_str}'"
        )


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
