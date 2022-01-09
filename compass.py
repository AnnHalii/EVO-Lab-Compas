DIRECTIONS = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']


class BaseError(Exception):
    pass


class InvalidDirection(BaseError):
    pass


class InvalidTypeError(BaseError):
    pass


class InvalidCertainDegreeToTurn(BaseError):
    pass


def _check_facing(facing):
    if facing not in DIRECTIONS:
        raise InvalidDirection(f"Value must be one of the 8 directions: {DIRECTIONS}")


def _check_turn(turn):
    if not isinstance(turn, int):
        raise InvalidTypeError(f"Value must be a int, but got {type(turn)}")
    if not turn // 45:
        raise InvalidCertainDegreeToTurn("Value must be a multiple of 45")
    if not -1080 <= turn <= 1080:
        raise InvalidCertainDegreeToTurn("Value must be between -1080 and 1080")


def direction(facing: str, turn: int) -> str:
    _check_facing(facing)
    _check_turn(turn)

    turns = turn // 45
    start_index = DIRECTIONS.index(facing)
    end_index = (start_index + turns) % len(DIRECTIONS)
    return DIRECTIONS[end_index]


if __name__ == '__main__':
    print(direction("N", 90))
