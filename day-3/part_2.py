import re


def get_num_from_coord(board: list[str], x: int, y: int) -> int:
    """
    If the x and y value is numerical, it returns the full number that it's connected to

    :param board: The board object
    :param x: The x index of one of the digits in the number
    :param y: The y index of one of the digits in the number
    :return: The full number
    """

    if not board[y][x].isdigit():
        raise ValueError(f"The index supplied does not contain a digit!")

    # Iterate backwards until you're at the first digit
    while x >= 0 and board[y][x].isdigit():
        x -= 1

    x += 1

    # Read the number
    number_str = ""
    while x < len(board[y]) and board[y][x].isdigit():
        number_str += board[y][x]
        x += 1

    return int(number_str)


def get_gear_ratio(board: list[str], x: int, y: int) -> int | None:
    """
    Gets the gear ratio for a specific gear.

    :param board: The board
    :param x: The x-coordinate of the gear
    :param y: The y-coordinate of the gear
    :return: None if the gear ratio cannot be calculated, otherwise the gear ratio
    """

    gear_values: set[int] = set()

    for row_i in range(max(0, y - 1), min(len(board), y + 2)):
        for col_i in range(max(0, x - 1), min(len(board[row_i]), x + 2)):
            if board[row_i][col_i].isdigit() is False:
                continue

            gear_values.add(get_num_from_coord(board, col_i, row_i))

    if len(gear_values) != 2:
        return None

    gear_values_list = list(gear_values)
    return gear_values_list[0] * gear_values_list[1]


def main():
    with open("input.txt") as f:
        board = f.read().splitlines()

    gear_ratio_sum = 0

    for row_i, row in enumerate(board):
        for col_i, char in enumerate(row):
            if char != "*":
                continue

            gear_ratio = get_gear_ratio(board, col_i, row_i)

            if gear_ratio is not None:
                gear_ratio_sum += gear_ratio

    print(gear_ratio_sum)


if __name__ == "__main__":
    main()
