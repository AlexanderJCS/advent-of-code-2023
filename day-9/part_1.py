

def get_diff(ints: list[int]) -> list[int]:
    diffs: list[int] = []

    for i in range(1, len(ints)):
        diffs.append(ints[i] - ints[i - 1])

    return diffs


def get_diffs(oasis_report: list[int]) -> list[list[int]]:
    diffs = [oasis_report]

    while any(diff != 0 for diff in diffs[-1]):
        diffs.append(get_diff(diffs[-1]))

    return diffs


def parse_line(line: str) -> list[int]:
    return list(map(int, line.split()))


def predict_next_value(diffs: list[list[int]]) -> int:
    return sum(diff[-1] for diff in diffs)


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    predicted_values_sum = 0

    for line in lines:
        diffs = get_diffs(parse_line(line))
        predicted_values_sum += predict_next_value(diffs)

    print(predicted_values_sum)


if __name__ == "__main__":
    main()
