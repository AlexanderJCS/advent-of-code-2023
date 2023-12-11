import re


class Universe:
    def __init__(self, lines: list[str]):
        self.lines = lines

    def is_rowcol_empty(self, x: int, y: int) -> bool:
        """
        :return: True if the row or column at the specified coordinates is empty
        """

        row_empty = True

        # Check row
        for char in self.lines[y]:
            if char == "#":
                row_empty = False

        # Check col
        col_empty = True
        for line in self.lines:
            if line[x] == "#":
                col_empty = False

        return row_empty or col_empty

    def calc_dist(self, gal_1_coords: tuple, gal_2_coords: tuple, galaxy_expansion_const=2) -> int:
        dist = 0

        if gal_1_coords == (3, 0) and gal_2_coords == (7, 8):
            pass

        min_x, max_x = min(gal_1_coords[0], gal_2_coords[0]), max(gal_1_coords[0], gal_2_coords[0])
        min_y, max_y = min(gal_1_coords[1], gal_2_coords[1]), max(gal_1_coords[1], gal_2_coords[1])

        # Calculate horizontal
        for x in range(min_x, max_x):
            if self.is_rowcol_empty(x, min_y):
                dist += galaxy_expansion_const

            else:
                dist += 1

        # Calculate vertical
        for y in range(min_y, max_y):
            if self.is_rowcol_empty(max_x, y):
                dist += galaxy_expansion_const

            else:
                dist += 1

        return dist

    def get_galaxies(self) -> list[tuple]:
        galaxy_re = re.compile("#")

        galaxy_coords: list[tuple] = []

        for y, line in enumerate(self.lines):
            for match in galaxy_re.finditer(line):
                galaxy_coords.append((match.start(), y))

        return galaxy_coords

    def get_galaxy_pairs_iter(self) -> iter:
        galaxies = self.get_galaxies()

        for i, galaxy_1 in enumerate(galaxies):
            for galaxy_2 in galaxies[i + 1:]:
                yield galaxy_1, galaxy_2


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    universe = Universe(lines)

    print("Calculating distances. This might take a few minutes")

    added_dists = 0
    for galaxy_pair in universe.get_galaxy_pairs_iter():
        added_dists += universe.calc_dist(*galaxy_pair)

    print(added_dists)


if __name__ == "__main__":
    main()
