import json
from datetime import datetime, timedelta
from typing import List, Dict

class Habit:
    def __init__(self, name: str, frequency: str):
        self.name = name
        self.frequency = frequency
        self.creation_date = datetime.now()
        self.completion_dates: List[datetime] = []

    def complete_task(self):
        self.completion_dates.append(datetime.now())

    def get_longest_streak(self) -> int:
        if not self.completion_dates:
            return 0

        sorted_dates = sorted(self.completion_dates)
        longest_streak = 1
        current_streak = 1

        for i in range(1, len(sorted_dates)):
            if self._is_within_frequency(sorted_dates[i - 1], sorted_dates[i]):
                current_streak += 1
                longest_streak = max(longest_streak, current_streak)
            else:
                current_streak = 1

        return longest_streak

    def _is_within_frequency(self, date1: datetime, date2: datetime) -> bool:
        if self.frequency == 'daily':
            return date2 - date1 <= timedelta(days=1)
        elif self.frequency == 'weekly':
            return date2 - date1 <= timedelta(weeks=1)
        elif self.frequency == 'monthly':
            return (date2.year == date1.year and date2.month == date1.month + 1) or \
                   (date2.year == date1.year + 1 and date2.month == 1 and date1.month == 12)
        else:
            raise ValueError("Unsupported frequency. Use 'daily', 'weekly', or 'monthly'.")

    def to_dict(self):
        return {
            'name': self.name,
            'frequency': self.frequency,
            'creation_date': self.creation_date.isoformat(),
            'completion_dates': [date.isoformat() for date in self.completion_dates]
        }

    @classmethod
    def from_dict(cls, data):
        habit = cls(name=data['name'], frequency=data['frequency'])
        habit.creation_date = datetime.fromisoformat(data['creation_date'])
        habit.completion_dates = [datetime.fromisoformat(date) for date in data['completion_dates']]
        return habit

    @staticmethod
    def load_all() -> List['Habit']:
        try:
            with open('habits.json', 'r') as file:
                data = json.load(file)
                return [Habit.from_dict(habit_data) for habit_data in data]
        except FileNotFoundError:
            return []

    @staticmethod
    def load(name: str) -> 'Habit':
        habits = Habit.load_all()
        for habit in habits:
            if habit.name == name:
                return habit
        return None

    @staticmethod
    def save_all(habits: List['Habit']) -> None:
        with open('habits.json', 'w') as file:
            json.dump([habit.to_dict() for habit in habits], file, indent=4)
