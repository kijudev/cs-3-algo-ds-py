# @author Jakub Kijek
# @date 2026.10.22


def heapify(list, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and list[left] > list[largest]:
        largest = left

    if right < n and list[right] > list[largest]:
        largest = right

    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        heapify(list, n, largest)

def heapsort(list):
    n = len(list)

    for i in range(n // 2 - 1, -1, -1):
        heapify(list, n, i)

    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heapify(list, i, 0)
    

list = [4, 5, 6, 1, 3, 2]
print(f"list:   {list}")
heapsort(list)
print(f"sorted: {list}")


