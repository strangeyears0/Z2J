# Creating patho objects from strings
#
import csv
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

# from pathlib import Path
#
# new_dir = Path.home() / "my_folder"
#
#
# file1 = new_dir / "file1.txt"
# file2 = new_dir / "file2.txt"
# image1 = new_dir / "image1.png"
#
# file1.touch()
# file2.touch()
# image1.touch()
#
# images_dir = new_dir /"images"
# image1.replace(images_dir / "image1.png")
#
# file1.unlink()
#
# import shutil
#
# shutil.rmtree(new_dir)

# 12.4 Challenge

# from pathlib import Path
# #
# #
# # documents_dir = Path.cwd() / "practice_files" / "documents"
# #
# # images_dir = Path.home() / "images"
# # images_dir.mkdir(exist_ok=True)
# #
# # for path in documents_dir.rglob("*.*"):
# #     if path.suffix.lower() in [".png", ".jpg", ".gif"]:
# #         path.replace(images_dir / path.name)

# 12..5 writing and reading file
from pathlib import Path
# path = Path.home() / "hello.txt"
# path.touch()
# file = path.open(mode = "r", encoding = "utf-8")
#
# print(file)
# file.close()

# file_path = "C:/Users/Ja/hello.txt"
#
# file = open(file_path, mode ="r", encoding="utf-8")
# print(file)
# file.close()
#
# with statemant

# from pathlib import Path
# path = Path.home() / "hello.txt"
# path.touch()
# file = path.open(mode = "r", encoding = "utf-8")
# #
# # # with path.open(mode = "r", encoding = "utf-8") as file:
# # #     text= file.read()
# # # print(text)
# # with path.open(mode = "r", encoding = "utf-8") as file:
# #     for line in file.readlines():
# #         print(line, end = "")
#
# #Writing file
#
#
# with path.open(mode = "w", encoding = "utf-8") as file:
#     file.write("Hi there!")
#
# with path.open(mode = "r", encoding = "utf-8") as file:
#     text= file.read()
# print(text)
#
#
# # append
#
# with path.open(mode = "a", encoding = "utf-8") as file:
#     file.write("\nNext line")
#
#
# with path.open(mode = "r", encoding = "utf-8") as file:
#     text= file.read()
# print(text)
#
# lines_of_text = ["Hello line1\n",
#                  "Hello line2\n",
#                  "Hello line3\n",
#                  ]
# with path.open(mode ="w", encoding= "utf-8") as file:
#     file.writelines(lines_of_text)
#
# with path.open(mode = "r", encoding = "utf-8") as file:
#     text= file.read()
# print(text)
#
# path = Path.home() / "new_file.txt"
# with path.open(mode = "w", encoding = "utf-8") as file:
#     file.write("Hello")
#
# with path.open(mode = "r", encoding = "utf-8") as file:
#     text= file.read()
# print(text)
#


# ex1.

# from pathlib import Path
#
# starships = ["Discovery\n", "Enterprise\n","Defiant\n","Voyager"]
#
# file_path = Path.home() / "starships.txt"
#
# with file_path.open(mode="w", encoding="utf-8") as file:
#     file.writelines(starships)
#
# # ex2.
#
# with file_path.open(mode="r", encoding= "utf-8") as file:
#     for starships in file.readlines():
#         print(starships, end ="\n")
#
# # ex3.
#
# with file_path.open(mode = "r", encoding = "utf-8") as file:
#     for starship in file.readlines():
#         if starship.startswith("D"):
#             print(f"\n{starship}", end= "")

# 12.6 READ AND WRITE CSV Data

# temperature_readings = [68, 65, 68, 70, 74, 72]
#
# from pathlib import Path
#
# file_path = Path.home() / "temperatures.csv"
#
# with file_path.open(mode = "a" , encoding = "utf-8") as file:
#     file.write(str(temperature_readings[0]))
#     for temp in temperature_readings[1:]:
#         file.write(f",{temp}")
# with file_path.open(mode = "r", encoding = "utf-8") as file:
#     text = file.read()
# print(text)
#
# temperatures = text.split(",")
# print(temperatures)
#
# int_temperatures = [int(temp) for temp in temperatures]
# print(int_temperatures)
#
# from pathlib import Path
# import csv
# daily_temperatures = [
#     [68, 65, 68, 70, 74, 72],
#     [67, 67, 70, 72, 72, 70],
#     [68, 70, 74, 76, 74, 73]
# ]
#
# file_path = Path.home() / "temperatures.csv"
# file = file_path.open(mode = "w", encoding = "utf-8", newline="")
#
# writer = csv.writer(file)
#
# for temp_list in daily_temperatures:
#     writer.writerow(temp_list)
# file.close()
#
# file = file_path.open(mode = "r", encoding = "utf-8", newline = "")
# reader = csv.reader(file)
#
# for row in reader:
#     print(row)
# file.close()


# exercise 1

import csv
from pathlib import Path

# numbers = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
# ]
#
# file_path = Path.home() / "numbers.csv"
#
# with file_path.open(mode = "w", encoding= "utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerows(numbers)
#
# # ex2/
#
# numbers = []
#
# with file_path.open(mode="r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         int_row = [int(num) for num in row]
#         numbers.append(int_row)
# print(numbers)

# ex3

favorite_colors = [
    {"name":"Joe","favorite_color":"blue"},
    {"name":"Anne","favorite_color":"green"},
    {"name":"Bailey","favorite_color":"red"},
]

file_path = Path.home() / "favorite_colors.csv"

with file_path.open(mode = "w",encoding = "utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name","favorite_color"])
    writer.writeheader()
    writer.writerows(favorite_colors)

# ex4

favorite_colors = []

with file_path.open(mode = "r", encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        favorite_colors.append(row)
print(favorite_colors)