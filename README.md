# User Filtering and Task Completion Analysis Script

This Python script fetches data from JSONPlaceholder's API, filters users based on geographical location, and evaluates their task completion percentages. It demonstrates basic API consumption, data filtering, and processing using Python.

---

## Features

- Fetches user and task data from JSONPlaceholder API endpoints.
- Filters users based on latitude and longitude ranges.
- Calculates the percentage of completed tasks for each user.
- Identifies users with a task completion percentage above a specified threshold.
- Outputs user information and statistics to the console.

---

## Requirements

- Python 3.7 or higher
- `requests` library for API requests

Install the required library using:
```bash
pip install requests
```

---

## Usage

1. Clone the repository or copy the script to your local machine.
2. Ensure Python and the required dependencies are installed.
3. Run the script using:
```bash
python main.py
```

If you encounter import issues while testing, ensure the following:

- Set the `PYTHONPATH` environment variable to the project root before running tests:
  ```bash
  set PYTHONPATH=.
  pytest
  ```
  Or for PowerShell:
  ```bash
  $env:PYTHONPATH = "."
  pytest
  ```
- Alternatively, add `sys.path` manipulation in `test_main.py` for direct referencing.

---

## Configuration

The script includes configurable constants:

- **`BASE_URL`**: Base URL for the API endpoints (default: `http://jsonplaceholder.typicode.com`).
- **`USER_URL`**: URL for fetching user data.
- **`TODO_URL`**: URL for fetching task data.
- **`LAT_RANGE`**: Tuple specifying the latitude range for filtering users (default: `(-40, 5)`).
- **`LON_RANGE`**: Tuple specifying the longitude range for filtering users (default: `(5, 100)`).
- **`COMPLETION_THRESHOLD`**: Minimum task completion percentage for eligibility (default: `50`).

---

## Script Overview

### 1. Fetch Data

The script uses the `fetch_data` function to retrieve user and task data from the JSONPlaceholder API.

### 2. Filter Users by Geolocation

The `filter_users_by_geolocation` function filters users based on latitude and longitude ranges.

### 3. Calculate Completion Percentage

The `calculate_completion_percentage` function computes the percentage of tasks completed by each user.

### 4. Main Function

The `main` function orchestrates the workflow:
- Fetches data from APIs.
- Filters users by location.
- Calculates task completion percentages.
- Identifies and displays users meeting the completion threshold.

---

## Output

The script outputs:

1. The number of users in the target geolocation range.
2. Names of users within the target location.
3. Names and completion percentages of users with task completion above the specified threshold.

---

## Example Output

```plaintext
2024-12-19 10:00:00 - INFO - Fetching user data...
2024-12-19 10:00:01 - INFO - Fetching todo data...
2024-12-19 10:00:02 - INFO - Filtering users by geolocation...
2024-12-19 10:00:02 - INFO - Number of users in the target location: 3
2024-12-19 10:00:02 - INFO - Users in the target location:
User: Leanne Graham
User: Chelsey Dietrich
User: Clementina DuBuque
2024-12-19 10:00:03 - INFO - Calculating task completion percentages...
2024-12-19 10:00:03 - INFO - Users with more than 50% tasks completed:
User: Leanne Graham, Completed: 55.00%
User: Chelsey Dietrich, Completed: 60.00%
User: Clementina DuBuque, Completed: 60.00%
```

---

## Error Handling

- If the API request fails, an error message is logged and an empty list is returned.
- The script gracefully handles cases where no users or tasks meet the specified criteria.