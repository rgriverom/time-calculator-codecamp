"""PyTest Module"""
from unittest import main, TestCase

from time_calculator import add_time


class TestTimeCalculator(TestCase):
    """Test class to test the Time Calculator"""
    def test_same_period(self):
        current = add_time("3:30 PM", "2:12")
        expected = "5:42 PM"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_different_period(self):
        current = add_time("11:55 AM", "3:12")
        expected = "3:07 PM"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_next_day(self):
        current = add_time("9:15 PM", "5:30")
        expected = "2:45 AM (next day)"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_period_change_at_twelve(self):
        current = add_time("11:40 AM", "0:25")
        expected = "12:05 PM"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_twenty_four(self):
        current = add_time("2:59 AM", "24:00")
        expected = "2:59 AM (next day)"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_two_days_later(self):
        current = add_time("11:59 PM", "24:05")
        expected = "12:04 AM (2 days later)"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_high_duration(self):
        current = add_time("8:16 PM", "466:02")
        expected = "6:18 AM (20 days later)"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_no_change(self):
        current = add_time("5:01 AM", "0:00")
        expected = "5:01 AM"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_same_period_with_day(self):
        current = add_time("3:30 PM", "2:12", "Monday")
        expected = "5:42 PM, Monday"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_twenty_four_with_day(self):
        current = add_time("2:59 AM", "24:00", "saturDay")
        expected = "2:59 AM, Sunday (next day)"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_two_days_later_with_day(self):
        current = add_time("11:59 PM", "24:05", "Wednesday")
        expected = "12:04 AM, Friday (2 days later)"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_high_duration_with_day(self):
        current = add_time("8:16 PM", "466:02", "tuesday")
        expected = "6:18 AM, Monday (20 days later)"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )


if __name__ == "__main__":
    main()
