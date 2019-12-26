# URL - https://open.kattis.com/problems/everywhere

from collections import Counter

cases = int(input())
places = []

for _ in range(cases):
    places.clear()
    n = int(input())
    for _ in range(n):
        new_place = input()
        places.append(new_place)

    unique_places = len(Counter(places).values())
    print(unique_places)