# URL - https://open.kattis.com/problems/fizzbuzz

fizz, buzz, numbers = map(int, input().split())

for num in range(1, numbers + 1):
    if num % fizz == 0 and num % buzz == 0:
        print("FizzBuzz")
    elif num % fizz == 0:
        print("Fizz")
    elif num % buzz == 0:
        print("Buzz")
    else:
        print(num)