import part_1


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    predicted_values_sum = 0

    for line in lines:
        parsed_line = part_1.parse_line(line)
        parsed_line = parsed_line[::-1]  # reverse for part 2

        diffs = part_1.get_diffs(parsed_line)
        predicted_values_sum += part_1.predict_next_value(diffs)

    print(predicted_values_sum)


if __name__ == "__main__":
    main()
