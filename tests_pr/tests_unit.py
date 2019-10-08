import unittest

from homework import (
    list_compare,
    count_letter_in_text,
    power_of_three,
    sum_of_digits,
    push_zeros,
    arithmetic_progres
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
        self.assertTrue(arithmetic_progres(list1))


if __name__ == "__main__":
    unittest.main()
