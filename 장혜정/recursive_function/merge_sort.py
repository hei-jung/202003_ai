def merge_sort(list):
    if len(list)<=1:    return list
    m = len(list)//2
    g1 = list[:m]
    g2 = list[m:]
    g1 = merge_sort(g1)
    g2 = merge_sort(g2)
    return merge(g1, g2)

def merge(g1, g2):
    result = []
    while len(g1) > 0 or len(g2) > 0:
        if len(g1) > 0 and len(g2) > 0:
            if g1[0] <= g2[0]:
                result.append(g1[0])
                g1 = g1[1:]
            else:
                result.append(g2[0])
                g2 = g2[1:]
        elif len(g1) > 0:
            result.append(g1[0])
            g1 = g1[1:]
        elif len(g2) > 0:
            result.append(g2[0])
            g2 = g2[1:]
    return result

list = [6,8,3,9,10,1,2,4,7,5]
print(merge_sort(list))