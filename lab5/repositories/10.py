import re

def camel_to_snake(camel_case):
    snake_case = ''
    for i, char in enumerate(camel_case):
        if i > 0 and char.isupper():
            snake_case += '_'
        snake_case += char.lower()
    return snake_case

text = "helloWorldHowAreYou"
camel_case_string = camel_to_snake(text)
print(camel_case_string)