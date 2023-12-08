import re
from functools import reduce

INPUT_PATH = './23-03-input.txt'
SPECIAL_CHARACTERS = {'#', '$', '@', '&', '-', '+', '/', '*', '=', '%'}


def get_available_directions(input_size: int, row_len: int, row_nm: int, start_index: int, end_index: int) -> tuple:
    """
    Calculates which directions are available from a specific location.
    This function is used for both the first and the second part.
    :param input_size: Number of rows in the input text
    :param row_len: Length of the rows
    :param row_nm: Current row number
    :param start_index: The start index of the character
    :param end_index: The end index of the character
    :return: tuple(left: bool, right: bool, top: bool, bottom: bool)
    """
    return start_index > 0, end_index < row_len - 1, row_nm > 0, row_nm < input_size - 1


def get_sum_of_all_numbers_adjacent_to_a_symbol(txt: list[str]) -> int:
    """
    Finds and sums up all the numbers adjacent to a special symbol.
    This function is used for the first part.

    1. Left and Right:
        ?NUMBER?

    2. Top:
        ????????
         NUMBER

    3. Bottom:
         NUMBER
        ????????

    :param txt: The file as a list containing the rows
    :return: Sum of all numbers adjacent to a symbol
    """
    adjacent_numbers_to_a_symbol = []
    for line_index, current_line in enumerate(txt):
        for match in re.finditer(r'\d+', current_line):
            number = match.group()
            index = match.start()
            number_start, number_end = index, index + len(number) - 1
            number = int(number)
            left, right, top, bottom = get_available_directions(input_size=len(txt), row_len=len(current_line),
                                                                row_nm=line_index, start_index=number_start,
                                                                end_index=number_end)

            # Check left
            if left and current_line[number_start - 1] in SPECIAL_CHARACTERS:
                adjacent_numbers_to_a_symbol.append(number)
                continue
            # Check right
            if right and current_line[number_end + 1] in SPECIAL_CHARACTERS:
                adjacent_numbers_to_a_symbol.append(number)
                continue

            indexes_to_check = list(range(number_start - left, number_end + right + 1))
            for check in indexes_to_check:
                # Check top
                if top and txt[line_index - 1][check] in SPECIAL_CHARACTERS:
                    adjacent_numbers_to_a_symbol.append(number)
                    continue

                # Check bottom
                if bottom and txt[line_index + 1][check] in SPECIAL_CHARACTERS:
                    adjacent_numbers_to_a_symbol.append(number)
                    continue

    return sum(adjacent_numbers_to_a_symbol)


def get_number_from_partial_index(row: str, partial_index: int) -> int:
    """
    Finds the number from a known index.
    This function is used for the second part.

    row = 'onetwothree159fourfive'
    partial_index = 12 (which is a 5)
    found_number = 159

    :param row: Row which contains the number we are looking for
    :param partial_index: Index where we found a digit
    :return: Found whole number
    """
    start_index = partial_index
    while start_index > 0 and row[start_index - 1].isdigit():
        start_index -= 1

    end_index = partial_index
    while end_index < len(row) - 1 and row[end_index + 1].isdigit():
        end_index += 1

    return int(row[start_index:end_index + 1])


def get_sum_of_all_gear_ratios(txt: list[str]) -> int:
    """
    Finds the two numbers that are adjacent to a `*` symbol.
    Multiplies these two numbers (=gear ratio) and then sums all of them.
    This function is used for the second part.

    1. Left and Right:
        N*N

    2. Top:
         *
        NNN

    3. Bottom:
        NNN
         *

    :param txt: The file as a list containing the rows
    :return: Sum of all gear ratios
    """
    gear_ratios = []
    for line_index, current_line in enumerate(txt):
        for match in re.finditer(r'\*', current_line):
            star_adj_nums = set()
            index = match.start()
            left, right, top, bottom = get_available_directions(input_size=len(txt), row_len=len(current_line),
                                                                row_nm=line_index, start_index=index,
                                                                end_index=index)

            # Check left
            if left and current_line[index - 1].isdigit():
                star_adj_nums.add(get_number_from_partial_index(row=current_line, partial_index=index-1))
            # Check right
            if right and current_line[index + 1].isdigit():
                star_adj_nums.add(get_number_from_partial_index(row=current_line, partial_index=index+1))

            indexes_to_check = list(range(index - left, index + right + 1))
            for check in indexes_to_check:
                # Check top
                if top and txt[line_index - 1][check].isdigit():
                    star_adj_nums.add(get_number_from_partial_index(row=txt[line_index - 1], partial_index=check))

                # Check bottom
                if bottom and txt[line_index + 1][check].isdigit():
                    star_adj_nums.add(get_number_from_partial_index(row=txt[line_index + 1], partial_index=check))

            if len(star_adj_nums) == 2:
                gear_ratios.append(reduce(lambda x, y: x * y, star_adj_nums, 1))

    return sum(gear_ratios)


if __name__ == '__main__':
    with open(file=INPUT_PATH, mode='r') as file:
        rows = [row.strip() for row in file.readlines()]

    part1 = get_sum_of_all_numbers_adjacent_to_a_symbol(txt=rows)
    part2 = get_sum_of_all_gear_ratios(txt=rows)

    print(f'[PART 1] Solution: {part1}')
    print(f'[PART 2] Solution: {part2}')
