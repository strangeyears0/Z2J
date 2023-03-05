list1 = []
list2 = [1,2,5,3,1,7,9,1,12,83,1,5,3,2]
list3 = [1,1,1,1,1,1,1,2,1,1,1]
list4 = [2,2,2,2]
list5 = [1,2]
list6 = [2,1]


def bubble_sort(list):

    for i in range(len(list)-1):
        for x in range(len(list)-1 -i):
            if list[x] > list[x+1]:
                list[x], list[x+1] = list[x+1], list[x]
    return list,print(list)

bubble_sort(list1)
bubble_sort(list2)
bubble_sort(list3)
bubble_sort(list4)
bubble_sort(list5)
bubble_sort(list6)