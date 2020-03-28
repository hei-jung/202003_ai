
def selection_sort(list):
    for i in range(len(list)-1):
        least = i
        for j in range(i+1, len(list)):
            if list[j] < list[least]:
                least = j
        list[i], list[least] = list[least], list[i]
    return list

list = [9, 4, 3, 1, 12]
print(selection_sort(list))