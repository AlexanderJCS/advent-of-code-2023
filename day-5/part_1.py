

class NumberMap:
    def __init__(self, dst_range_start: int, src_range_start: int, length: int):
        self.dst_range_start = dst_range_start
        self.src_range_start = src_range_start
        self.diff = self.dst_range_start - self.src_range_start
        self.length = length

    def in_range(self, num: int) -> bool:
        """
        :param num: The number to check if it is in the NumberMap range
        :return: If it is in the range
        """

        return self.src_range_start <= num <= self.src_range_start + self.length

    def convert(self, num: int) -> int | None:
        """
        :param num: The number to map
        :return: The mapped number, or None if it is not within the map range
        """

        if not self.in_range(num):
            return None

        return num + self.diff

    def __repr__(self):
        return f"NumberMap({self.dst_range_start} {self.src_range_start} {self.length})"


def parse_seeds(line: str):
    line = line.strip("seeds: ")

    return [int(num) for num in line.split()]


def parse_maps(lines: list[str]) -> list[list[NumberMap]]:
    """
    :param lines: The lines from the input file. Do not include the "seeds" line.
    :return: A 2D array of NumberMaps. The second dimension in the array is for each step, while the first dimension is
             to represent a list of steps that the numbers must go through.
    """

    maps: list[list[NumberMap]] = []

    for line in lines:
        if "map" in line:
            maps.append([])
            continue

        try:
            dst_range_start, src_range_start, length = line.split()

        except ValueError:  # line could not be parsed
            continue

        maps[-1].append(
            NumberMap(
                int(dst_range_start),
                int(src_range_start),
                int(length)
            )
        )

    return maps


def run_step(numbers: list[int], step: list[NumberMap]) -> None:
    """
    Mutates the numbers list according to the number maps in the step variable.
    :param numbers: A list of integers that will be mutated
    :param step: The steps, a list of NumberMaps
    """

    for i, number in enumerate(numbers):
        for number_map in step:
            mapped = number_map.convert(number)

            if mapped is None:
                continue

            numbers[i] = mapped
            break


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    numbers = parse_seeds(lines[0])

    for step in parse_maps(lines[1:]):
        run_step(numbers, step)

    print(min(numbers))


if __name__ == "__main__":
    main()
