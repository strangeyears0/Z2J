# Creating patho objects from strings

import pathlib

path = pathlib.Path("/Users/David/Documents/hello.txt")

# path = pathlib.Path("C:\Users\David\Desktop\hello.txt")
path = pathlib.Path("C:/Users/David/Desktop/hello.txt")
path = pathlib.Path(r"C:\Users\David\Desktop\hello.txt")


home = pathlib.Path.home()
print(home)
print(pathlib.Path.cwd())
print (home / "Desktop" / "hello.txt")