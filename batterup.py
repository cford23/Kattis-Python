# URL - https://open.kattis.com/problems/batterup

num = int(input())
atbats = list(map(int, input().split()))

top = 0
for bat in atbats:
    if bat != -1:
        top += bat
    else:
        num -= 1

total = top / num
print(total)