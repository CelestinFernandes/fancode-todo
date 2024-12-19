# User Filtering and Task Completion Analysis Script

To fetch data from JSONPlaceholder's API, filters users based on geographical location, and evaluates their task completion percentages. 

---

## Features

- Fetches user and task data from JSONPlaceholder API endpoints.
- Filters users based on latitude and longitude ranges.
- Calculates the percentage of completed tasks for each user.
- Identifies users with a task completion percentage above a specified threshold.

---

## Requirements

- Python 3.7 or higher
- `requests` library for API requests

Install required library:
```bash
pip install requests
```

---

## Usage

- Clone the repository.
- To run the script:
```bash
python main.py
```
---

## Configuration

Configurable constants:

- **`BASE_URL`**: Base URL for the API endpoints (default: `http://jsonplaceholder.typicode.com`).
- **`USER_URL`**: URL for fetching user data.
- **`TODO_URL`**: URL for fetching task data.
- **`LAT_RANGE`**: Tuple specifying the latitude range for filtering users (default: `(-40, 5)`).
- **`LON_RANGE`**: Tuple specifying the longitude range for filtering users (default: `(5, 100)`).
- **`COMPLETION_THRESHOLD`**: Minimum task completion percentage for eligibility (default: `50`).

---

## Script Overview

### 1. Fetch Data
`fetch_data` function to retrieve user and task data from the JSONPlaceholder API.

### 2. Filter Users by Geolocation
`filter_users_by_geolocation` function filters users based on latitude and longitude ranges.

### 3. Calculate Completion Percentage
`calculate_completion_percentage` function computes the percentage of tasks completed by each user.

### 4. Main Function
`main` function:
- Fetches data from APIs.
- Filters users by location.
- Calculates task completion percentages.
- Identifies and displays users that meet the completion threshold.

---

## Output

Script outputs:
1. Number of users in the target geolocation range.
2. Names of users within the target location.
3. Names and completion percentages of users with task completion above the specified threshold.

---

## Output

```plaintext
2024-12-19 19:38:36,511 - INFO - Fetching user data...
2024-12-19 19:38:36,785 - INFO - Fetching todo data...
2024-12-19 19:38:37,135 - INFO - Filtering users by geolocation...
2024-12-19 19:38:37,136 - INFO - Number of users in the target location: 3
2024-12-19 19:38:37,136 - INFO - Users in the target location:
User: Leanne Graham
User: Chelsey Dietrich
User: Clementina DuBuque
2024-12-19 19:38:37,137 - INFO - Calculating task completion percentages...
2024-12-19 19:38:37,138 - INFO - Users with more than 50% tasks completed:
User: Leanne Graham, Completed: 55.00%
User: Chelsey Dietrich, Completed: 60.00%
User: Clementina DuBuque, Completed: 60.00%
```

---

## Error Handling
- If the API request fails, then an error message is sent and an empty list is returned.