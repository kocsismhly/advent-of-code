from typing import Optional

INPUT_PATH = '23-01-input.txt'
MAPPING = {'one':   '1',
           'two':   '2',
           'three': '3',
           'four':  '4',
           'five':  '5',
           'six':   '6',
           'seven': '7',
           'eight': '8',
           'nine':  '9'}


def get_the_first_digit(txt: str, part: int) -> Optional[chr]:
    """
    Get the first digit of a string.
    This function is used for both the first and the second part.

    Part 1 only searches for numbers as digits, e.g.: 1, 2, 3, ..., 9.
    Part 2 searches both for numbers as digits and numbers as words, e.g.: `1, 2, ..., 9` and `one, two, ..., nine`.

    :param txt: Input string
    :param part: 1 for the first, 2 for the second part
    :return: First digit in the input as a character, if there is any, else None
    """
    numbers = {txt.find(n): n for n in list(MAPPING.values()) if txt.find(n) != -1}

    if part == 2:
        numbers.update({txt.find(n): n for n in list(MAPPING.keys()) if txt.find(n) != -1})

    if not numbers:
        return None

    first = sorted(numbers.items())[0][1]

    return MAPPING[first] if not first.isdigit() else first


def get_the_last_digit(txt: str, part: int) -> Optional[chr]:
    """
    Get the last digit of a string.
    This function is used for both the first and the second part.

    Part 1 only searches for numbers as digits, e.g.: 1, 2, 3, ..., 9.
    Part 2 searches both for numbers as digits and numbers as words, e.g.: `1, 2, ..., 9` and `one, two, ..., nine`.

    :param txt: Input string
    :param part: 1 for the first, 2 for the second part
    :return: Last digit in the input as a character, if there is any, else None
    """
    numbers = {txt.rfind(n): n for n in list(MAPPING.values()) if txt.rfind(n) != -1}

    if part == 2:
        numbers.update({txt.rfind(n): n for n in list(MAPPING.keys()) if txt.rfind(n) != -1})

    if not numbers:
        return None

    last = sorted(numbers.items())[-1][1]

    return MAPPING[last] if not last.isdigit() else last


def form_two_digit_number(first_digit: chr, last_digit: chr) -> int:
    """
    Form a single two-digit number from two characters.
    This function is used for both the first and the second part.

    :param first_digit: First digit
    :param last_digit: Last digit
    :return: Two-digit number, if everything is right, else 0
    """
    if not first_digit or not last_digit:
        return 0

    combined = first_digit + last_digit
    return int(combined)


if __name__ == '__main__':
    part1 = 0
    part2 = 0

    with open(file=INPUT_PATH, mode='r') as file:
        for line in file:
            # PART 1
            num1 = get_the_first_digit(txt=line, part=1)
            num2 = get_the_last_digit(txt=line, part=1)
            calibration_value = form_two_digit_number(first_digit=num1, last_digit=num2)
            part1 += calibration_value

            # PART 2
            num1 = get_the_first_digit(txt=line, part=2)
            num2 = get_the_last_digit(txt=line, part=2)
            calibration_value = form_two_digit_number(first_digit=num1, last_digit=num2)
            part2 += calibration_value

    print(f'[PART 1] Solution: {part1}')
    print(f'[PART 2] Solution: {part2}')
