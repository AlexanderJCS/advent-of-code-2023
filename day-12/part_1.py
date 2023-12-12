import time


def is_valid_line(line: str | list[str], hashtags: list[int]) -> bool:
    hashtags_in_row = []

    hashtag_count = 0
    for element in line + ".":
        if element == "#":
            hashtag_count += 1

        elif hashtag_count != 0:
            hashtags_in_row.append(hashtag_count)
            hashtag_count = 0

            if len(hashtags_in_row) > len(hashtags):
                return False

            if hashtags_in_row[-1] != hashtags[len(hashtags_in_row) - 1]:
                return False

    return len(hashtags_in_row) == len(hashtags)


def gen_combinations(s: str | list[str], current="", index=0):
    if index == len(s):
        yield current

    elif s[index] == "?":
        yield from gen_combinations(s, current + ".", index + 1)
        yield from gen_combinations(s, current + "#", index + 1)

    else:
        yield from gen_combinations(s, current + s[index], index + 1)


def bruteforce(line: list[str], hashtags: list[int]) -> int:
    line = [element for element in line]

    combinations = gen_combinations(line)

    valid_combinations = 0
    for combination in combinations:
        if is_valid_line(combination, hashtags):
            valid_combinations += 1

    return valid_combinations


def has_too_many_in_row(line: list[str], max_hashtags: int) -> bool:
    """
    :return: True if the number of hashtags in a row is greater than the maximum
    """
    if line[-2] == ".":
        pass

    num_in_row = 0
    for element in line:
        if element == "#":
            num_in_row += 1

        elif element != "#":
            num_in_row = 0

        if num_in_row > max_hashtags:
            return True

    return False


def find_num_arrangements(line: list[str], hashtags: list[int]) -> int:
    line = [element for element in line]

    # First find all spaces that must be whitespace to reduce load when bruteforcing
    for i, element in enumerate(line):
        if element != "?":
            continue

        line[i] = "#"

        if has_too_many_in_row(line, max(hashtags)):
            line[i] = "."

        else:
            line[i] = "?"

    # Bruteforce
    return bruteforce(line, hashtags)


def parse_line(line: str) -> tuple[list[str], list[int]]:
    splitted = line.split()

    return list(splitted[0]), list(map(int, splitted[1].split(",")))


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    sum_arrangements = 0

    start_time = time.time()
    for line in lines:
        springs, hashtags = parse_line(line)

        sum_arrangements += find_num_arrangements(springs, hashtags)

    print(time.time() - start_time)
    print(sum_arrangements)


if __name__ == "__main__":
    main()
