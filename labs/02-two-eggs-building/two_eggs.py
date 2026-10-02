"""Find a breaking floor in a building with two eggs."""


def get_starting_step(floors: int) -> int:
    """Return a step size that covers all floors with decreasing jumps."""
    step = 1
    covered_floors = 1

    while covered_floors < floors:
        step += 1
        covered_floors += step

    return step


def egg_breaks(floor: int, breaking_floor: int) -> bool:
    """Return True when an egg breaks on this floor."""
    return breaking_floor != 0 and floor >= breaking_floor


def find_breaking_floor(floors: int, breaking_floor: int) -> int:
    """Use two eggs to find the first floor where an egg breaks.

    Use 0 as the breaking floor when the egg never breaks.
    """
    step = get_starting_step(floors)
    previous_safe_floor = 0
    current_floor = step
    first_egg_drops = 0

    # Drop the first egg with smaller and smaller jumps.
    while previous_safe_floor < floors:
        current_floor = min(current_floor, floors)
        first_egg_drops += 1
        print(f"First egg: drop from floor {current_floor}.")

        if egg_breaks(current_floor, breaking_floor):
            print("The first egg broke.")
            break

        previous_safe_floor = current_floor
        step -= 1
        current_floor += step
    else:
        print("The egg did not break in this building.")
        return 0

    # Use the second egg to check every floor in the last interval.
    for floor in range(previous_safe_floor + 1, min(current_floor, floors) + 1):
        print(f"Second egg: drop from floor {floor}.")
        if egg_breaks(floor, breaking_floor):
            print(f"The first breaking floor is {floor}.")
            print(f"First-egg drops: {first_egg_drops}")
            return floor

    return 0


if __name__ == "__main__":
    number_of_floors = int(input("Enter the number of floors: "))
    first_breaking_floor = int(
        input("Enter the first breaking floor (0 if the egg never breaks): ")
    )

    if number_of_floors < 1:
        print("The building must have at least one floor.")
    elif first_breaking_floor < 0 or first_breaking_floor > number_of_floors:
        print("The breaking floor must be between 0 and the number of floors.")
    else:
        find_breaking_floor(number_of_floors, first_breaking_floor)
