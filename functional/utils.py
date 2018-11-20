import os


def list_all_files_in_folder():
    for root, dirs, files in os.walk("addresses/"):
        for filename in files:
            print(filename)
