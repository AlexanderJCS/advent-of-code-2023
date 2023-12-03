from dataclasses import dataclass


@dataclass
class PartNumber:
    number: int
    x_index: int
    y_index: int
    width: int


def find_part_numbers(board: list[str]) -> list[PartNumber]:
    part_numbers: list[PartNumber] = []

    for row_i, row in enumerate(board):
        current_number = ""
        x_coord = 0
        y_coord = 0

        for col_i, char in enumerate(row):
            if char.isdigit() and len(current_number) == 0:
                x_coord = col_i
                y_coord = row_i

            if char.isdigit():
                current_number += char

            if not char.isdigit() and len(current_number) > 0:
                part_numbers.append(PartNumber(int(current_number), x_coord, y_coord, len(current_number)))
                current_number = ""

            # If you got to the end of the line
            if col_i == len(row) - 1 and len(current_number) > 0:
                part_numbers.append(PartNumber(int(current_number), x_coord, y_coord, len(current_number)))
                current_number = ""

    return part_numbers


def check_for_symbol(board: list[str], x: int, y: int, width: int, height: int) -> bool:
    for row in range(y, y + height):
        if row < 0:
            continue

        for col in range(x, x + width):
            if col < 0:
                continue

            try:
                char = board[row][col]
            except IndexError:
                continue

            if not char.isdigit() and char != ".":
                return True

    return False


def is_adjacent_to_symbol(board: list[str], part_number: PartNumber):
    top_left_x = part_number.x_index - 1
    top_left_y = part_number.y_index - 1

    width = part_number.width + 2
    height = 3

    return check_for_symbol(board, top_left_x, top_left_y, width, height)


def main():
    with open("input.txt") as f:
        board = f.read().splitlines()

    part_numbers = find_part_numbers(board)

    adjacent_sum = 0
    for part_number in part_numbers:
        print(part_number.number, is_adjacent_to_symbol(board, part_number))

        if is_adjacent_to_symbol(board, part_number):
            adjacent_sum += part_number.number

    print(adjacent_sum)


if __name__ == "__main__":
    main()
