def input_temperature(temp_str: str) -> int:
    temp_int: int = int(temp_str)
    if temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    elif temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    return temp_int


def test_temperature() -> None:
    temp_str: list[str] = ["25", "abc", "100", "-50"]
    for test in temp_str:
        print(f"Input data is '{test}'")
        try:
            print(f"Temperature is now {input_temperature(test)}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
        print()


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
