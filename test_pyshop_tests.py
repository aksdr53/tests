import unittest

from test_pyshop import get_score


TEST_STAMP = [
    {'offset': 0, 'score': {'away': 1, 'home': 0}},
    {'offset': 3, 'score': {'away': 1, 'home': 1}},
    {'offset': 6, 'score': {'away': 2, 'home': 1}},
    {'offset': 8, 'score': {'away': 2, 'home': 2}},
    {'offset': 11, 'score': {'away': 3, 'home': 2}},
    {'offset': 14, 'score': {'away': 3, 'home': 3}},
    {'offset': 17, 'score': {'away': 4, 'home': 3}},
    {'offset': 18, 'score': {'away': 4, 'home': 4}},
    {'offset': 21, 'score': {'away': 5, 'home': 4}},
    {'offset': 23, 'score': {'away': 5, 'home': 5}},
    {'offset': 25, 'score': {'away': 6, 'home': 5}},
    {'offset': 27, 'score': {'away': 6, 'home': 6}},
    {'offset': 30, 'score': {'away': 7, 'home': 6}},
    {'offset': 33, 'score': {'away': 7, 'home': 7}},
    {'offset': 34, 'score': {'away': 8, 'home': 7}},
    {'offset': 35, 'score': {'away': 8, 'home': 8}},
    {'offset': 37, 'score': {'away': 9, 'home': 8}},
    {'offset': 39, 'score': {'away': 9, 'home': 9}},
    {'offset': 41, 'score': {'away': 10, 'home': 9}},
    {'offset': 43, 'score': {'away': 10, 'home': 10}},
    {'offset': 45, 'score': {'away': 11, 'home': 10}},
    {'offset': 48, 'score': {'away': 11, 'home': 11}},
    {'offset': 50, 'score': {'away': 12, 'home': 11}},
    {'offset': 52, 'score': {'away': 12, 'home': 12}},
    {'offset': 53, 'score': {'away': 13, 'home': 12}},
    {'offset': 55, 'score': {'away': 13, 'home': 13}},
]


class TestGetScore(unittest.TestCase):
    """Testing get_score function."""

    def test_offset_in_list(self):
        home, away = get_score(TEST_STAMP, 18)
        self.assertEqual([home, away], [4, 4],
                         'Метод get_score работает неверно')

    def test_offset_in_range(self):
        home, away = get_score(TEST_STAMP, 19)
        self.assertEqual([home, away], [4, 4],
                         'Метод get_score работает неверно,'
                         ' если offset не равен такому в stamp')

    def test_offset_is_bigger(self):
        self.assertRaises(ValueError, get_score, TEST_STAMP, 56)

    def test_offset_bellow_zero(self):
        self.assertRaises(ValueError, get_score, TEST_STAMP, -1)

    def test_offset_is_double(self):
        home, away = get_score(TEST_STAMP, 18.3)
        self.assertEqual([home, away], [4, 4],
                         'Метод get_score работает неверно,'
                         ' если offset не целое')

    def test_stamp_is_empty(self):
        self.assertRaises(ValueError, get_score, [], -1)

    def test_stamp_isnt_list(self):
        self.assertRaises(ValueError, get_score, {}, -1)
