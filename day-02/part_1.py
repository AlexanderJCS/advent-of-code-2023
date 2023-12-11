from dataclasses import dataclass


@dataclass
class CubeDrawing:
    red_cubes: int
    green_cubes: int
    blue_cubes: int

    def can_fit_with_cubes(self, red_cubes, green_cubes, blue_cubes) -> bool:
        return self.red_cubes <= red_cubes and self.green_cubes <= green_cubes and self.blue_cubes <= blue_cubes


class Game:
    def __init__(self, game_id: int, drawings: list[CubeDrawing]):
        self.game_id = game_id
        self.drawings = drawings

    def can_fit_with_cubes(self, red_cubes, green_cubes, blue_cubes) -> bool:
        for drawing in self.drawings:
            if drawing.can_fit_with_cubes(red_cubes, green_cubes, blue_cubes) is False:
                return False

        return True

    @staticmethod
    def _parse_drawing(drawing: str):
        colors = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for cube in drawing.split(", "):
            value, color = cube.split(" ")
            colors[color] += int(value)

        return CubeDrawing(colors["red"], colors["green"], colors["blue"])

    @staticmethod
    def parse_game(game_line: str):
        game_id_str, drawings = game_line.split(": ")

        # From the string "Game 4: something else here" get the "4"
        game_id = int(game_id_str.split(" ")[1])

        cube_drawings = []
        for cube_drawing in drawings.split("; "):
            cube_drawings.append(Game._parse_drawing(cube_drawing))

        return Game(game_id, cube_drawings)


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    sum_ids = 0

    for line in lines:
        game = Game.parse_game(line)

        if game.can_fit_with_cubes(12, 13, 14):
            sum_ids += game.game_id

    print(sum_ids)


if __name__ == "__main__":
    main()
