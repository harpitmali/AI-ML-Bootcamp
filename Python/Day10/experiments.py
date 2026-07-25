# Experiment 1 — Current Date & Time

import datetime

current_date = datetime.date.today()
current_time = datetime.datetime.now().strftime("%H:%M:%S")
current_date_and_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

print(f"Current Date: {current_date}")
print(f"Current Time: {current_time}")
print(f"Current Date & Time: {current_date_and_time}")

# Experiment 2 — Date Formatting

current_date = datetime.datetime.now()

print(f"{current_date.strftime("%d/%m/%Y")}")
print(f"{current_date.strftime("%B %d, %Y")}")
print(f"{current_date.strftime("%A, %B %d")}") 

# Experiment 3 — String to Date

random_day = datetime.datetime.strptime("25/12/2026", "%d/%m/%Y")

print(random_day)
print(type(random_day))
print(random_day.year)
print(random_day.month)
print(random_day.day)

# Experiment 4 — Multithreading

import threading
import time

def task1():
    for i in range(1, 6):
        print(f"Task 1: {i}")
        time.sleep(1)

def task2():
    for i in range(1, 6):
        print(f"Task 2: {i}")
        time.sleep(1)

t1 = threading.Thread(target=task1)
t1.start()

t2 = threading.Thread(target=task2)
t2.start()

t1.join()
t2.join()

print("All task completed!")

# Experiment 5 — Simple API Request

import requests

base_url = "https://api.github.com"
response = requests.get(base_url)

print(f"Status Code: {response.status_code}")

print("\nResponse Headers:")
for key, value in response.headers.items():
    print(f"{key}: {value}")

data = response.json()

print("\nJSON Response:")
print(data)

print("\nSome Key Field:")
print(f"Current User URL:, {data["current_user_url"]}")
print(f"Current User Authorizations URL: {data["current_user_authorizations_html_url"]}")
print("Repository URL:", data["repository_url"])
print("Rate Limit URL:", data["rate_limit_url"])