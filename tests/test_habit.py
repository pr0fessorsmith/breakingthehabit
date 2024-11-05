import unittest
from datetime import datetime
from src.habit import Habit

# Predefined habit data for testing
daily_habit_full_streak = [
    datetime(2023, 1, 1),
    datetime(2023, 1, 2),
    datetime(2023, 1, 3),
    datetime(2023, 1, 4),
    datetime(2023, 1, 5),
    datetime(2023, 1, 6),
    datetime(2023, 1, 7),
    datetime(2023, 1, 8),
    datetime(2023, 1, 9),
    datetime(2023, 1, 10),
    datetime(2023, 1, 11),
    datetime(2023, 1, 12),
    datetime(2023, 1, 13),
    datetime(2023, 1, 14),
    datetime(2023, 1, 15),
    datetime(2023, 1, 16),
    datetime(2023, 1, 17),
    datetime(2023, 1, 18),
    datetime(2023, 1, 19),
    datetime(2023, 1, 20),
    datetime(2023, 1, 21),
    datetime(2023, 1, 22),
    datetime(2023, 1, 23),
    datetime(2023, 1, 24),
    datetime(2023, 1, 25),
    datetime(2023, 1, 26),
    datetime(2023, 1, 27),
    datetime(2023, 1, 28)
]

daily_habit_missed_days = [
    datetime(2023, 1, 1),
    datetime(2023, 1, 2),
    datetime(2023, 1, 3),
    datetime(2023, 1, 5),
    datetime(2023, 1, 6),
    datetime(2023, 1, 7),
    datetime(2023, 1, 9),
    datetime(2023, 1, 10),
    datetime(2023, 1, 11),
    datetime(2023, 1, 13),
    datetime(2023, 1, 14),
    datetime(2023, 1, 15),
    datetime(2023, 1, 17),
    datetime(2023, 1, 18),
    datetime(2023, 1, 19),
    datetime(2023, 1, 21),
    datetime(2023, 1, 22),
    datetime(2023, 1, 23),
    datetime(2023, 1, 25),
    datetime(2023, 1, 26),
    datetime(2023, 1, 27)
]

weekly_habit_full_streak = [
    datetime(2023, 1, 1),
    datetime(2023, 1, 8),
    datetime(2023, 1, 15),
    datetime(2023, 1, 22),
    datetime(2023, 1, 29)
]

weekly_habit_missed_weeks = [
    datetime(2023, 1, 1),
    datetime(2023, 1, 8),
    datetime(2023, 1, 22),
    datetime(2023, 1, 29)
]

monthly_habit_full_streak = [
    datetime(2023, 1, 1),
    datetime(2023, 2, 1),
    datetime(2023, 3, 1),
    datetime(2023, 4, 1)
]

monthly_habit_missed_months = [
    datetime(2023, 1, 1),
    datetime(2023, 3, 1),
    datetime(2023, 4, 1)
]

class TestHabit(unittest.TestCase):
    def test_daily_streak_full(self):
        habit = Habit(name="Exercise", frequency="daily")
        habit.completion_dates = daily_habit_full_streak
        self.assertEqual(habit.get_longest_streak(), 28)

    def test_daily_streak_missed_days(self):
        habit = Habit(name="Exercise", frequency="daily")
        habit.completion_dates = daily_habit_missed_days
        self.assertEqual(habit.get_longest_streak(), 3)

    def test_weekly_streak_full(self):
        habit = Habit(name="Exercise", frequency="weekly")
        habit.completion_dates = weekly_habit_full_streak
        self.assertEqual(habit.get_longest_streak(), 4)

    def test_weekly_streak_missed_weeks(self):
        habit = Habit(name="Exercise", frequency="weekly")
        habit.completion_dates = weekly_habit_missed_weeks
        self.assertEqual(habit.get_longest_streak(), 2)

    def test_monthly_streak_full(self):
        habit = Habit(name="Exercise", frequency="monthly")
        habit.completion_dates = monthly_habit_full_streak
        self.assertEqual(habit.get_longest_streak(), 4)

    def test_monthly_streak_missed_months(self):
        habit = Habit(name="Exercise", frequency="monthly")
        habit.completion_dates = monthly_habit_missed_months
        self.assertEqual(habit.get_longest_streak(), 2)

    def test_no_streak(self):
        habit = Habit(name="Exercise", frequency="daily")
        habit.completion_dates = []
        self.assertEqual(habit.get_longest_streak(), 0)

    def test_single_completion(self):
        habit = Habit(name="Exercise", frequency="daily")
        habit.completion_dates = [datetime(2023, 1, 1)]
        self.assertEqual(habit.get_longest_streak(), 1)

    def test_to_dict(self):
        habit = Habit(name="Exercise", frequency="daily")
        habit.complete_task()
        habit_dict = habit.to_dict()
        self.assertEqual(habit_dict['name'], "Exercise")
        self.assertEqual(habit_dict['frequency'], "daily")
        self.assertIn('creation_date', habit_dict)
        self.assertIn('completion_dates', habit_dict)

    def test_from_dict(self):
        habit_dict = {
            'name': "Exercise",
            'frequency': "daily",
            'creation_date': datetime(2023, 1, 1).isoformat(),
            'completion_dates': [datetime(2023, 1, 2).isoformat()]
        }
        habit = Habit.from_dict(habit_dict)
        self.assertEqual(habit.name, "Exercise")
        self.assertEqual(habit.frequency, "daily")
        self.assertEqual(habit.creation_date, datetime(2023, 1, 1))
        self.assertEqual(habit.completion_dates, [datetime(2023, 1, 2)])

if __name__ == '__main__':
    unittest.main()