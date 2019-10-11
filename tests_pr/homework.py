import re
import string
from math import log


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


def arith_progress(numbers):
    if len(numbers) < 2:
        return False
    arith_progress_step = numbers[1] - numbers[0]
    ind = 1
    while ind < len(numbers) - 1:
        if numbers[ind + 1] != numbers[ind] + arith_progress_step:
            return False
        ind += 1
    return True


def number_not_twice(numbers):
    return [element for element in numbers if list(numbers).count(element) == 1]


def missing_number(numbers):
    seq = range(min(numbers), max(numbers))
    return [element for element in seq if element not in set(numbers)]


def count_until_tuple(something):
    result = 0
    for element in something:
        if type(element) == tuple:
            break
        result += 1
    return result


def reversed_text(text):
    return str(text)[::-1]


def hours_minutes(num):
    return f"{num // 60}:{num - num // 60 * 60}"


def first_longest_word(text):
    return max([''.join([ch for ch in words if ch not in string.punctuation])
                for words in text.split()], key=len)


def words_in_backward():
    return ' '.join(list(reversed(input().split())))


def fibonnaci_seq():
    fib1 = fib2 = 1
    result = [fib1, fib2]
    num = int(input("Enter how many Fibonnaci numbers to generate: ")) - 2
    while num > 0:
        fib1, fib2 = fib2, fib1 + fib2
        num -= 1
        result.append(fib2)
    return result


def list_with_even(numbers):
    return [element for element in numbers if element % 2 == 0]


def sum_of_num(num):
    return sum(range(1, num + 1))


def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


def letter_replace(text):
    vowels = "aeiou"
    res = "".join(string.ascii_lowercase[(string.ascii_lowercase.index(letter) + 1) %
                                         len(string.ascii_lowercase)] for letter in text)
    return ''.join(i.upper() if i in vowels else i for i in res)


def sorted_letters(text):
    return ''.join(sorted((letter for letter in text if letter in string.ascii_letters)))


def two_nums(num1, num2):
    if num1 == num2:
        return -1
    else:
        return num1 < num2



