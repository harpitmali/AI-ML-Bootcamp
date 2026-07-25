import datetime

date = datetime.date(2026, 1, 21)
print(date)

today = datetime.date.today()
print(today)

time = datetime.time(11, 11, 11)
print(time)

now = datetime.datetime.now()
print(now)

now = now.strftime("%H:%M:%S %d-%m-%Y")
print(now)

target_datetime = datetime.datetime(2030, 2, 17, 11, 11, 11)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")