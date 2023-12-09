

def get_diffs(oasis_report: list[int]) -> list[list[int]]:
    diffs = [oasis_report]

    while any(diff != 0 for diff in diffs[-1]):
        diffs.append([diffs[-1][i] - diffs[-1][i - 1] for i in range(1, len(diffs[-1]))])

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
