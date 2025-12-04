import os

def batch_rename(folder_path, prefix):
    for index, filename in enumerate(os.listdir(folder_path), start=1):
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, f"{prefix}_{index}_{filename}")

        if os.path.isfile(old_path):
            os.rename(old_path, new_path)

    print(" Rename completed")

if __name__ == "__main__":
    path = input("Enter folder path: ")
    prefix = input("Enter rename prefix: ")
    batch_rename(path, prefix)
