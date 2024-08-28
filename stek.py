class Stack:
    def __init__(self):
        # Инициализируем пустой список для хранения элементов стека
        self.items = []

    def is_empty(self):
        # Проверяем, пуст ли стек
        return len(self.items) == 0

    def push(self, item):
        # Добавляем элемент в конец списка (вверх стека)
        self.items.append(item)

    def pop(self):
        # Удаляем и возвращаем последний элемент из списка (верх стека)
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        # Возвращаем последний элемент из списка без удаления
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        # Возвращаем количество элементов в стеке
        return len(self.items)

    def __str__(self):
        # Возвращаем строковое представление стека
        return str(self.items)

# Пример использования стека
stack = Stack()

# Добавляем элементы в стек
stack.push(1)
stack.push(2)
stack.push(3)

print("Стек после добавления элементов:", stack)

# Получаем верхний элемент стека
print("Верхний элемент стека:", stack.peek())

# Удаляем элемент из стека
print("Удалённый элемент:", stack.pop())

# Проверяем состояние стека
print("Стек после удаления элемента:", stack)

# Проверяем размер стека
print("Размер стека:", stack.size())