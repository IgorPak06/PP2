import re

text = "HelloWorld"

pattern = r'(?<=[a-z])(?=[A-Z])'

spaced_text = re.sub(pattern, ' ', text)
print(spaced_text)