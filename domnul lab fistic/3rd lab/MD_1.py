def canFinish(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    for edge in prerequisites:
        graph[edge[0]].append(edge[1])

    status = [0] * numCourses

    def dfs(node):
        status[node] = 1

        for neighbor in graph[node]:
            if status[neighbor] == 0:
                if not dfs(neighbor):
                    return False
            elif status[neighbor] == 1:
                return False

        status[node] = 2
        return True

    for node in range(numCourses):
        if status[node] == 0:
            if not dfs(node):
                return False
    return True


numCourses1 = 2
prerequisites1 = [[1, 0]]
print(canFinish(numCourses1, prerequisites1))

numCourses2 = 2
prerequisites2 = [[1, 0], [0, 1]]
print(canFinish(numCourses2, prerequisites2))
