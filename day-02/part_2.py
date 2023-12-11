import part_1


class GamePart2(part_1.Game):
    def __init__(self, game_id: int, drawings: list[part_1.CubeDrawing]):
        super().__init__(game_id, drawings)

    def get_power(self) -> int:
        min_red = 0
        min_green = 0
        min_blue = 0

        for drawing in self.drawings:
            if drawing.red_cubes > min_red:
                min_red = drawing.red_cubes

            if drawing.green_cubes > min_green:
                min_green = drawing.green_cubes

            if drawing.blue_cubes > min_blue:
                min_blue = drawing.blue_cubes

        return min_red * min_green * min_blue

    @staticmethod
    def parse_game(game_line):
        game = part_1.Game.parse_game(game_line)
        return GamePart2(game.game_id, game.drawings)


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    sum_powers = 0

    for line in lines:
        game = GamePart2.parse_game(line)
        sum_powers += game.get_power()

    print(sum_powers)


if __name__ == "__main__":
    main()
