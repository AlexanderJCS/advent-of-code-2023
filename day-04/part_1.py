

class ScratchOff:
    def __init__(self, winning_numbers: list[int], your_numbers: list[int]):
        self.winning_numbers: list[int] = winning_numbers
        self.your_numbers: list[int] = your_numbers

    def get_matching_nums(self) -> list[int]:
        matching_nums: list[int] = []

        for winning_num in self.winning_numbers:
            if winning_num in self.your_numbers:
                matching_nums.append(winning_num)

        return matching_nums

    def get_points(self) -> int:
        return int(2 ** (len(self.get_matching_nums()) - 1))

    @staticmethod
    def parse_scratch_off(scratch_off_str: str):
        scratch_off_str = scratch_off_str.split(": ")[1]  # remove "Card _: " from the string
        winning_nums_str, your_nums_str = scratch_off_str.split(" | ")

        winning_nums = [int(winning_num) for winning_num in winning_nums_str.split()]
        your_nums = [int(your_num) for your_num in your_nums_str.split()]

        return ScratchOff(winning_nums, your_nums)


def parse_input(scratch_off_strs: list[str]) -> list[ScratchOff]:
    scratch_offs: list[ScratchOff] = []

    for scratch_off_str in scratch_off_strs:
        scratch_offs.append(ScratchOff.parse_scratch_off(scratch_off_str))

    return scratch_offs


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    scratch_offs = parse_input(lines)

    total_points = 0
    for scratch_off in scratch_offs:
        total_points += scratch_off.get_points()

    print(total_points)


if __name__ == "__main__":
    main()
