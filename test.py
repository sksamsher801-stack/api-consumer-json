import json  # Write the final report as JSON.
import time  # Measure API response times.
import requests  # Send HTTP requests to the public API.
BASE_URL = "https://jsonplaceholder.typicode.com"  # Base address for the sample API.
def get_data(endpoint):  # Fetch one API resource and report request details.
    """data taken from the API and shown the data of requests."""
    url = BASE_URL + endpoint
    start_time = time.perf_counter()
    try:
        response = requests.get(url, timeout=10)  # Request data with a 10-second timeout.
        response_time = time.perf_counter() - start_time
        content_type = response.headers.get("Content-Type", "Not provided")
        print(
            f"GET {endpoint} | "
            f"Status: {response.status_code} | "
            f"Time: {response_time:.2f}s | "
            f"Content-Type: {content_type}"
        )
        response.raise_for_status()  # Treat non-success HTTP status codes as errors.
        return response.json()  # Convert the JSON response into Python data.
    except requests.exceptions.Timeout:
        print(f"{endpoint} request timed out.")
    except requests.exceptions.ConnectionError:
        print(f"{endpoint} connection failed.")
    except requests.exceptions.HTTPError:
        print(f"{endpoint} returned an error status.")
    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")
    return None
users = get_data("/users")
posts = get_data("/posts")
comments = get_data("/comments")
if users is None or posts is None or comments is None:
    raise SystemExit("all data are not collected properly.Please check Internet connection.")
posts_per_user = {}
for user in users:
    posts_per_user[user["id"]] = 0
for post in posts:
    user_id = post["userId"]
    posts_per_user[user_id] += 1
post_owner = {}  # Map each post ID to the ID of its user.
for post in posts:
    post_owner[post["id"]] = post["userId"]
comments_per_user = {}  # Track comment totals for each user.
for user in users:
    comments_per_user[user["id"]] = 0
for comment in comments:
    post_id = comment["postId"]
    user_id = post_owner[post_id]
    comments_per_user[user_id] += 1
highest_comment_count = 0
top_user_ids = []
for user_id in comments_per_user:
    count = comments_per_user[user_id]
    if count > highest_comment_count:
        highest_comment_count = count
        top_user_ids = [user_id]
    elif count == highest_comment_count:
        top_user_ids.append(user_id)
top_users = []
for top_user_id in top_user_ids:
    for user in users:
        if user["id"] == top_user_id:
            top_users.append({
                "user_id": top_user_id,
                "name": user["name"],
                "comment_count": highest_comment_count,
            })
total_length = 0  # Accumulate post body character counts.
for post in posts:
    total_length += len(post["body"])
if len(posts) > 0:
    average_post_length = total_length / len(posts)
else:
    average_post_length = 0
user_summaries = []
for user in users:
    user_id = user["id"]
    user_summaries.append({
        "user_id": user_id,
        "name": user["name"],
        "post_count": posts_per_user[user_id],
        "comment_count": comments_per_user[user_id],
    })
report = {  # Collect the calculated results for the report.
    "users": user_summaries,
    "user_with_most_comments": top_users,
    "average_post_body_length_characters": round(average_post_length, 2),
}
with open("report.json", "w", encoding="utf-8") as file:  # Open the report file for writing.
    json.dump(report, file, indent=2, ensure_ascii=False)  # Save the report in readable JSON format.
print("\nUser(s) with the most comments:")
for user in top_users:
    print(
        f"{user['name']} "
        f"(ID: {user['user_id']}) - "
        f"{user['comment_count']} comments"
    )
print("Report saved to report.json")
