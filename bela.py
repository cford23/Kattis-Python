# URL - https://open.kattis.com/problems/bela

hands, dominant = input().split()
cards = int(hands) * 4

total = 0
for _ in range(cards):
    card = input()
    num = card[0]
    suit = card[1]
    
    if num == "A":
        score = 11
    elif num == "K":
        score = 4
    elif num == "Q":
        score = 3
    elif num == "T":
        score = 10
    elif num == "8":
        score = 0
    elif num == "7":
        score = 0
    elif num == "J":
        if suit == dominant:
            score = 20
        else:
            score = 2
    elif num == "9":
        if suit == dominant:
            score = 14
        else:
            score = 0

    total += score

print(total)