import re

#file = open('row.txt')

#a_to_b_f = file.read()

text = "Abc_abc cba_lol bruh"

pattern = r'\b[a-z]+_[a-z]+\b'

print(re.findall(pattern, text))