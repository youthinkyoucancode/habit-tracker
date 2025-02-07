# Habit Tracking Application

This is a **command-line tool** for creating, tracking, and analyzing habits using Python. The application allows users to manage daily and weekly habits, track progress, and analyze streaks, with data stored persistently in a JSON file.

---

## **Features**
- Create and delete habits.
- Support for **daily** and **weekly** habit tracking.
- Mark habits as complete for specific dates.
- Analyze habits and track the longest streak.
- Predefined habits with 4 weeks of tracking data.

---

## **Requirements**
- **Python 3.7 or later** is required.
- Install the following dependencies:
  - `click` for the CLI
  - `pytest` for testing

---

## **Installation**
1. **Clone the repository:**
   ```bash
   git clone https://github.com/youthinkyoucancode/habit-tracker.git
   cd habit-tracker
   ```

2. **Create and activate a virtual environment:**

### **On Windows:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

### **On macOS/Linux:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**
1. **Run the application using:**
   ```bash
   python main.py
   ```

2. **Available commands:**

   - **List all habits:**
     ```bash
     python main.py list
     ```

   - **Add a habit (with periodicity):**
     ```bash
     python main.py add "Habit Name" "Habit Description" [daily/weekly]
     ```
     Example:
     ```bash
     python main.py add "Morning workout" "Daily morning exercise" daily
     python main.py add "Weekly cleanup" "Clean the house every weekend" weekly
     ```

   - **Mark a habit as complete:**
     ```bash
     python main.py check "Habit Name" YYYY-MM-DD
     ```

   - **View progress and streaks for a habit:**
     ```bash
     python main.py progress "Habit Name"
     ```

   - **Delete a habit:**
     ```bash
     python main.py delete "Habit Name"
     ```

---

## **Example Commands**
1. **Add a new daily habit:**
   ```bash
   python main.py add "Drink Water" "Drink 2 liters of water daily" daily
   ```

2. **Add a new weekly habit:**
   ```bash
   python main.py add "Weekly cleaning" "Clean the house every weekend" weekly
   ```

3. **Mark the habit as complete:**
   ```bash
   python main.py check "Drink Water" 2025-02-02
   ```

4. **View the progress:**
   ```bash
   python main.py progress "Drink Water"
   ```

5. **Delete a habit:**
   ```bash
   python main.py delete "Drink Water"
   ```

---

## **Testing**
1. **Run the tests using `pytest`:**
   ```bash
   pytest tests/
   ```

2. **Example output:**
   ```bash
   ============================= test session starts ==============================
   collected 6 items                                                               
   tests/test_habit.py ....                                                  [100%]
   tests/test_habit_tracker.py ...                                           [100%]
   =============================== 6 passed in 0.05s ===============================
   ```

---


## **Predefined Habits**
The project includes 5 predefined habits in `habits.json` with 4 weeks of tracking data:

- **Daily habits**:
  - Morning workout
  - Read a book
  - Evening meditation

- **Weekly habits**:
  - Weekly yoga session
  - Weekly cleanup

---

## **Future Improvements**
- Add a **GUI interface** for easier interaction.
- Add **extended analytics**, such as identifying missed days and trends.

---

## **Credits**
Developed as part of the habit tracker project using **Python** and **click**.  
Testing implemented with **pytest**.





