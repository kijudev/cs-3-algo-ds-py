# @author Jakub Kijek
# @date 2026.10.20

def mergesort(list):
    if len(list) <= 1: return list
    if len(list) == 2:
        if list[0] < list[1]: return list
        return list[::-1]
    
    mid = len(list) // 2
    left = mergesort(list[:mid])
    right = mergesort(list[mid:])

    result = []
    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        elif left[l] >= right[r]:
            result.append(right[r])
            r += 1

    if l == len(left): result.extend(right[r:])
    else: result.extend(left[l:])

    return result
    

list = [4, 5, 6, 1, 3, 2]
print(f"list:   {list}")

list = mergesort(list)
print(f"sorted: {list}")

