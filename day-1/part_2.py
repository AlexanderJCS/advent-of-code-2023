LETTERS_TO_NUM = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9")
]


def replace_words_with_num(string: str) -> str:
    for letter, num in LETTERS_TO_NUM:
        string = string.replace(letter, num)

    return string


def get_first_num(string: str) -> str:
    for char in string:
        if char.isdigit():
            return char


def get_last_num(string: str) -> str:
    return get_first_num(string[::-1])


def get_calibration_value(string) -> int:
    calibration_value = f"{get_first_num(string)}{get_last_num(string)}"

    return int(calibration_value)


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    calib_value_sum = 0
    for line in lines:
        line = replace_words_with_num(line)
        calib_value_sum += get_calibration_value(line)

    print(calib_value_sum)


if __name__ == "__main__":
    main()
