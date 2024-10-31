from datetime import datetime, timedelta
from typing import List, Dict

class Habit:
    def __init__(self, name: str, frequency: str):
        """
        Initialize a new habit.

        :param name: The name of the habit.
        :param frequency: The frequency of the habit (e.g., daily, weekly, monthly).
        """
        self.name = name
        self.frequency = frequency
        self.creation_date = datetime.now()
        self.completion_dates: List[datetime] = []

    def complete_task(self) -> None:
        """
        Mark the habit as completed by adding the current date and time to the completion dates.
        """
        self.completion_dates.append(datetime.now())

    def get_longest_streak(self) -> int:
        """
        Calculate the longest streak of habit completion.

        :return: The longest streak as an integer.
        """
        if not self.completion_dates:
            return 0

        # Sort completion dates
        sorted_dates = sorted(self.completion_dates)
        longest_streak = 1
        current_streak = 1

        # Calculate streaks
        for i in range(1, len(sorted_dates)):
            if self._is_within_frequency(sorted_dates[i - 1], sorted_dates[i]):
                current_streak += 1
                longest_streak = max(longest_streak, current_streak)
            else:
                current_streak = 1

        return longest_streak

    def _is_within_frequency(self, date1: datetime, date2: datetime) -> bool:
        """
        Check if two dates are within the specified frequency.

        :param date1: The first date.
        :param date2: The second date.
        :return: True if the dates are within the frequency, False otherwise.
        """
        if self.frequency == 'daily':
            return date2 - date1 <= timedelta(days=1)
        elif self.frequency == 'weekly':
            return date2 - date1 <= timedelta(weeks=1)
        elif self.frequency == 'monthly':
            return (date2.year == date1.year and date2.month == date1.month + 1) or \
                   (date2.year == date1.year + 1 and date2.month == 1 and date1.month == 12)
        else:
            raise ValueError("Unsupported frequency. Use 'daily', 'weekly', or 'monthly'.")

    def to_dict(self) -> Dict:
        """
        Convert the habit to a dictionary.

        :return: A dictionary representation of the habit.
        """
        return {
            'name': self.name,
            'frequency': self.frequency,
            'creation_date': self.creation_date.isoformat(),
            'completion_dates': [date.isoformat() for date in self.completion_dates]
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Habit':
        """
        Create a habit from a dictionary.

        :param data: A dictionary representation of the habit.
        :return: A Habit object.
        """
        habit = cls(name=data['name'], frequency=data['frequency'])
        habit.creation_date = datetime.fromisoformat(data['creation_date'])
        habit.completion_dates = [datetime.fromisoformat(date) for date in data['completion_dates']]
        return habit
