import re

INPUT_PATH = './23-02-input.txt'


def get_game_id_and_rounds(original: str) -> tuple[int, list]:
    """
    Gets the game ID and every round's color with their quantity, using regex.
    This function is used for both the first and the second part.

    :param original: Game string from the txt file.
    :return: tuple(game_id: int, color_counts: list[tuple(count: int, color: str)])
    """
    game, rounds = original.split(': ')
    game_id = int(re.findall(r'\d+', game)[0])
    color_counts = [(int(count), color) for count, color in re.findall(r'(\d+) (\w+)', rounds)]
    return game_id, color_counts


def get_game_points(txt: str) -> int:
    """
    Get the points for the current game.
    If the game is valid (color count within the limit), the point = game_id.
    This function is used for the first part.

    :param txt: Current game as a string from the file
    :return: Current game's points
    """
    game_id, color_counts = get_game_id_and_rounds(txt)
    color_limits = {'red': 12, 'green': 13, 'blue': 14}
    for count, color in color_counts:
        if not count <= color_limits[color]:
            return 0
    return game_id


def get_power_of_fewest_number_of_cubes(txt: str) -> int:
    """
    Finds the fewest number of cubes of each color that could have been in the bag to make the game possible.
    Calculates the power of these 3 numbers.
    This function is used for the second part.

    :param txt: Current game as a string from the file
    :return: Power of the fewest number of cubes
    """
    _, color_counts = get_game_id_and_rounds(txt)
    minimum = {'red': 1, 'blue': 1, 'green': 1}
    for count, color in color_counts:
        if minimum[color] < count:
            minimum[color] = count
    return minimum['red'] * minimum['blue'] * minimum['green']


if __name__ == '__main__':
    part1 = 0
    part2 = 0

    with open(file=INPUT_PATH, mode='r') as file:
        for line in file:
            part1 += get_game_points(txt=line)
            part2 += get_power_of_fewest_number_of_cubes(txt=line)

    print(f'[PART 1] Solution: {part1}')
    print(f'[PART 2] Solution: {part2}')
