# URL - https://open.kattis.com/problems/pieceofcake2

n, h, v = map(int, input().split())
squares = []

square = h * v * 4
squares.append(square)

square = (n - h) * v * 4
squares.append(square)

square = h * (n - v) * 4
squares.append(square)

square = (n - h) * (n - v) * 4
squares.append(square)

biggest = 0
for size in squares:
    if size > biggest:
        biggest = size

print(biggest)