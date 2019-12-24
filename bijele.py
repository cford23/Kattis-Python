# URL - https://open.kattis.com/problems/bijele

kings, queens, rooks, bishops, knights, pawns = map(int, input().split())

kings = 1 - kings
queens = 1 - queens
rooks = 2 - rooks
bishops = 2 - bishops
knights = 2 - knights
pawns = 8 - pawns

print(f"{kings} {queens} {rooks} {bishops} {knights} {pawns}")