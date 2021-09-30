import os
import zipfile
with zipfile.ZipFile('/home/yassya/Рабочий стол/main.zip') as my_zip_file:
    my_zip_file.extractall('/home/yassya/Рабочий стол')

lst = list()

os.chdir("/home/yassya/Рабочий стол/main")
for current_dir, dirs, files in os.walk("."):
    for names in files:
        if names[-2:] == 'py':
            lst.append(current_dir)
print(sorted(lst))


