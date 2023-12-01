import part_1


NUM_STRINGS = (
        [str(i) for i in range(1, 10)]
        + ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
)

WRITTEN_TO_NUM = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def get_num_indices(string: str) -> list[tuple[int, str]]:
    indices: list[tuple[int, str]] = []

    for num_string in NUM_STRINGS:
        try:
            first_index = string.index(num_string)
            last_index = string.rindex(num_string)
        except ValueError:
            continue

        num_string_short = WRITTEN_TO_NUM.get(num_string)
        if num_string_short is None:  # would happen if it's "9" instead of "nine", for example
            num_string_short = num_string

        indices.append((first_index, num_string_short))
        if last_index != first_index:
            indices.append((last_index, num_string_short))

    return indices


def get_first_num(string: str) -> str:
    num_indices = get_num_indices(string)
    num_indices.sort(key=lambda x: x[0])  # sort by index

    return num_indices[0][1]


def get_last_num(string: str) -> str:
    num_indices = get_num_indices(string)
    num_indices.sort(key=lambda x: x[0], reverse=True)  # sort by index reversed

    return num_indices[0][1]


def get_calibration_value(string) -> int:
    calibration_value = f"{get_first_num(string)}{get_last_num(string)}"

    return int(calibration_value)


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    calib_value_sum = 0
    for line in lines:
        calib_value_sum += get_calibration_value(line)

    print(calib_value_sum)


if __name__ == "__main__":
    main()
