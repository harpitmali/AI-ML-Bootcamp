# Assignment 1 — Age / Birthday Calculator ⭐⭐

import datetime

try:
    birth_date = input("Enter your birth date(DD/MM/YYYY): ")

    obj_birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")
    current_date = datetime.date.today()

    age = current_date.year - obj_birth_date.year
    if (current_date.month, current_date.day) < (obj_birth_date.month, obj_birth_date.day):
        age -= 1

    print(f"Birth date: {obj_birth_date.strftime("%d %B %Y")}")
    print(f"Birth Year: {obj_birth_date.year}")
    print(f"Approximate Age: {age}")
except ValueError:
    print("Invalid Input")


# Assignment 2 — Activity Logger ⭐⭐
    
import datetime

def log_activity(activity):
    current_date = datetime.datetime.now()
    with open("activities.txt", "a") as file:
        file.write(f"{current_date.strftime("%d/%m/%Y %H:%M:%S")} - {activity}\n")


activity = input("What did you do? ")

log_activity(activity)

# Assignment 3 — Activity Reader ⭐⭐

def read_activity():
    try:
        with open("activities.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No Activity found")
        else:
            print("===== Activity History =====")
            for i,line in enumerate(lines, start=1):
                time, task = line.strip().split("-", 1)
                print(f"{i}. {time} {task}")
                print()
    except FileNotFoundError:
        print("File Not Found")

read_activity()


# Assignment 4 — API Data Reader ⭐⭐⭐

import requests

try:
    response = requests.get("https://api.github.com")

    if response.status_code == 200:
        data = response.json()
        print("===== GitHub API =====")
        print(f"Status: Success")
        print(f"Repository URL: {data["repository_url"]}")
        print(f"User URL: {data["user_url"]}")
        print(f"Rate Limit URL: {data["rate_limit_url"]}")
        print(f"Gists URL:  {data["gists_url"]}")
    else: 
        print("Request Failed")
        print(f"Status Code: {response.status_code}")
        
except requests.RequestException:
    print("Request Failed")


# ⭐ Bonus — Mini API + File Pipeline
import datetime
import requests

try:
    def fetch_data_into_file(data):
        current_date = datetime.datetime.now()
        with open("api_data.txt", "w") as file:
            file.write(f"Fetched: {current_date.strftime("%d/%m/%Y %H:%M:%S")}\n")
            file.write(f"Repository URL: {data["repository_url"]}\n")
            file.write(f"User URL: {data["user_url"]}\n")
            file.write(f"Rate Limit URL: {data["rate_limit_url"]}\n")
            file.write(f"Gists URL:  {data["gists_url"]}")

    def read_data_from_file():
        with open("api_data.txt", "r") as file:
            print(file.read())


    response = requests.get("https://api.github.com")

    if response.status_code == 200:
        data = response.json()
        fetch_data_into_file(data)
        read_data_from_file()
    else:
        print("Request Failed")
        print(f"Status Code: {response.status_code}")
except requests.exceptions.RequestException:
    print("Unable to connect to the API.")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)
