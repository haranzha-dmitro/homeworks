import pytest

from homework import (
    list_compare,
    count_letter_in_text,
    power_of_three,
    sum_of_digits,
    push_zeros,
    arith_progress,
    number_not_twice,
    missing_number,
    count_until_tuple,
    reversed_text,
    hours_minutes,
    words_in_backward,
    first_longest_word,
    list_with_even,
    fibonnaci_seq,
    sum_of_num,
    factorial,
    two_nums,
    letter_replace,
    sorted_letters
)


def test_list_compare():
    list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    result = [1, 2, 3, 5, 8, 13]
    assert list_compare(list1, list2) == result


def test_count_letter_in_text():
    text = "I am a good developer. I am also a writer"
    letter = "a"
    assert count_letter_in_text(text, letter) == 5


def test_power_of_three_true():
    number1 = 9
    number2 = 81
    assert power_of_three(number1) is True
    assert power_of_three(number2) is True


def test_power_of_three_false():
    number = 8
    assert power_of_three(number) is False


def test_sum_of_digits():
    rezult1 = 7
    rezult2 = 8
    assert sum_of_digits(34) == rezult1
    assert sum_of_digits(89) == rezult2


def test_push_zeros():
    list1 = [0, 2, 3, 4, 6, 7, 10]
    result = [2, 3, 4, 6, 7, 10, 0]
    assert push_zeros(list1) == result


def test_arithmetic_progres():
    testlist = [5, 7, 9, 11]
    assert arith_progress(testlist) == True


def test_number_not_twice():
    testlist = [5, 3, 4, 3, 4]
    result = [5]
    assert number_not_twice(testlist) == result


def test_missing_number():
    testlist = [1, 2, 3, 4, 6, 7, 8]
    result = [5]
    assert missing_number(testlist) == result


def test_count_until_tuple():
    testlist = [1, 2, 3, (1, 2), 3]
    result = 3
    assert count_until_tuple(testlist) == result


def test_reversed_text():
    text = "Hello World and Coders"
    result = "sredoC dna dlroW olleH"
    assert reversed_text(text) == result


def test_hours_minutes():
    num = 13
    result = "0:13"
    assert hours_minutes(num) == result


def test_first_longest_word():
    text = "fun&!! time"
    result = "time"
    assert first_longest_word(text) == result


def test_words_in_backward(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: 'My name is Michele')
    assert words_in_backward() == 'Michele is name My'


def test_fibonnaci_seq(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 4)
    assert fibonnaci_seq() == [1, 1, 2, 3]


def test_list_with_even():
    numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert list_with_even(numbers) == [4, 16, 36, 64, 100]


def test_sum_of_num():
    num = 4
    assert sum_of_num(num) == 10


def test_factorial():
    num = 4
    assert factorial(num) == 24


@pytest.mark.parametrize('test_input, expected',
                         [('edcba', 'abcde'), ('qwerty', 'eqrtwy')])
def test_sorted_letters(test_input, expected):
    assert sorted_letters(test_input) == expected


@pytest.mark.parametrize('test_input, expected',
                         [('abcd', 'bcdE'), ('zabcd', 'AbcdE')])
def test_letter_replace(test_input, expected):
    assert letter_replace(test_input) == expected

@pytest.mark.parametrize('test_input1, test_input2, expected',
                         [(1, 3, True), (3, 1, False), (1, 1, -1)])
def test_two_nums(test_input1, test_input2, expected):
    assert two_nums(test_input1, test_input2) == expected