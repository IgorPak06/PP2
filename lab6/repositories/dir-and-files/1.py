import os

def list_directories_files(path):
    print("Directories:")
    for dir_name in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir_name)):
            print(dir_name)

    print("Files:")
    for file_name in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_name)):
            print(file_name)

def list_all_directories(path):
    print("All directories and Files:")
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            print(os.path.join(root, dir_name))
        for file_name in files:
            print(os.path.join(root, file_name))

if __name__ == "__main__":
    p = input()
    print(list_directories_files(p))
    print(list_all_directories(p))
    