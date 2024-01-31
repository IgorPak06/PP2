def isPrime(num):
    if (num < 2):
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filterPrime(numbers):
    count = 0
    for num in numbers:
        if isPrime(num):
            count += 1
    print(count)

numbers = []
x = int(input())
for i in range(x):
    y = int(input())
    numbers.append(y)

filterPrime(numbers)