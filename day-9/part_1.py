

def get_diffs(oasis_report: list[int]) -> list[list[int]]:
    last_report = oasis_report
    diffs = [oasis_report] + [(last_report := [last_report[i] - last_report[i - 1] for i in range(1, len(last_report))]) for _ in range(len(oasis_report) - 1)]

    return diffs


def main():
    with open("input.txt") as f:
        predicted_values = sum(
            sum(diff[-1] for diff in get_diffs(list(map(int, line.split()))))
            for line in f.read().splitlines()
        )

    print(predicted_values)


if __name__ == "__main__":
    main()
