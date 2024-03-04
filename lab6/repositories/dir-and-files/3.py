import os

def test_path(path):
    if os.path.exists(path):
        print("Path exists")
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print("Filename:", filename)
        print("Directory:", directory)
    else:
        print("Path doesn't exists.")

if __name__ == "__main__":
    p = input()
    test_path(p)