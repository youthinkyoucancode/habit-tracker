import json
from src.habit import Habit

class HabitTracker:
    def __init__(self):
        self.habits = []

    def add_habit(self, habit):
        """Add a new habit to the tracker."""
        self.habits.append(habit)
        self.save_habits_to_file('habits.json')

    def list_habits(self):
        """List all current habits."""
        return self.habits

    def delete_habit(self, habit_name):
        """Delete a habit by its name (case-insensitive)."""
        initial_length = len(self.habits)
        self.habits = [habit for habit in self.habits if habit.name.lower() != habit_name.lower()]
        self.save_habits_to_file('habits.json')
        return len(self.habits) < initial_length

    def load_habits_from_file(self, filename):
        """Load predefined habits from a JSON file."""
        try:
            with open(filename, 'r') as file:
                habit_data = json.load(file)
                for habit in habit_data:
                    new_habit = Habit(habit["name"], habit["desc"], habit.get("periodicity", "daily"))
                    new_habit.check_dates = habit["check_dates"]
                    new_habit.compute_streak()
                    self.habits.append(new_habit)
        except FileNotFoundError:
            print(f"Warning: {filename} not found. Starting with an empty habit list.")

    def save_habits_to_file(self, filename):
        """Save the current list of habits to the JSON file."""
        habit_data = [
            {
                "name": habit.name,
                "desc": habit.desc,
                "periodicity": habit.periodicity,
                "check_dates": habit.check_dates
            }
            for habit in self.habits
        ]
        with open(filename, 'w') as file:
            json.dump(habit_data, file, indent=4)
