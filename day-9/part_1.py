

def get_diffs(oasis_report: list[int]) -> list[list[int]]:
    return [oasis_report] + [(last_report := [(last_report if "last_report" in locals() else oasis_report)[i] - (last_report if "last_report" in locals() else oasis_report)[i - 1] for i in range(1, len(last_report if "last_report" in locals() else oasis_report))]) for _ in range(len(oasis_report) - 1)]


def main():
    with open("input.txt") as f:
        predicted_values = sum(
            sum(diff[-1] for diff in get_diffs(list(map(int, line.split()))))
            for line in f.read().splitlines()
        )

    print(predicted_values)


if __name__ == "__main__":
    main()
