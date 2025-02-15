import json
from src.habit import Habit

class HabitTracker:
    def __init__(self, filename='habits.json'):
        """
        Initialize the habit tracker.
        
        :param filename: The JSON file used for loading and saving habits.
        """
        self.habits = []
        self.filename = filename

    def add_habit(self, habit):
        """Add a new habit to the tracker and save it to the file."""
        self.habits.append(habit)
        self.save_habits_to_file()

    def list_habits(self):
        """List all current habits."""
        return self.habits

    def delete_habit(self, habit_name):
        """Delete a habit by its name (case-insensitive) and save the changes."""
        initial_length = len(self.habits)
        self.habits = [habit for habit in self.habits if habit.name.lower() != habit_name.lower()]
        self.save_habits_to_file()
        return len(self.habits) < initial_length

    def load_habits_from_file(self):
        """Load predefined habits from the JSON file."""
        try:
            with open(self.filename, 'r') as file:
                habit_data = json.load(file)
                for habit in habit_data:
                    new_habit = Habit(habit["name"], habit["desc"], habit.get("periodicity", "daily"))
                    new_habit.check_dates = habit["check_dates"]
                    new_habit.compute_streak()
                    self.habits.append(new_habit)
        except FileNotFoundError:
            print(f"Warning: {self.filename} not found. Starting with an empty habit list.")

    def save_habits_to_file(self):
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
        with open(self.filename, 'w') as file:
            json.dump(habit_data, file, indent=4)
