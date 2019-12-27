# URL - https://open.kattis.com/problems/detaileddifferences

cases = int(input())
outputList = []

for _ in range(cases):
    output = ""
    string1 = input()
    string2 = input()
    length = len(string1)
    for c in range(length):
        if string1[c] == string2[c]:
            output += "."
        else:
            output += "*"
    outputList.append(string1)
    outputList.append(string2)
    outputList.append(output)

count = 0
for string in outputList:
    print(string)
    count += 1
    if count % 3 == 0:
        print("\n")