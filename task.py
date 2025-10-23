def selection_sort(arr):
   
    n = len(arr)
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]

    return arr
my_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(my_list)
print(my_list)