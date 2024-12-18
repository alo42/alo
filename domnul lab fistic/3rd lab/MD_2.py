def findCheapestPrice(n, flights, start, destination, k):
    graph = {}
    for flight in flights:
        if flight[0] not in graph:
            graph[flight[0]] = []
        graph[flight[0]].append((flight[1], flight[2]))

    def dfs(city, stops, cost):
        nonlocal min_cost

        if city == destination:
            min_cost = min(min_cost, cost)
            return

        if stops > k:
            return

        if city not in graph:
            return

        for neighbor, price in graph[city]:
            dfs(neighbor, stops + 1, cost + price)

    min_cost = float('inf')
    dfs(start, 0, 0)

    return min_cost if min_cost != float('inf') else "no route"

# Example 1
n1 = 4
flights1 = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
start1 = 0
destination1 = 3
k1 = 1
output1 = findCheapestPrice(n1, flights1, start1, destination1, k1)
print(output1)  # Output: 700

# Example 2
n2 = 3
flights2 = [[0,1,100],[1,2,100],[0,2,500]]
start2 = 0
destination2 = 2
k2 = 1
output2 = findCheapestPrice(n2, flights2, start2, destination2, k2)
print(output2)  # Output: 200

# Example 3
n3 = 3
flights3 = [[0,1,100],[1,2,100],[0,2,500]]
start3 = 0
destination3 = 2
k3 = 0
output3 = findCheapestPrice(n3, flights3, start3, destination3, k3)
print(output3)  # Output: 500
