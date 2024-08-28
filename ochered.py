class Queue:
    def __init__(self):
        # Инициализируем пустой список для хранения элементов очереди
        self.items = []

    def is_empty(self):
        # Проверяем, пуста ли очередь
        return len(self.items) == 0

    def enqueue(self, item):
        # Добавляем элемент в конец списка (в конец очереди)
        self.items.append(item)

    def dequeue(self):
        # Удаляем и возвращаем первый элемент из списка (из начала очереди)
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        # Возвращаем первый элемент из списка без удаления
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from empty queue")

    def size(self):
        # Возвращаем количество элементов в очереди
        return len(self.items)

    def __str__(self):
        # Возвращаем строковое представление очереди
        return str(self.items)

# Пример использования очереди
queue = Queue()

# Добавляем элементы в очередь
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Очередь после добавления элементов:", queue)

# Получаем первый элемент очереди
print("Первый элемент очереди:", queue.peek())

# Удаляем элемент из очереди
print("Удалённый элемент:", queue.dequeue())

# Проверяем состояние очереди
print("Очередь после удаления элемента:", queue)

# Проверяем размер очереди
print("Размер очереди:", queue.size())