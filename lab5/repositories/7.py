import re

def snake_to_camel(snake_case):
    parts = snake_case.split('_')
    camel_case = parts[0] + ''.join(word.capitalize() for word in parts[1::])
    return camel_case

text = "hello_world_how_are_you"
camel_case_string = snake_to_camel(text)
print(camel_case_string)