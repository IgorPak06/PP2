import time
import math

def calculate_root(number, ms):
    time.sleep(ms/1000)
    result = math.sqrt(number)
    return result

number = int(input())
ms = int(input())

print("Square root of ", number, "after ", ms, "miliseconds is ", calculate_root(number, ms))
