def quick_sort(list):
    if len(list) <= 1:    return list
    pivot = list[len(list)//2]
    g1, mid, g2 = [], [], []

    for i in list:
        if i < pivot:   g1.append(i)
        elif i > pivot: g2.append(i)
        else:   mid.append(i)
    return quick_sort(g1) + mid + quick_sort(g2)

list = [6,8,3,9,10,1,2,4,7,5]
print(quick_sort(list))
