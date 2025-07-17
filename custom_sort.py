def custom_sort(arr):
    arr.sort(key=lambda x: x[1]-x[0])
    return arr

a=[(1, 3), (2, 1), (3, 6)]
print(custom_sort(a))