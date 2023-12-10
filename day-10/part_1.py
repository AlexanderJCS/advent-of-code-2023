import networkx as nx


# Empty tuples are special chars that should be treated differently
OFFSETS: dict[str, tuple] = {
    "|": ((0, -1), (0, 1)),
    "-": ((-1, 0), (1, 0)),
    "L": ((0, -1), (1, 0)),
    "J": ((-1, 0), (0, -1)),
    "7": ((-1, 0), (0, 1)),
    "F": ((0, 1), (1, 0)),
    ".": (),
    "S": ()
}


def add_tuples(t1: tuple, t2: tuple):
    return tuple(a + b for a, b, in zip(t1, t2))


def pipe_connects(
        pipe1_chr: str, pipe1_coords: tuple,
        pipe2_coords: tuple, offsets: dict
) -> bool:
    """
    Used by the pipes_connect method.

    :return: True if pipe_1 connects to pipe_2.
    """
    offset_coords = [
        add_tuples(pipe1_coords, offset)
        for offset in offsets[pipe1_chr]
    ]

    return pipe2_coords in offset_coords


def pipes_connect(
        pipe1_chr: str, pipe1_coords: tuple,
        pipe2_chr: str, pipe2_coords: tuple,
        offsets: dict
) -> bool:
    """
    :return: True if two pipes at two different places connect
    """
    if "S" in (pipe1_chr, pipe2_chr):
        return True

    return (pipe_connects(pipe1_chr, pipe1_coords, pipe2_coords, offsets)
            and pipe_connects(pipe2_chr, pipe2_coords, pipe1_coords, offsets))


def generate_offset_coords(char, coords, lines, offsets):
    offset_coords = []

    for offset in offsets[char]:
        coords_offset = add_tuples(coords, offset)

        # Check if x or y is out of range
        if (coords_offset[1] < 0 or coords_offset[1] >= len(lines)
                or coords_offset[0] < 0 or coords_offset[0] >= len(lines[coords_offset[1]])):
            continue

        if not pipes_connect(char, coords, lines[coords_offset[1]][coords_offset[0]], coords_offset, offsets):
            continue

        offset_coords.append(coords_offset)

    return offset_coords


def construct_graph(lines: list[str], offsets: dict) -> nx.Graph:
    graph = nx.Graph()

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char in (".", "S"):
                continue

            coords = (col, row)

            offset_coords = generate_offset_coords(char, coords, lines, offsets)

            graph.add_edges_from(
                [coords, offset_coord]
                for offset_coord in offset_coords
            )

    return graph


def find_farthest_dist(graph: nx.Graph, start_pos: tuple) -> int:
    farthest_dist = 0

    for i, node in enumerate(graph.nodes):
        try:
            dist = nx.shortest_path_length(graph, start_pos, node)

        except nx.exception.NetworkXNoPath:
            continue

        if dist > farthest_dist:
            farthest_dist = dist

    return farthest_dist


def find_start_pos(lines: list[str]) -> tuple | None:
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "S":
                return col, row

    return None


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    print("Calculating graph...")
    graph = construct_graph(lines, OFFSETS)

    print("Finding the start position...")
    start_pos = find_start_pos(lines)

    print("Calculating farthest distance. This may take a few minutes")
    farthest_dist = find_farthest_dist(graph, start_pos)
    print(farthest_dist)


if __name__ == "__main__":
    main()
