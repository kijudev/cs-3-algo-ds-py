# @author Jakub Kijek
# @date 2026.10.22


def insertsort(list):
    for i in range(1, len(list)):
        idx = i
        val = list[i]

        for j in range(i - 1, -1, -1):
            if list[j + 1] > val:
                list[j + 1] = list[j]
                idx = j
            else:
                break

        list[idx] = val
    

list = [4, 5, 6, 1, 3, 2]
print(f"list:   {list}")
insertsort(list)
print(f"sorted: {list}")


