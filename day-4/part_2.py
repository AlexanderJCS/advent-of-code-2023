from dataclasses import dataclass

import part_1


@dataclass
class ScratchOffData:
    scratch_off: part_1.ScratchOff
    matching_nums: int
    card_number: int
    instances: int = 1


class ScratchOffManager:
    def __init__(self, scratch_offs: list[part_1.ScratchOff]):
        self.scratch_off_data: list[ScratchOffData] = [
            ScratchOffData(
                scratch_off=scratch_off,
                matching_nums=len(scratch_off.get_matching_nums()),
                card_number=index + 1
            )

            for index, scratch_off in enumerate(scratch_offs)
        ]

    def process_copies(self, card_data: ScratchOffData) -> None:
        for i in range(card_data.matching_nums):
            target_card = self.scratch_off_data[card_data.card_number + i]
            target_card.instances += 1
            self.process_copies(target_card)

    def process_all_copies(self):
        for card_data in self.scratch_off_data:
            self.process_copies(card_data)

    def total_scratchcard_instances(self) -> int:
        instances = 0

        for card_data in self.scratch_off_data:
            instances += card_data.instances

        return instances


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    scratch_offs = part_1.parse_input(lines)

    manager = ScratchOffManager(scratch_offs)
    manager.process_all_copies()
    print(manager.total_scratchcard_instances())


if __name__ == "__main__":
    main()
