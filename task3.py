import heapq


# Функція для алгоритму Дейкстри
def dijkstra(graph: dict, start: str) -> dict:
    # Ініціалізуємо мін-купу
    heap = []

    # Словник для збереження найкоротших відстаней до кожної вершини
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Додаємо початкову вершину в купу
    heapq.heappush(heap, (0, start))

    while heap:
        # Витягуємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(heap)

        # Якщо відстань більше вже відомої мінімальної, пропускаємо цю вершину
        if current_distance > distances[current_vertex]:
            continue

        # Оновлюємо відстані для сусідів
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Якщо знайшли коротший шлях до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


# Створення зваженого графа у вигляді словника
graph = {
    'A': [('B', 11), ('C', 7)],
    'B': [('A', 18), ('C', 21), ('D', 5)],
    'C': [('A', 90), ('B', 3), ('D', 11)],
    'D': [('B', 51), ('C', 15)]
}

# Запуск алгоритму Дейкстри від початкової вершини 'A'
start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

print(f"Найкоротші шляхи від вершини {start_vertex}:")
for vertex, distance in shortest_paths.items():
    print(f"Відстань до {vertex}: {distance}")
