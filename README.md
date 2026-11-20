<<<<<<< HEAD
# Q2: API Consumer and JSON Report

A Python client that fetches users, posts, and comments from JSONPlaceholder, summarizes the data, and saves the result in report.json.

## Requirements

- Python 3
- The requests package
- An internet connection
- See requirements.txt for the package dependency.

## Install the dependency

Open Command Prompt in this folder and run:

~~~cmd
python -m pip install -r requirements.txt
~~~

## Run the program

~~~cmd
python test.py
~~~

The program requests the users, posts, and comments resources. For each successful HTTP response, it prints the status code, response time, and Content-Type. It also handles request timeouts, connection errors, and unsuccessful HTTP status codes.

## Report contents

The program creates or replaces report.json in this folder. The report includes:

- The number of posts and comments for each user.
- The user or users whose posts have the most comments.
- The average character length of post bodies.

## Submission

Include test.py, report.json, this README, requirements.txt, and a screenshot of the console output.
=======
# api-consumer-json
>>>>>>> 986a287c5cf5ebbb9408fc3410fb3e36f713714b
