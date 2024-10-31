import unittest
import os
import json
from src.user import User
from src.habit import Habit

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User("test_user", "test_user@example.com")
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

    def test_save_and_load_user(self):
        self.user.add_habit(self.habit1)
        self.user.add_habit(self.habit2)
        self.user.save_to_json('test_user_data.json')

        loaded_user = User.load_from_json('test_user_data.json')
        self.assertEqual(loaded_user.username, self.user.username)
        self.assertEqual(loaded_user.email, self.user.email)
        self.assertEqual(len(loaded_user.get_habits()), 2)
        os.remove('test_user_data.json')

if __name__ == '__main__':
    unittest.main()