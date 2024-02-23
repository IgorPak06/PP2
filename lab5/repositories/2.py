import re

#file = open('row.txt')

#a_to_b_f = file.read()

#print(re.findall#("a[b]{2,3}", a_to_b_f))
text = "Aaaaabbbbbccc abbb ab cacbab"

pattern = r'a[b]{2,3}'

matches = re.findall(pattern, text)

for match in matches:
    print(match)
