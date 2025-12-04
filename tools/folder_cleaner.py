import os

def remove_empty_folders(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for d in dirs:
            full_path = os.path.join(root, d)
            if not os.listdir(full_path):
                os.rmdir(full_path)
                print("Deleted:", full_path)

    print(" Cleaning complete")

if __name__ == "__main__":
    path = input("Enter directory path: ")
    remove_empty_folders(path)
