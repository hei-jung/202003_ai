
def insertion_sort(list):
    i = 1
    for i in range(i, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and list[j] > key:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    return list

list = [9, 4, 3, 1, 12]
print(insertion_sort(list))