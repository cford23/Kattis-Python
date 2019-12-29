# URL - https://open.kattis.com/problems/conundrum

cipher = input()
length = len(cipher)

count = 0
for letter in range(length):
    if letter % 3 == 0:
        if cipher[letter] != "P":
            count += 1
    elif letter % 3 == 1:
        if cipher[letter] != "E":
            count += 1
    elif letter % 3 == 2:
        if cipher[letter] != "R":
            count += 1

print(count)