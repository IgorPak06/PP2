import string

def generator():
    for l in string.ascii_uppercase:
        file_name = l + ".txt"
        with open(file_name, "x") as file:
            print(f"This is file '{file_name}'.")
        print("File {} created".format(file_name))

if __name__ == "__main__":
    generator()