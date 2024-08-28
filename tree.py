class Node:
    def __init__(self, data):
        # Инициализируем узел с данными и без потомков
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        # Инициализируем пустое дерево
        self.root = None

    def insert(self, data):
        # Вставляем новый узел в дерево
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursively(self.root, data)

    def _insert_recursively(self, node, data):
        # Рекурсивно вставляем узел в дерево
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursively(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursively(node.right, data)

    def inorder_traversal(self, node):
        # Обход дерева в порядке (in-order)
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.data, end=' ')
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        # Обход дерева в прямом порядке (pre-order)
        if node is not None:
            print(node.data, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        # Обход дерева в обратном порядке (post-order)
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end=' ')

# Пример использования бинарного дерева
tree = BinaryTree()

# Вставляем узлы в дерево
nodes = [7, 3, 9, 1, 5, 8, 10]
for node in nodes:
    tree.insert(node)

print("In-order обход:")
tree.inorder_traversal(tree.root)
print("\nPre-order обход:")
tree.preorder_traversal(tree.root)
print("\nPost-order обход:")
tree.postorder_traversal(tree.root)