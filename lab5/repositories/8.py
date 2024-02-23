import re

text = "It's Beatutiful Day in Europe ASAP"

pattern = r'[A-Z]'

text_splitted = re.split(pattern, text)

print(text_splitted)