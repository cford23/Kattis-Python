# URL - https://open.kattis.com/problems/datum

from math import floor

day, month = map(int, input().split())
dates = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if month == 1 or month == 2:
    Y = 8
    month += 10
else:
    Y = 9
    month -= 2

date = (day + floor(2.6*month - 0.2) - 2 * 20 + Y + floor(Y / 4) + floor(20 / 4)) % 7

print(dates[date])