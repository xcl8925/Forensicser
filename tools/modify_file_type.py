import os
import random

path = r'E:\test'
files = os.listdir(path)
type = ".jpg"

for file in files:
    print(file)
    if not file.endswith(".jpg"):

        old_name = os.path.join(path, file)
        new_name = os.path.join(path, file + type)
        print(new_name)
        try:
            os.rename(old_name, new_name)
        except FileExistsError:
            new_name = os.path.join(path, file + str(random.randint(0, 9)) + type)
            os.rename(old_name, new_name)


