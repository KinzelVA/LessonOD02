class Graph:
    def __init__(self):
        # Инициализируем пустой словарь для хранения графа
        self.graph = {}

    def add_vertex(self, vertex):
        # Добавляем вершину в граф, если её ещё нет
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Добавляем ребро между двумя вершинами
        # Если вершины не существуют, добавляем их
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)

        # Добавляем vertex2 в список смежных вершин vertex1
        self.graph[vertex1].append(vertex2)
        # Для неориентированного графа добавляем vertex1 в список смежных вершин vertex2
        self.graph[vertex2].append(vertex1)

    def get_vertices(self):
        # Возвращаем список всех вершин в графе
        return list(self.graph.keys())

    def get_edges(self):
        # Возвращаем список всех рёбер в графе
        edges = []
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if {neighbor, vertex} not in edges:
                    edges.append({vertex, neighbor})
        return edges

    def __str__(self):
        # Возвращаем строковое представление графа
        return str(self.graph)


# Пример использования графа
graph = Graph()

# Добавляем вершины
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")

# Добавляем рёбра
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")

print("Граф:", graph)

# Получаем список вершин
print("Вершины графа:", graph.get_vertices())

# Получаем список рёбер
print("Рёбра графа:", graph.get_edges())