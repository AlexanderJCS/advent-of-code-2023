

def get_diff(ints: list[int]) -> list[int]:
    return [ints[i] - ints[i - 1] for i in range(1, len(ints))]


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
        predicted_values = sum(
            sum(diff[-1] for diff in get_diffs(list(map(int, line.split()))))
            for line in f.read().splitlines()
        )

    print(predicted_values)


if __name__ == "__main__":
    main()
