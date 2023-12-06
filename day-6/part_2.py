import part_1


def parse_line(line: str) -> int:
    # Remove all whitespace and combine into a single int
    return int("".join(line.split()))


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    lines = [line.strip("Time:").strip("Distance:") for line in lines]

    time = parse_line(lines[0])
    dist = parse_line(lines[1])

    print(len(part_1.find_winning_charge_times(time, dist)))


if __name__ == "__main__":
    main()
