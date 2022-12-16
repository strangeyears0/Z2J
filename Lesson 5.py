# 8COndittional logic and control flow

# 8.1 Compare Values

# Boolean operators:
#
# <
# >
# >=
# <=
# !=
# ==
#

#exercises1

# print(1 <= 1)
# print(1 != 1)
# print(1 != 2)
# print('good' != "bad")
# print("good" != "Good")
# print(123 == "123")
#
# # ex2.

# print(3 != 4)
# print(10 > 5)
# print("jack" != "jill")
# print(42 != "42")


#8.2 Add some logic

# AND
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)


# OR
# print(True or True)
# print(True or False)
# print(False or True)
# # print(False or False)

# NOT
#
# print(not True)
# print(not False)

# Building complex EXPRESSIONS
# print(True and not (1 != 1))
#
# print(("A" != "A") or not (2 >=3 ))
#
# print(True and False == True and False)
# print((True and False) == (True and False))

#exercises1
# print((1 <= 1) and(1 != 1))
# print(not(1 != 2))
# print(("good" != "bad") or False)
# print(("good" != "Good") and not (1 == 1))

#exercises2

# print(False == (not True))
# print((True and False) == (True and False))
# print(not (True and "A" == "B"))


#8.3 Control the flow of your programms
# the IF statement
#
# if 2+2 == 4:
#     print("2 and 2 is 4")
#
# grade = 50
# if grade >= 70:
#     print("You passed")
# if grade < 70:
#     print("Tou not passed")
# print("This your for attendig")

# else keyword

grade = 40

if grade >= 70:
    print("you passed")
else:
    print("you dont pass")
print("No elo")
