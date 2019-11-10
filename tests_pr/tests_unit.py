import unittest

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
    first_longest_word,
    list_with_even,
    sum_of_num,
    factorial
)


class TestsCase(unittest.TestCase):

    def test_list_compare_true(self):
        list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        rezult = [1, 2, 3, 5, 8, 13]
        self.assertListEqual(list_compare(list1, list2), rezult)

    def test_count_letter_in_text(self):
        text = "I am a good developer. I am also a writer"
        letter = "a"
        self.assertEqual(count_letter_in_text(text, letter), 5)

    def test_power_of_three_true(self):
        number1 = 9
        number2 = 81
        self.assertTrue(power_of_three(number1))
        self.assertTrue(power_of_three(number2))

    def test_power_of_three_false(self):
        number = 8
        self.assertFalse(power_of_three(number))

    def test_power_of_three_negative(self):
        number = 3.1
        self.assertRaises(ValueError, power_of_three, number)

    def test_sum_of_digits(self):
        rezult1 = 7
        rezult2 = 8
        self.assertEqual(sum_of_digits(34), rezult1)
        self.assertEqual(sum_of_digits(-89), rezult2)

    def test_push_zeros(self):
        list1 = [0, 2, 3, 4, 6, 7, 10]
        rezult = [2, 3, 4, 6, 7, 10, 0]
        self.assertListEqual(push_zeros(list1), rezult)

    def test_arithmetic_progres(self):
        list1 = [5, 7, 9, 11]
        self.assertTrue(arith_progress(list1))

    def test_number_not_twice(self):
        testlist = [5, 3, 4, 3, 4]
        result = [5]
        self.assertEqual(number_not_twice(testlist), result)

    def test_missing_number(self):
        testlist = [1, 2, 3, 4, 6, 7, 8]
        result = [5]
        self.assertEqual(missing_number(testlist), result)

    def test_count_until_tuple(self):
        testlist = [1, 2, 3, (1, 2), 3]
        result = 3
        self.assertEqual(count_until_tuple(testlist), result)

    def test_reversed_text(self):
        text = "Hello World and Coders"
        result = "sredoC dna dlroW olleH"
        self.assertEqual(reversed_text(text), result)

    def test_hours_minutes(self):
        num = 13
        result = "0:13"
        self.assertEqual(hours_minutes(num), result)

    def test_first_longest_word(self):
        text = "fun&!! time"
        result = "time"
        self.assertEqual(first_longest_word(text), result)

    def test_list_with_even(self):
        numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertListEqual(list_with_even(numbers), [4, 16, 36, 64, 100])

    def test_sum_of_num(self):
        num = 4
        self.assertEqual(sum_of_num(num), 10)

    def test_factorial(self):
        num = 4
        self.assertEqual(factorial(num), 24)


if __name__ == "__main__":
    unittest.main()
