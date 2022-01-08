DIRECTIONS = ("N", "NE", "E", "SE", "S", "SW", "W", "NW")


def direction(facing, turn):
    if not -1080 <= turn <= 1080:
        raise ValueError("facing should be between 1080 and -1080.")
    if turn % 45 != 0:
        raise ValueError("turn should be multiply of 45.")
    try:
        direction_number = DIRECTIONS.index(facing)
    except ValueError:
        raise ValueError(f"{facing} is not correct direction. This must be one of this list: {DIRECTIONS}")
    res_direction_number = (turn // 45 + direction_number) % 8
    return DIRECTIONS[res_direction_number]
