from src.habit import Habit

def test_habit_initialization():
    """Test that a habit is correctly initialized with its attributes."""
    habit = Habit("Workout", "Daily workout routine", "daily")
    assert habit.name == "Workout"
    assert habit.desc == "Daily workout routine"
    assert habit.periodicity == "daily"
    assert habit.streak == 0
    assert habit.check_dates == []

def test_check_dates():
    """Test that dates are correctly added when the habit is checked off."""
    habit = Habit("Workout", "Daily workout routine", "daily")
    habit.check("2025-02-01")
    habit.check("2025-02-02")
    assert len(habit.check_dates) == 2
    assert "2025-02-01" in habit.check_dates
    assert "2025-02-02" in habit.check_dates

def test_check_duplicate_date():
    """Ensure that duplicate dates are not added."""
    habit = Habit("Workout", "Daily workout routine", "daily")
    habit.check("2025-02-01")
    habit.check("2025-02-01")
    assert len(habit.check_dates) == 1  # Duplicate date should not be added

def test_compute_streak_consecutive():
    """Test streak calculation for consecutive daily habits."""
    habit = Habit("Workout", "Daily workout routine", "daily")
    habit.check("2025-02-01")
    habit.check("2025-02-02")
    habit.check("2025-02-03")
    habit.compute_streak()
    assert habit.streak == 3  # Streak should be 3 for 3 consecutive days

def test_compute_streak_with_gaps():
    """Test that the streak resets when there is a gap in daily completions."""
    habit = Habit("Workout", "Daily workout routine", "daily")
    habit.check("2025-02-01")
    habit.check("2025-02-02")
    habit.check("2025-02-05")  # Gap in dates
    habit.compute_streak()
    assert habit.streak == 2  # Streak should reset after the gap

def test_compute_streak_weekly():
    """Test streak calculation for weekly habits."""
    habit = Habit("Weekly cleanup", "Clean the house every weekend", "weekly")
    habit.check("2025-01-18")
    habit.check("2025-01-25")
    habit.check("2025-02-01")
    habit.compute_streak()
    assert habit.streak == 3  # Streak should be 3 for 3 consecutive weeks
