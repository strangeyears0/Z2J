# Creating patho objects from strings
#
import pathlib
#
# path = pathlib.Path("/Users/David/Documents/hello.txt")
#
# # path = pathlib.Path("C:\Users\David\Desktop\hello.txt")
# path = pathlib.Path("C:/Users/David/Desktop/hello.txt")
# path = pathlib.Path(r"C:\Users\David\Desktop\hello.txt")
#
#
# home = pathlib.Path.home()
# print(home)
# print(pathlib.Path.cwd())
# print (home / "Desktop" / "hello.txt")
#
# print(path.is_absolute())
# # .resolve return absolute path
#
# list = list(path.parents)
# print(list)
#
# for directory in list:
#     print(directory)
#
# print(path.parent)
#
# # .parent is a shortcut for . parents[0]
#
# # absolute path:
# print(path.anchor)
#
# # for relative paths :
# path = pathlib.Path("hello.txt")
# print(path.anchor)
#
# #.name
#
# path = pathlib.Path.home()
# print(path.name)
# path = home / "hello.txt"
# print(path.name)
# print(path.stem)
# print(path.suffix)
#
# #.exists
#
#
# path = pathlib.Path.home() / "hello.txt"
# print(path.exists())
#
# #.is_file()
#
# print(path.is_file())
#
# #.is_dir()
#
# print(path.is_dir())
# print(home.is_dir())

# ex1

# from pathlib import Path
#
# file_path = Path.home() / "my_folder" / "my_file.txt"
# print(file_path)
#
# # ex2
#
# print(file_path.exists())
#
# # ex3
# print(file_path.name)
#
# #ex4
# print(file_path.parent.name)

#12.3 COmmon file system operatios
#
# from pathlib import Path
#
# new_dir = Path.home() / "new_directory"
# #
# new_dir.mkdir(parents=True, exist_ok=True)
#
# # print(new_dir.exists())
# # print(new_dir.is_dir())
#
# nested_dir = new_dir / "folder_a"
# nested_dir = new_dir / "folder_b"
#
# nested_dir.mkdir(parents=True, exist_ok=True)
#
# file_path = new_dir / "file1.txt"
# file_path = new_dir / "folder_b" / "file2.txt"
# file_path.touch()
# print(file_path.exists())
# file_path.touch()
# print(file_path.exists())
# print(file_path.is_file())

# Iterating over directory contents

# for path in new_dir.iterdir():
#     print(path)
#
# print(list(new_dir.iterdir()))

#searching for files in directory
# .glob


# for path in new_dir.glob("*.txt"):
#     print(path)

# paths =[
#     new_dir / "program1.py",
#     new_dir / "program2.py",
#     new_dir / "folder_a" / "program3.py",
#     new_dir / "folder_a" / "folder_b" / "image1.jpg",
#     new_dir / "folder_a" / "folder_b" / "image2.png",
# ]

# for path in paths:
#     path.touch()
# #
# print(list(new_dir.glob("*.py")))
# print(list(new_dir.glob("*1*")))
# print(list(new_dir.glob("1*")))
# print(list(new_dir.glob("program?.py")))
# print(list(new_dir.glob("?older_?")))
# print(list(new_dir.glob("*1.??")))
# print(list(new_dir.glob("program[12].py")))
# print(list(new_dir.glob("**/*.txt")))
# print(list(new_dir.glob("**/*.py")))
# print(list(new_dir.rglob("*.py")))


#MOVING AND DELETING FILES

# source = new_dir / "file1.txt"
# destination = new_dir / "folder_a" / "file1.txt"
# source.replace(destination)

# source = new_dir / "folder_b"
# destination = new_dir / "folder_c"
# # print(source.replace(destination))
#
# file_path= new_dir / "program1.py"
# file_path.unlink()
#
# import shutil
# folder_a = new_dir / "folder_a"
# shutil.rmtree(folder_a)
# folder_a.exists()

# exercises

from pathlib import Path

new_dir = Path.home() / "my_folder"


file1 = new_dir / "file1.txt"
file2 = new_dir / "file2.txt"
image1 = new_dir / "image1.png"

file1.touch()
file2.touch()
image1.touch()

images_dir = new_dir /"images"
image1.replace(images_dir / "image1.png")

file1.unlink()

import shutil

shutil.rmtree(new_dir)