from typing import List


def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]: # Accepted on Leetcode
    if not edges:
        return list(range(n))

    in_degree = [0] * n
    graph: List[List[int]] = [[] for _ in range(n)]

    for edge in edges:
        in_degree[edge[0]] += 1
        in_degree[edge[1]] += 1

        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    queue = []
    for index, degree in enumerate(in_degree):
        if degree == 1:
            queue.append(index)

    while any(num not in (0, 1) for num in in_degree) or in_degree.count(1) >= 3:
        temp = []
        while queue:
            node = queue.pop(0)
            in_degree[node] -= 1

            for child in graph[node]:
                in_degree[child] -= 1
                graph[child].remove(node)

                if in_degree[child] == 1:
                    temp.append(child)

            graph[node] = []
        queue = temp

    return queue


if __name__ == "__main__":
    print(findMinHeightTrees(1, []))
