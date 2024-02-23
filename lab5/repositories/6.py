import re

text = "This message doesn't belongs to you, fool"

pattern = r'[ ,.]'

replaced_occurences = re.sub(pattern, '|', text)

print(replaced_occurences)