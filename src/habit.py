from datetime import datetime, timedelta

class Habit:
    def __init__(self, name, desc, periodicity="daily"):
        """
        Initialize a new Habit instance.
        
        :param name: The name of the habit.
        :param desc: A description of the habit.
        :param periodicity: Either 'daily' or 'weekly'.
        """
        self.name = name
        self.desc = desc
        self.periodicity = periodicity  # "daily" or "weekly"
        self.streak = 0
        self.check_dates = []  # Dates when the habit was marked as complete

    def check(self, date):
        """
        Mark the habit as complete on the given date and compute streak.
        
        :param date: The date to mark the habit as complete (format YYYY-MM-DD).
        """
        if date not in self.check_dates:
            self.check_dates.append(date)
            self.compute_streak()

    def compute_streak(self):
        """
        Compute the streak based on consecutive check-off dates, 
        considering the periodicity (daily or weekly).
        """
        if not self.check_dates:
            self.streak = 0
            return

        # Sort dates in ascending order
        sorted_dates = sorted([datetime.strptime(date, "%Y-%m-%d") for date in self.check_dates])
        self.streak = 1  # Minimum streak starts at 1
        current_streak = 1

        for i in range(1, len(sorted_dates)):
            if self.periodicity == "daily":
                # Check for consecutive days
                if (sorted_dates[i] - sorted_dates[i - 1]) == timedelta(days=1):
                    current_streak += 1
                else:
                    current_streak = 1  # Reset streak if non-consecutive

            elif self.periodicity == "weekly":
                # Check for consecutive weeks
                if (sorted_dates[i] - sorted_dates[i - 1]) == timedelta(weeks=1):
                    current_streak += 1
                else:
                    current_streak = 1  # Reset streak if non-consecutive

            # Update the longest streak
            self.streak = max(self.streak, current_streak)
