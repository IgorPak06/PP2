import re

#file = open('row.txt')

#a_to_b_f = file.read()

#print(re.findall("a[b]*", a_to_b_f))
text = "Aaaaabbbbbccc abbb ab cacbab"

pattern = r'a[b]*'

matches = re.findall(pattern, text)

for match in matches:
    print(match)
