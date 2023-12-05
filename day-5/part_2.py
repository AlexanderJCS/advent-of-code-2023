"""
Brute-force method for pat 2
!!! This file does not work properly !!!
"""

import multiprocessing as mp
import time

import part_1


def parse_seed_ranges(line: str) -> list[range]:
    line = line.strip("seeds: ")

    seed_intervals = line.split()

    return [
        range(int(seed_intervals[i]), int(seed_intervals[i]) + int(seed_intervals[i + 1]) + 1)
        for i in range(0, len(seed_intervals), 2)
    ]


def get_min_of_range(
        process_num: int, return_dict: dict, seed_range: range, steps: list[list[part_1.NumberMap]]) -> None:
    print(f"{round(time.time())}: Starting seed range {seed_range}")

    min_output: int = -1

    # <spaghetti code>
    for seed in seed_range:
        if seed % 5000000 == 0:
            percent_complete = round((seed - seed_range.start) / (seed_range.stop - seed_range.start) * 100, 1)

            print(f"{round(time.time())} | {process_num}: {percent_complete}%")

        num = seed

        for step in steps:
            for num_range in step:
                converted: int | None = num_range.convert(num)

                if converted is None:
                    continue

                num = converted
                break

        if num < min_output or min_output == -1:
            min_output = num
    # </spaghetii code>

    print(f"{round(time.time())} | {process_num}: DONE with range {seed_range}. Min output: {min_output}")
    return_dict[process_num] = min_output


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    seed_ranges = parse_seed_ranges(lines[0])

    steps = part_1.parse_maps(lines[1:])

    manager = mp.Manager()
    outputs = manager.dict()
    jobs = []

    for i, seed_range in enumerate(seed_ranges):
        process = mp.Process(target=get_min_of_range, args=(i, outputs, seed_range, steps))
        jobs.append(process)
        process.start()

    for process in jobs:
        process.join()

    print(f"{outputs=}")
    print(f"Min outputs: {min(outputs.values())}")


if __name__ == "__main__":
    main()
