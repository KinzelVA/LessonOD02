def insertion_sort(arr):
    # Проходим по всему массиву начиная со второго элемента
    for i in range(1, len(arr)):
        key = arr[i]
        # Перемещаем элементы arr[0..i-1], которые больше, чем key,
        # на одну позицию вперёд от их текущего положения
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Произвольн��й числовой ряд для сортировки
arr = [12, 11, 13, 5, 6]

insertion_sort(arr)

print("Отсортированный массив:")
for i in arr:
    print(i, end=" ")