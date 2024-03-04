import os

def check_access(path):
    if not os.path.exists(path):
        print("Doesn't exist")
        return
    
    print("Existence:", "Yes" if os.path.exists(path) else "No")
    print("Readability:", "Yes" if os.access(path, os.R_OK) else "No")
    print("Writability:", "Yes" if os.access(path, os.W_OK) else "No")
    print("Executability:", "Yes" if os.access(path, os.X_OK) else "No")

if __name__ == "__main__":
    p = input()
    check_access(p)