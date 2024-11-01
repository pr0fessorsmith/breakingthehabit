import click
from src.user import User
from src.habit import Habit
from src.analytics import get_longest_streak, get_longest_streak_all

# Define the path to the JSON file
USER_DATA_FILE = 'user_data.json'

# Load user data from JSON file
try:
    user = User.load_from_json(USER_DATA_FILE)
except FileNotFoundError:
    user = User(username="cli_user", email="cli_user@example.com")

@click.group()
def cli():
    """A simple CLI for managing habits."""
    pass

@cli.command()
@click.argument('name')
@click.argument('frequency')
def create_habit(name, frequency):
    """Create a new habit with a given name and frequency."""
    habit = Habit(name=name, frequency=frequency)
    user.add_habit(habit)
    user.save_to_json(USER_DATA_FILE)
    click.echo(f"Habit '{name}' with frequency '{frequency}' created.")

@cli.command()
def list_habits():
    """List all habits."""
    habits = user.get_habits()
    if not habits:
        click.echo("No habits found.")
    else:
        for habit in habits:
            click.echo(f"Habit: {habit.name}, Frequency: {habit.frequency}")

@cli.command()
@click.argument('name')
@click.argument('new_frequency')
def modify_frequency(name, new_frequency):
    """Modify the frequency of an existing habit."""
    try:
        habit = user.get_habit_by_name(name)
        habit.frequency = new_frequency
        user.save_to_json(USER_DATA_FILE)
        click.echo(f"Habit '{name}' frequency updated to '{new_frequency}'.")
    except ValueError as e:
        click.echo(str(e))

@cli.command()
@click.argument('name')
def complete_task(name):
    """Mark a habit task as completed."""
    try:
        habit = user.get_habit_by_name(name)
        habit.complete_task()
        user.save_to_json(USER_DATA_FILE)
        click.echo(f"Habit '{name}' marked as completed.")
    except ValueError as e:
        click.echo(str(e))

@cli.command()
@click.argument('name')
def longest_streak(name):
    """Get the longest streak for a specific habit."""
    try:
        streak = get_longest_streak(name)
        click.echo(f"The longest streak for habit '{name}' is {streak} days.")
    except ValueError as e:
        click.echo(str(e))

@cli.command()
def longest_streak_all():
    """Get the habit with the longest streak among all habits."""
    try:
        habit_name = get_longest_streak_all()
        click.echo(f"The habit with the longest streak is '{habit_name}'.")
    except ValueError as e:
        click.echo(str(e))

if __name__ == '__main__':
    cli()