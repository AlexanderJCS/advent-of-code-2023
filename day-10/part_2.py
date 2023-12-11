import sys

import part_1

import shapely


def traverse_pipe(lines: list[str], coords, come_from, offsets: dict) -> list[tuple]:
    offset_coords = part_1.generate_offset_coords(lines[coords[1]][coords[0]], coords, lines, offsets)
    offset_coords.remove(come_from)

    if lines[offset_coords[0][1]][offset_coords[0][0]] == "S":
        return []

    return [offset_coords[0]] + traverse_pipe(lines, offset_coords[0], coords, offsets)


def get_main_pipe_points(lines: list[str], start_point: tuple, offsets: dict) -> list[tuple]:
    # The coords argument needs to be hard-coded depending on the input dataset, I'm too lazy to code that
    x_offset = -1
    y_offset = 0

    return [start_point] + traverse_pipe(
        lines,
        (start_point[0] + x_offset, start_point[1] + y_offset),
        start_point,
        offsets
    )


def main():
    sys.setrecursionlimit(1000000)  # big number

    with open("input.txt") as f:
        lines = f.read().splitlines()

    print("Calculating start point")
    start_point = part_1.find_start_pos(lines)

    print("Calculating main pipe points")
    main_pipe_points = get_main_pipe_points(lines, start_point, part_1.OFFSETS)

    print("Calculating polygon lines")
    polygon_lines = [
        shapely.LineString(main_pipe_points),
        shapely.LineString([main_pipe_points[-1], main_pipe_points[0]])
    ]

    print("Creating polygon")
    polygon: shapely.GeometryCollection = shapely.polygonize(polygon_lines)

    print("Finding points inside polygon")
    points_containing = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if polygon.contains(shapely.Point(x, y)):
                points_containing += 1

        print(f"{y / len(lines) * 100:.1f}%")

    print(points_containing)


if __name__ == "__main__":
    main()
