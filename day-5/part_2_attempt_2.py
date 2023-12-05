import part_1


class DoubleNumberMap(part_1.NumberMap):
    """
    A number map that can go forwards and backwards.
    """
    def __init__(self, dst_range_start: int, src_range_start: int, length: int):
        super().__init__(dst_range_start, src_range_start, length)

    def in_output_range(self, num: int) -> bool:
        return self.dst_range_start <= num <= self.dst_range_start + self.length

    def convert_reverse(self, num: int) -> int | None:
        """
        The inverse function of self.convert()

        :param num: The number to reverse map
        :return: The reverse mapped number, or None if it is not within the output range
        """

        if not self.in_output_range(num):
            return None

        return num - self.diff


def parse_seed_ranges(line: str) -> list[range]:
    line = line.strip("seeds: ")

    seed_intervals = line.split()

    return [
        range(int(seed_intervals[i]), int(seed_intervals[i]) + int(seed_intervals[i + 1]) + 1)
        for i in range(0, len(seed_intervals), 2)
    ]


def parse_maps(lines: list[str]) -> list[list[DoubleNumberMap]]:
    maps = part_1.parse_maps(lines)

    double_maps: list[list[DoubleNumberMap]] = []

    for step in maps:
        double_maps.append([])

        for num_map in step:
            double_maps[-1].append(
                DoubleNumberMap(num_map.dst_range_start, num_map.src_range_start, num_map.length)
            )

    return double_maps


def reverse_one_step(num: int, step: list[DoubleNumberMap]) -> int:
    """
    Finds the reverse number map of the number.

    :param num: The number to reverse
    :param step: The number maps in this step
    :return: Either the reverse number or the same number if it cannot be reversed
    """

    for num_map in step:
        converted_reverse = num_map.convert_reverse(num)

        if converted_reverse is not None:
            return converted_reverse

    return num


def find_critical_point(number_map: DoubleNumberMap, step_index_of_map: int, steps: list[list[DoubleNumberMap]]) -> int:
    critical_point: int = number_map.dst_range_start

    for i in range(step_index_of_map, -1, -1):
        critical_point = reverse_one_step(critical_point, steps[i])

    return critical_point


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    seeds: list[range] = parse_seed_ranges(lines[0])
    steps: list[list[DoubleNumberMap]] = parse_maps(lines[1:])

    # Critical points are seed indices that the min must be, found by working backwards
    critical_points: list[int] = [seed.start for seed in seeds]

    for step_index, step in enumerate(steps):
        for num_map in step:
            critical_points.append(
                find_critical_point(num_map, step_index, steps)
            )

    # Remove critical points that are not in the input range
    for i in range(len(critical_points) - 1, -1, -1):
        critical_point = critical_points[i]

        for seed in seeds:
            if critical_point in seed:
                break

        else:  # nobreak
            critical_points.pop(i)

    # Find the output values of the critical points
    outputs = [point for point in critical_points]

    for step in steps:
        part_1.run_step(outputs, step)

    outputs.sort()
    print(outputs[0])


if __name__ == "__main__":
    main()
