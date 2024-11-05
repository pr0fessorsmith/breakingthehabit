import unittest
from datetime import datetime
from src.habit import Habit
from src.user import User
from src.analytics import (
    get_all_habits,
    get_habits_by_period,
    get_longest_streak,
    get_longest_streak_all,
    get_user_longest_streak,
    get_user_longest_streak_all
)

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

weekly_habit_full_streak = [
    datetime(2023, 1, 1),
    datetime(2023, 1, 8),
    datetime(2023, 1, 15),
    datetime(2023, 1, 22),
    datetime(2023, 1, 29)
]

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        self.user = User(username="test_user", email="test_user@example.com")
        self.habit1 = Habit(name="Exercise", frequency="daily")
        self.habit2 = Habit(name="Read", frequency="weekly")
        self.habit3 = Habit(name="Meditate", frequency="monthly")
        self.user.add_habit(self.habit1)
        self.user.add_habit(self.habit2)
        self.user.add_habit(self.habit3)

    def test_get_all_habits(self):
        habits = get_all_habits()
        self.assertIn("Exercise", habits)
        self.assertIn("Read", habits)
        self.assertIn("Meditate", habits)

    def test_get_habits_by_period(self):
        daily_habits = get_habits_by_period("daily")
        self.assertIn("Exercise", daily_habits)
        weekly_habits = get_habits_by_period("weekly")
        self.assertIn("Read", weekly_habits)
        monthly_habits = get_habits_by_period("monthly")
        self.assertIn("Meditate", monthly_habits)

    def test_get_longest_streak(self):
        self.habit1.completion_dates = daily_habit_full_streak
        streak = get_longest_streak("Exercise")
        self.assertEqual(streak, 28)

    def test_get_longest_streak_all(self):
        self.habit1.completion_dates = daily_habit_full_streak
        self.habit2.completion_dates = weekly_habit_full_streak
        longest_streak_habit = get_longest_streak_all()
        self.assertEqual(longest_streak_habit, "Exercise")

    def test_get_user_longest_streak(self):
        self.habit1.completion_dates = daily_habit_full_streak
        streak = get_user_longest_streak(self.user, "Exercise")
        self.assertEqual(streak, 28)

    def test_get_user_longest_streak_all(self):
        self.habit1.completion_dates = daily_habit_full_streak
        self.habit2.completion_dates = weekly_habit_full_streak
        longest_streak_habit = get_user_longest_streak_all(self.user)
        self.assertEqual(longest_streak_habit, "Exercise")

if __name__ == '__main__':
    unittest.main()