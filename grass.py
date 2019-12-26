# URL - https://open.kattis.com/problems/grassseed

cost = float(input())
lawns = int(input())

totalCost = 0
for _ in range(lawns):
    width, length = map(float, input().split())
    totalCost += width * length * cost

print(totalCost)