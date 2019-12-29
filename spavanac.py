# URL - https://open.kattis.com/problems/spavanac

hour, minute = map(int, input().split())

if minute >= 45:
    minute -= 45
else:
    if hour == 0:
        hour = 23
    else:
        hour -= 1
    minute = 45 - minute
    minute = 60 - minute

print(f"{hour} {minute}")