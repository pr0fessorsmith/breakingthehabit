import unittest
from datetime import datetime, timedelta
from src.habit import Habit

class TestHabit(unittest.TestCase):
    def test_daily_streak(self):
        habit = Habit(name="Exercise", frequency="daily")
        habit.completion_dates = [
            datetime(2023, 1, 1),
            datetime(2023, 1, 2),
            datetime(2023, 1, 3),
            datetime(2023, 1, 5)
        ]
        self.assertEqual(habit.get_longest_streak(), 3)

    def test_weekly_streak(self):
        habit = Habit(name="Exercise", frequency="weekly")
        habit.completion_dates = [
            datetime(2023, 1, 1),
            datetime(2023, 1, 8),
            datetime(2023, 1, 15),
            datetime(2023, 1, 29)
        ]
        self.assertEqual(habit.get_longest_streak(), 3)

    def test_monthly_streak(self):
        habit = Habit(name="Exercise", frequency="monthly")
        habit.completion_dates = [
            datetime(2023, 1, 1),
            datetime(2023, 2, 1),
            datetime(2023, 3, 1),
            datetime(2023, 5, 1)
        ]
        self.assertEqual(habit.get_longest_streak(), 3)

    def test_no_streak(self):
        habit = Habit(name="Exercise", frequency="daily")
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