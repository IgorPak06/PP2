import re

#file = open('row.txt')

#a_to_b_f = file.read()

text = "ABc abc Cba lol b Ruh"

pattern = r'\b[A-Z]+[a-z]+\b'

print(re.findall(pattern, text))