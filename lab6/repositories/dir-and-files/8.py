import os

def check_accessability(path):
    if not os.path.exists(path):
        print("Path doesn't exist.")
        return
    
    if not os.access(path, os.F_OK):
        print("No access.")
        return
    
    else:
        os.remove(path)
        print("File deleted.")


if __name__ == "__main__":
    spec_path = input("Enter the file to delete: ")
    check_accessability(spec_path)