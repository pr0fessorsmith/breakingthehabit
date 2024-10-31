import unittest
from src.user import User
from src.habit import Habit

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User("test_user")
        self.habit1 = Habit("Exercise", "daily")
        self.habit2 = Habit("Read", "weekly")

    def test_add_habit(self):
        self.user.add_habit(self.habit1)
        self.assertIn(self.habit1, self.user.get_habits())

    def test_remove_habit(self):
        self.user.add_habit(self.habit1)
        self.user.remove_habit(self.habit1)
        self.assertNotIn(self.habit1, self.user.get_habits())

    def test_remove_habit_not_found(self):
        self.user.add_habit(self.habit1)
        self.user.remove_habit(self.habit2)  # habit2 was never added
        self.assertIn(self.habit1, self.user.get_habits())

    def test_get_habits(self):
        self.user.add_habit(self.habit1)
        self.user.add_habit(self.habit2)
        habits = self.user.get_habits()
        self.assertEqual(len(habits), 2)
        self.assertIn(self.habit1, habits)
        self.assertIn(self.habit2, habits)

    def test_get_habit_by_name(self):
        self.user.add_habit(self.habit1)
        habit = self.user.get_habit_by_name("Exercise")
        self.assertEqual(habit, self.habit1)

    def test_get_habit_by_name_not_found(self):
        with self.assertRaises(ValueError):
            self.user.get_habit_by_name("Nonexistent Habit")

if __name__ == '__main__':
    unittest.main()