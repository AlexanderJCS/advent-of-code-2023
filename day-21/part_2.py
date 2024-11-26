from functools import lru_cache


@lru_cache(maxsize=None)
def rock_at(position: tuple[int, int], rocks: frozenset[tuple[int, int]], size: int) -> bool:
    position_modulo = (position[0] % size, position[1] % size)
    return position_modulo in rocks


@lru_cache(maxsize=None)
def expand(position: tuple[int, int], rocks: frozenset[tuple[int, int]], size: int) -> list[tuple[int, int]]:
    return [
        (position[0] + dx, position[1] + dy)
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))
        if not rock_at((position[0] + dx, position[1] + dy), rocks, size)
    ]


def run_iteration(
        positions: set[tuple[int, int]],
        prev_positions: set[tuple[int, int]],
        rocks: frozenset[tuple[int, int]],
        size: int
) -> set[tuple[int, int]]:
    new_positions = prev_positions.copy()
    
    for position in positions - prev_positions:
        new_positions.update(expand(position, rocks, size))
    
    return new_positions


def find_all(data: list[str], char: str) -> set[tuple[int, int]]:
    positions = set()
    
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col == char:
                positions.add((i, j))
        
    return positions


def three_point_formula(one, two, three, n):
    a = (three - (2 * two) + one) / 2
    b = two - one - a
    c = one
    
    return (a * (n**2)) + (b * n) + c


def main():
    print("This is close to working but doesn't work... I give up")
    
    with open("input.txt") as f:
        data = f.read().splitlines()
    
    prev_positions = set()
    current = find_all(data, "S")
    rocks = frozenset(find_all(data, "#"))
    size = len(data)
    
    possible_positions = []
    for _ in range(size // 2 + size * 2 + 1):
        tmp = current
        current = run_iteration(current, prev_positions, rocks, size)
        prev_positions = tmp
        
        possible_positions.append(len(current))
    
    one = possible_positions[size // 2]
    two = possible_positions[size // 2 + size]
    three = possible_positions[size // 2 + size * 2]
    
    print(one, two, three)
    
    print(three_point_formula(one, two, three, 202300))


if __name__ == "__main__":
    main()
