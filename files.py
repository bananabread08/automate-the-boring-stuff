import os

# walk() -> generates the file names in a directory tree


for root, dirs, files in os.walk('.'):
    print(root)
    print(dirs)
    print(files)
