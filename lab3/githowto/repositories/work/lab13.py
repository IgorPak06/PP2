import random

def guess(cnt1):
    print("Take a guess.")
    n = int(input())
    if n < num:
        print("Your guess is too low.")
        cnt1 += 1
        guess(cnt1)
    elif n > num:
        print("Your guess is too high.")
        cnt1 += 1
        guess(cnt1)
    else:
        print("Good job, ", name, "! You guessed my number in", cnt1, "guesses!")

print("Hello! What is your name?")
name = str(input())

print("Well,", name,", I am thinking of a number between 1 and 20")
num = random.randint(1,20)
cnt = 0
guess(cnt)