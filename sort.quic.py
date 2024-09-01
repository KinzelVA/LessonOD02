def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Выбираем опорный элемент
        pivot = arr[len(arr) // 2]
        # Элементы меньше опорного
        left = [x for x in arr if x < pivot]
        # Элементы равные опорному
        middle = [x for x in arr if x == pivot]
        # Элементы больше опорного
        right = [x for x in arr if x > pivot]
        # Рекурсивно применяем быструю сортировку к спискам меньше и больше опорного, и объединяем результаты
        return quick_sort(left) + middle + quick_sort(right)

# Произвольный числовой ряд для сортировки
arr = [3, 6, 8, 10, 1, 2, 1]

sorted_arr = quick_sort(arr)

print("Отсортированный массив:")
print(sorted_arr)