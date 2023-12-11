import part_1


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    universe = part_1.Universe(lines)

    print("Calculating distances. This might take a few minutes")

    added_dists = 0
    for galaxy_pair in universe.get_galaxy_pairs_iter():
        added_dists += universe.calc_dist(*galaxy_pair, galaxy_expansion_const=1000000)

    print(added_dists)


if __name__ == "__main__":
    main()