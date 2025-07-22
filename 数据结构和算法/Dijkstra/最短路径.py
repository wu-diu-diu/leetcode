import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}  # 用于路径追踪
    distances[start] = 0

    priority_queue = [(0, start)]  # (距离, 节点)

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prev[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, prev

def reconstruct_path(prev, end):
    path = []
    while end is not None:
        path.append(end)
        end = prev[end]
    return path[::-1]  # 从起点到终点

# 定义图（无向图）
graph = {
    1: [(2, 2), (4, 6)],       # A: B(2), D(6)
    2: [(1, 2), (3, 3), (4, 2)], # B: A(2), C(3), D(2)
    3: [(2, 3), (4, 2)],       # C: B(3), D(2)
    4: [(1, 6), (2, 2), (3, 2)]  # D: A(6), B(2), C(2)
}

start = 1  # A节点
distances, prev = dijkstra(graph, start)