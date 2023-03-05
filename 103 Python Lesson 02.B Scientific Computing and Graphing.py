# 17.1 Use NumPy for Matrix Manipulation
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[0][1])
#
# for row in matrix:
#     for i in range(len(row)):
#         row[i] = row[i]*2
# print(matrix)
# CREATE A NUMPY ARRAY

import numpy as np
# # matrix = np.array([[1,2,3,],[4,5,6],[7,8,9]])
# # print(matrix)
# # print(matrix[0][1])
# # print(matrix[0,1])
# matrix = np.array([
#     [[1,2,3],[4,5,6]],
#     [[7,8,9],[10,11,12]],
#     [[13,14,15],[16,17,18]]
# ])
# print(matrix[0,1,2])

# ARRAY OPERATIONS

# A = np.array([[1,2,3],[4,5,6],[7,8,9]])
# multiple = 2*A
# # print(multiple)
#
# B = np.array([[5,4,3],[7,6,5],[9,8,7]])
#
# C = B - A
# print(C)
#
# A = np.array([[1,1,1],[1,1,1],[1,1,1]])
# multi=A*A
# print(multi)
# monk=A@A
# print(monk)

# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
#
# print(matrix.shape)
# print(matrix.diagonal())
# print(matrix.flatten())
# print(matrix.transpose())
# print(matrix.min())
# print(matrix.max())
# print(matrix.mean())
# print(matrix.sum())

# Stacking and Shaping Arrays

# A = np.array([[1,2,3],[4,5,6]])
# B = np.array([[7,8,9],[10,11,12]])
#
# print(np.vstack([A,B]))
# print(np.hstack([A,B]))
# print(A.reshape(6,1))

# nums = np.arange(1,10)
# print(nums)
# matrix = nums.reshape(3,3)
# print(matrix)
#
# print(np.arange(1,10).reshape(3,3))
#
# print(np.arange(1,13).reshape(3,2,2))

# arr = np.array([1,3,5,7,9,11,13,15,17,19,21,23])
# print(arr.reshape(3,2,2))

# print(np.arange(1,24,2).reshape(3,2,2))

#ex1

# import numpy as np
#
# first_matrix = np.arange(3,12).reshape(3,3)
# # ex2
# print(f"Min is {first_matrix.min()}")
# print(f"Max is {first_matrix.max()}")
# print(f"Mean is {first_matrix.mean()}")
# # ex3
# second_matrix = first_matrix**2
# #ex4
# third_matrix = np.vstack([first_matrix, second_matrix])
# # ex5
# print(third_matrix @ first_matrix)
# # ex6
# third_matrix = third_matrix.reshape(3,3,2)
# print(third_matrix)

# 17.2 Use matplotlib for plotting graphs

# from matplotlib import pyplot as plt
#
# plt.plot([1,2,3,4,5])
# plt.show()

# xs = [1,2,3,4,5]
# ys = [2,4,6,8,10]
# plt.plot(xs,ys)
# plt.show()

# xs = [1,2,3,4,5]
# ys = [3,-1,4,0,6]
# plt.plot(xs,ys)
# plt.show()

# plt.plot([2,4,6,8,10],"g-o")
# plt.show()

#plot multiple graphs in the same window

# plt.plot([1,2,3,4,5])
# plt.plot([1,2,4,8,16])
# plt.show()

# plt.plot([1,2,3,4,5],"g-o")
# plt.plot([1,2,4,8,16],"b-^")
# plt.show()

#plot data from numpy arrays

# from matplotlib import pyplot as plt
# import numpy as np

# array = np.arange(1,6)
# plt.plot(array)
# plt.show()

# data = np.arange(1,21).reshape(5,4)
# plt.plot(data)
# plt.show()

# data = np.arange(1,21).reshape(5,4)
# plt.plot(data.transpose())
# plt.show()

#format your plots to perfection
# from matplotlib import pyplot as plt
# import numpy as np
# days = np.arange(0,21)
# other_site, real_python = days,days **2
#
# plt.plot(days,other_site)
# plt.plot(days,real_python)
# plt.xticks([0,5,10,15,20])
# plt.xlabel("Days of Reading")
# plt.ylabel("Amount of Python Learned")
# plt.title("Python Learned Reading Real Python vs Other Site")
# plt.legend(["Other Site","Real Python"])
# plt.show()

# Other types of plots
#bar charts

from matplotlib import pyplot as plt
from numpy import random
# centers = [1,2,3,4,5]
# tops = [2,4,6,8,10]
#
# plt.bar(centers,tops)
# plt.show()

# centers = np.arange(1,6)
# tops = np.arange(2,12,2)
#
# plt.bar(centers,tops)
# plt.show()
#
# fruits = {
#     "apples":10,
#     "oranges":16,
#     "bananas":9,
#     "pears":4,
# }
# plt.bar(fruits.keys(),fruits.values())
# plt.show()

#histograms
# plt.hist(random.randn(10000),20)
# plt.show()
#Save as figures as images
#
# xs = np.arange(1,6)
# tops = np.arange(2,12,2)
#
# plt.bar(xs, tops)
# plt.savefig("bar.png")

#Works with plots interactivity
