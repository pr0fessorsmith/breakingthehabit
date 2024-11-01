from datetime import datetime, timedelta
from src.habit import Habit
from src.user import User

def get_all_habits():
    habits = Habit.load_all()
    return [habit.name for habit in habits]

def get_habits_by_period(frequency):
    habits = Habit.load_all()
    return [habit.name for habit in habits if habit.frequency == frequency]

def get_longest_streak(habit_name):
    habit = Habit.load(habit_name)
    if habit:
        return calculate_streak(habit.completion_dates, habit.frequency)
    return 0

def get_longest_streak_all():
    habits = Habit.load_all()
    streaks = {habit.name: calculate_streak(habit.completion_dates, habit.frequency) for habit in habits}
    return max(streaks, key=streaks.get)

def get_user_longest_streak(user: User, habit_name: str) -> int:
    habit = user.get_habit_by_name(habit_name)
    if habit:
        return calculate_streak(habit.completion_dates, habit.frequency)
    return 0

def get_user_longest_streak_all(user: User) -> str:
    streaks = {habit.name: calculate_streak(habit.completion_dates, habit.frequency) for habit in user.get_habits()}
    return max(streaks, key=streaks.get)

def calculate_streak(completion_dates, frequency):
    if not completion_dates:
        return 0

    # Sort completion dates
    sorted_dates = sorted(completion_dates)
    longest_streak = 1
    current_streak = 1

    # Calculate streaks
    for i in range(1, len(sorted_dates)):
        if is_within_frequency(sorted_dates[i - 1], sorted_dates[i], frequency):
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        else:
            current_streak = 1

    return longest_streak

def is_within_frequency(date1, date2, frequency):
    if frequency == 'daily':
        return date2 - date1 <= timedelta(days=1)
    elif frequency == 'weekly':
        return date2 - date1 <= timedelta(weeks=1)
    elif frequency == 'monthly':
        return (date2.year == date1.year and date2.month == date1.month + 1) or \
               (date2.year == date1.year + 1 and date2.month == 1 and date1.month == 12)
    else:
        raise ValueError("Unsupported frequency. Use 'daily', 'weekly', or 'monthly'.")
