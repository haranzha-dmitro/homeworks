from math import (
    log
)


def list_compare(list1, list2):
    return list(set(list1) & set(list2))


def count_letter_in_text(text, letter):
    return str(text).count(letter)


def power_of_three(number):
    if type(number) != int:
        raise ValueError('Not int')
    x = log(abs(number), 3)
    return int(x) == x


def sum_of_digits(number):
    while True:
        digits_count = sum(int(digit) for digit in str(abs(number)))
        number = digits_count
        if digits_count < 10:
            return digits_count


def push_zeros(numbers):
    zeros_list = [x for x in numbers if x == 0]
    non_zeros = [x for x in numbers if x != 0]
    return [*non_zeros, *zeros_list]

def arithmetic_progres(numbers):
    pass