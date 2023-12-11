

def parse_line_to_list(line: str):
    return list(map(int, line.split()))


def calc_dist(charge_up_time: int, drift_time: int) -> int:
    # Since speed = charge_up_time, we can do speed (mm / s) * drift time (s) = dist (mm)
    return charge_up_time * drift_time


def find_winning_charge_times(max_time: int, dist: int) -> list[int]:
    winning_times = []

    for charge_time in range(max_time + 1):
        if calc_dist(charge_time, max_time - charge_time) > dist:
            winning_times.append(charge_time)

    return winning_times


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    lines = [line.strip("Time:").strip("Distance:") for line in lines]

    times = parse_line_to_list(lines[0])
    dists = parse_line_to_list(lines[1])

    possibilities: list[int] = []

    for time, dist in zip(times, dists):
        possibilities.append(len(find_winning_charge_times(time, dist)))

    multiplied = 1
    for possibility in possibilities:
        multiplied *= possibility

    print(multiplied)


if __name__ == "__main__":
    main()
