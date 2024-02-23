import re

text = r"acb"

pattern = r'a.*b$'

print(re.findall(pattern, text))