def selection_sort(arr):
    # Проходим по всему массиву
    for i in range(len(arr)):
        # Находим минимальный элемент в оставшейся неотсортированной части массива
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Меняем местами найденный минимальный элемент с первым элементом в неотсортированной части
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Произвольный числовой ряд для сортировки
arr = [64, 25, 12, 22, 11]

selection_sort(arr)

print("Отсортированный массив:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")