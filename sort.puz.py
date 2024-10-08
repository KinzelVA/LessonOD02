def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Последние i элементов уже на месте
        for j in range(0, n-i-1):
            # Проходим по массиву от начала до n-i-1
            # Меняем элементы местами, если они идут в неправильном порядке
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Произвольный числовой ряд для сортировки
arr = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(arr)

print("Отсортированный массив:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")