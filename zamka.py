# URL - https://open.kattis.com/problems/zamka

def sumDigits(number):
    sum = 0
    while number > 0:
        remainder = number % 10
        sum += remainder
        number = number // 10
    return sum

L = int(input())
D = int(input())
X = int(input())

# Set N to be highest number in range
# Set M to be lowest number in range
N = D
M = L

# for N
for num in range(D, L - 1, -1):
    if X == sumDigits(num):
        if num < N:
            N = num

# for M
for num in range(L, D + 1):
    if X == sumDigits(num):
        if num > M:
            M = num

print(N)
print(M)