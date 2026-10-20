# @author Jakub Kijek
# @date 2026.10.20

def bubblesort(list):
    for i in range(1, len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

list = [4, 5, 6, 1, 3, 2]
print(f"list:   {list}")

bubblesort(list)
print(f"sorted: {list}")

