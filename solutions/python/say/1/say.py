import traceback

DIGITS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
TEENS = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
TENS = [
    "",
    "",  # Unreachable.
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]


def say_two_digit(number):
    if 10 <= number < 20:
        return TEENS[number % 10]
    prefix = TENS[number // 10]
    if number % 10 != 0:
        dash = "-" if number >= 10 else ""
        suffix = f"{dash}{DIGITS[number % 10]}"
    else:
        suffix = "zero" if number == 0 else ""

    return f"{prefix}{suffix}"


def say_three_digit(number):
    if number < 100:
        return say_two_digit(number)
    suffix = f" {say_two_digit(number % 100)}" if number % 100 != 0 else ""
    return f"{DIGITS[number // 100]} hundred{suffix}"


def say_thousand(number):
    if number < 1000:
        return say_three_digit(number)
    suffix = f" {say_three_digit(number % 1000)}" if number % 1000 != 0 else ""
    return f"{say_three_digit(number // 1000)} thousand{suffix}"


def say_million(number):
    suffix = f" {say_thousand(number % 1_000_000)}" if number % 1_000_000 != 0 else ""
    return f"{say_thousand(number // 1_000_000)} million{suffix}"


def say_billion(number):
    if number % 1_000_000_000 != 0:
        suffix = f" {say_million(number % 1_000_000_000)}"
    else:
        suffix = ""

    return f"{say_thousand(number // 1_000_000_000)} billion{suffix}"


def say(number):
    if not 0 <= number < 1_000_000_000_000:
        raise ValueError("input out of range")
    try:
        if number < 100:
            return say_two_digit(number)
        elif number < 1000:
            return say_three_digit(number)
        elif number < 1_000_000:
            return say_thousand(number)
        elif number < 1_000_000_000:
            return say_million(number)
        else:
            return say_billion(number)
    except IndexError as e:
        traceback.print_exception(e)