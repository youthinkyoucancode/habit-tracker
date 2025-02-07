import click
from src.habit import Habit
from src.habit_tracker import HabitTracker

# Initialize the habit tracker
habit_tracker = HabitTracker()
habit_tracker.load_habits_from_file('habits.json')

@click.group()
def cli():
    """CLI tool for managing and tracking habits."""
    pass

@cli.command()
@click.argument('name')
@click.argument('desc')
@click.argument('periodicity', type=click.Choice(['daily', 'weekly']))
def add(name, desc, periodicity):
    """
    Add a new habit with the specified name, description, and periodicity.
    
    :param name: Name of the habit.
    :param desc: Description of the habit.
    :param periodicity: Either 'daily' or 'weekly'.
    """
    habit = Habit(name, desc, periodicity)
    habit_tracker.add_habit(habit)
    click.echo(f"Habit '{name}' with periodicity '{periodicity}' added successfully.")

@cli.command(name="list")
def list_habits():
    """List all current habits with their descriptions and periodicity."""
    for habit in habit_tracker.list_habits():
        click.echo(f"- {habit.name} ({habit.desc}) [{habit.periodicity}]")

@cli.command()
@click.argument('name')
def delete(name):
    """Delete a habit by name."""
    if habit_tracker.delete_habit(name.lower()):
        click.echo(f"Habit '{name}' has been deleted.")
    else:
        click.echo(f"Habit '{name}' not found.")

@cli.command()
@click.argument('name')
@click.argument('date')
def check(name, date):
    """
    Mark a habit as complete for a specific date.
    
    :param name: Name of the habit.
    :param date: Date to mark as complete (format YYYY-MM-DD).
    """
    for habit in habit_tracker.list_habits():
        if habit.name.lower() == name.lower():
            habit.check(date)
            habit_tracker.save_habits_to_file('habits.json')
            click.echo(f"Habit '{habit.name}' marked as complete on {date}.")
            return
    click.echo(f"Habit '{name}' not found.")

@cli.command()
@click.argument('name')
def progress(name):
    """
    Display the progress of a habit by name, including its streak and check dates.
    
    :param name: Name of the habit.
    """
    for habit in habit_tracker.list_habits():
        if habit.name.lower() == name.lower():
            click.echo(f"Habit: {habit.name}")
            click.echo(f"Description: {habit.desc}")
            click.echo(f"Check Dates: {', '.join(habit.check_dates)}")
            unit = "days" if habit.periodicity == "daily" else "weeks"
            click.echo(f"Longest Streak: {habit.streak} {unit}")
            return
    click.echo(f"Habit '{name}' not found.")
