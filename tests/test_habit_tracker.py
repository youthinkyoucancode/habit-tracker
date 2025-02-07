import pytest
from src.habit import Habit
from src.habit_tracker import HabitTracker

def test_add_habit():
    """Test that adding a habit increases the habit list."""
    tracker = HabitTracker()
    tracker.add_habit(Habit("Workout", "Daily workout", "daily"))
    assert len(tracker.habits) == 1
    assert tracker.habits[0].name == "Workout"

def test_delete_habit():
    """Test that a habit can be deleted by name."""
    tracker = HabitTracker()
    tracker.add_habit(Habit("Workout", "Daily workout", "daily"))
    tracker.delete_habit("Workout")
    assert len(tracker.habits) == 0

def test_delete_non_existent_habit():
    """Ensure that attempting to delete a non-existent habit does not cause errors."""
    tracker = HabitTracker()
    tracker.add_habit(Habit("Workout", "Daily workout", "daily"))
    result = tracker.delete_habit("Non-existent habit")
    assert len(tracker.habits) == 1  # No habit should be deleted
    assert result is False  # Should return False when habit is not found

def test_list_habits():
    """Test that the habit tracker correctly lists all habits."""
    tracker = HabitTracker()
    tracker.add_habit(Habit("Workout", "Daily workout", "daily"))
    tracker.add_habit(Habit("Read", "Read a book", "daily"))
    habits = tracker.list_habits()
    assert len(habits) == 2
    assert habits[0].name == "Workout"
    assert habits[1].name == "Read"

def test_save_and_load_habits(tmp_path):
    """Test that habits are saved and loaded correctly from a file."""
    tracker = HabitTracker()
    habit = Habit("Workout", "Daily workout", "daily")
    tracker.add_habit(habit)

    # Save to a temporary file
    temp_file = tmp_path / "test_habits.json"
    tracker.save_habits_to_file(temp_file)

    # Create a new tracker and load the data
    new_tracker = HabitTracker()
    new_tracker.load_habits_from_file(temp_file)

    assert len(new_tracker.habits) == 1
    assert new_tracker.habits[0].name == "Workout"
