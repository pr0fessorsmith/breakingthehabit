import click
from src.user import User
from src.habit import Habit
from src.analytics import get_longest_streak, get_longest_streak_all, get_user_longest_streak, get_user_longest_streak_all

# Define the path to the JSON file
USER_DATA_FILE = 'users_data.json'

# Load all users data from JSON file
try:
    users = User.load_all_from_json(USER_DATA_FILE)
except FileNotFoundError:
    users = {}

# Current user
current_user = None

@click.group()
def cli():
    """A simple CLI for managing habits."""
    pass

@cli.command()
@click.argument('username')
@click.argument('email')
def create_user(username, email):
    """Create a new user with a given username and email."""
    global users, current_user
    if username in users:
        click.echo(f"User '{username}' already exists.")
        return
    user = User(username=username, email=email)
    users[username] = user
    current_user = user
    User.save_all_to_json(users, USER_DATA_FILE)
    click.echo(f"User '{username}' with email '{email}' created.")

@cli.command()
@click.argument('username')
def remove_user(username):
    """Remove an existing user."""
    global users, current_user
    if username not in users:
        click.echo(f"User '{username}' not found.")
        return
    del users[username]
    if current_user and current_user.username == username:
        current_user = None
    User.save_all_to_json(users, USER_DATA_FILE)
    click.echo(f"User '{username}' removed.")

@cli.command()
@click.argument('username')
def change_user(username):
    """Change the current user."""
    global users, current_user
    if username not in users:
        click.echo(f"User '{username}' not found.")
        return
    current_user = users[username]
    click.echo(f"Current user changed to '{username}'.")

@cli.command()
@click.argument('name')
@click.argument('frequency')
def create_habit(name, frequency):
    """Create a new habit with a given name and frequency."""
    if not current_user:
        click.echo("No user selected. Use 'change_user' to select a user.")
        return
    habit = Habit(name=name, frequency=frequency)
    current_user.add_habit(habit)
    User.save_all_to_json(users, USER_DATA_FILE)
    click.echo(f"Habit '{name}' with frequency '{frequency}' created.")

@cli.command()
def list_habits():
    """List all habits."""
    if not current_user:
        click.echo("No user selected. Use 'change_user' to select a user.")
        return
    habits = current_user.get_habits()
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
    if not current_user:
        click.echo("No user selected. Use 'change_user' to select a user.")
        return
    try:
        habit = current_user.get_habit_by_name(name)
        habit.frequency = new_frequency
        User.save_all_to_json(users, USER_DATA_FILE)
        click.echo(f"Habit '{name}' frequency updated to '{new_frequency}'.")
    except ValueError as e:
        click.echo(str(e))

@cli.command()
@click.argument('name')
def complete_task(name):
    """Mark a habit task as completed."""
    if not current_user:
        click.echo("No user selected. Use 'change_user' to select a user.")
        return
    try:
        habit = current_user.get_habit_by_name(name)
        habit.complete_task()
        User.save_all_to_json(users, USER_DATA_FILE)
        click.echo(f"Habit '{name}' marked as completed.")
    except ValueError as e:
        click.echo(str(e))

@cli.command()
@click.argument('name')
def longest_streak(name):
    """Get the longest streak for a specific habit."""
    if not current_user:
        click.echo("No user selected. Use 'change_user' to select a user.")
        return
    streak = get_user_longest_streak(current_user, name)
    click.echo(f"The longest streak for habit '{name}' is {streak} days.")

@cli.command()
def longest_streak_all():
    """Get the habit with the longest streak among all habits."""
    if not current_user:
        click.echo("No user selected. Use 'change_user' to select a user.")
        return
    habit_name = get_user_longest_streak_all(current_user)
    click.echo(f"The habit with the longest streak is '{habit_name}'.")

if __name__ == '__main__':
    cli()