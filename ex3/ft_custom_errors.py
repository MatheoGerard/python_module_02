class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def check_garden_exist(is_exist: bool):
    if not is_exist:
        raise GardenError("The garden does not exist!")


def plant_state(is_wilting: bool):
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def water_lvl(is_acceptable: bool):
    if not is_acceptable:
        raise WaterError("Not enough water in the tank!")


def test_errors():
    print("Testing PlantError...")
    try:
        plant_state(True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        water_lvl(False)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    try:
        plant_state(True)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        water_lvl(False)
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    test_errors()
