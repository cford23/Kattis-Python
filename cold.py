# URL - https://open.kattis.com/problems/cold

numbers = input()

count = 0
temps = list(map(int, input().split()))
for temp in temps:
    if temp < 0:
        count += 1

print(count)