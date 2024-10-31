import json
from .habit import Habit  # Adjust the import path as necessary
from typing import List, Dict

class User:
    def __init__(self, username: str, email: str):
        """
        Initialize a new user.

        :param username: The username of the user.
        :param email: The email address of the user.
        """
        self.username = username
        self.email = email
        self.habits: List[Habit] = []

    def add_habit(self, habit: Habit) -> None:
        """
        Add a habit to the user's list of habits.

        :param habit: The habit to add.
        """
        self.habits.append(habit)

    def remove_habit(self, habit: Habit) -> None:
        """
        Remove a habit from the user's list of habits.

        :param habit: The habit to remove.
        """
        if habit in self.habits:
            self.habits.remove(habit)
        else:
            print(f"Habit '{habit.name}' not found in user's habits.")

    def get_habits(self) -> List[Habit]:
        """
        Get the list of habits for the user.

        :return: A list of habits.
        """
        return self.habits

    def get_habit_by_name(self, name: str) -> Habit:
        """
        Get a habit by its name.

        :param name: The name of the habit.
        :return: The habit with the specified name.
        """
        for habit in self.habits:
            if habit.name == name:
                return habit
        raise ValueError(f"Habit with name '{name}' not found.")

    def save_to_json(self, file_path: str) -> None:
        """
        Save the user's data to a JSON file.

        :param file_path: The path to the JSON file.
        """
        data = {
            'username': self.username,
            'email': self.email,
            'habits': [habit.to_dict() for habit in self.habits]
        }
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_from_json(cls, file_path: str) -> 'User':
        """
        Load a user's data from a JSON file.

        :param file_path: The path to the JSON file.
        :return: A User object.
        """
        with open(file_path, 'r') as f:
            data = json.load(f)
        user = cls(username=data['username'], email=data['email'])
        user.habits = [Habit.from_dict(habit_data) for habit_data in data['habits']]
        return user