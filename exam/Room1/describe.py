def describe():
    file_path = "D:/Z2J/exam/Room1/describe.txt"
    file = open(file_path, mode = "r", encoding= "utf-8")
    for line in file:
        print(line)

