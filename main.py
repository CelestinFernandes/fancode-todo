import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

BASE_URL = "http://jsonplaceholder.typicode.com"
USER_URL = f"{BASE_URL}/users"
TODO_URL = f"{BASE_URL}/todos"
LAT_RANGE = (-40, 5)
LON_RANGE = (5, 100)
COMPLETION_THRESHOLD = 50

def fetch_data(url):
    """Fetch data from the given API URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from {url}: {e}")
        return []


def filter_users_by_geolocation(users, lat_range, lon_range):
    """Filter users based on latitude and longitude."""
    return [
        user for user in users
        if lat_range[0] <= float(user['address']['geo']['lat']) <= lat_range[1]
        and lon_range[0] <= float(user['address']['geo']['lng']) <= lon_range[1]
    ]


def calculate_completion_percentage(todos, user_id):
    """Calculate the percentage of completed tasks for a user."""
    user_todos = [todo for todo in todos if todo['userId'] == user_id]
    if not user_todos:
        return 0
    completed_tasks = sum(todo['completed'] for todo in user_todos)
    return (completed_tasks / len(user_todos)) * 100


def main():
    logging.info("Fetching user data...")
    users = fetch_data(USER_URL)

    logging.info("Fetching todo data...")
    todos = fetch_data(TODO_URL)

    logging.info("Filtering users by geolocation...")
    target_users = filter_users_by_geolocation(users, LAT_RANGE, LON_RANGE)

    logging.info(f"Number of users in the target location: {len(target_users)}")
    if target_users:
        logging.info("Users in the target location:")
        for user in target_users:
            print(f"User: {user['name']}")

    logging.info("Calculating task completion percentages...")
    eligible_users = []
    for user in target_users:
        completion_percentage = calculate_completion_percentage(todos, user['id'])
        if completion_percentage > COMPLETION_THRESHOLD:
            eligible_users.append({
                "name": user['name'],
                "completion_percentage": completion_percentage
            })

    if eligible_users:
        logging.info(f"Users with more than {COMPLETION_THRESHOLD}% tasks completed:")
        for user in eligible_users:
            print(f"User: {user['name']}, Completed: {user['completion_percentage']:.2f}%")
    else:
        logging.info(f"No users found with more than {COMPLETION_THRESHOLD}% tasks completed.")


if __name__ == "__main__":
    main()
