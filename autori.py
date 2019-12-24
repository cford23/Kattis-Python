msg = input()
shortened = ""

length = len(msg)
for letter in range(length):
    if msg[letter].isupper():
        shortened += msg[letter]

print(shortened)