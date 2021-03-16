from minimum_cost_flow import min_cost_flow
from maximum_flow import Dinic


def bipartite_matching(bigraph):
    nx = len(bigraph)
    ny = 0
    for x in range(nx):
        for y in bigraph[x]:
            ny = max(ny, y + 1)
    graph = [{} for _ in range(nx + ny + 2)]
    for x in range(nx):
        graph[0][x + 1] = 1
        graph[x + 1][0] = 0
    for x in range(nx):
        for y in bigraph[x]:
            graph[x + 1][y + nx + 1] = 1
            graph[y + nx + 1][x + 1] = 0
    for y in range(ny):
        graph[y + nx + 1][nx + ny + 1] = 1
        graph[nx + ny + 1][y + nx + 1] = 0
    return Dinic(graph, 0, nx + ny + 1).max_flow()


def weighted_bipartite_matching(bigraph):
    nx = len(bigraph)
    ny = 0
    max_weight = 0
    for x in range(nx):
        for y in bigraph[x]:
            ny = max(ny, y + 1)
            max_weight = max(max_weight, bigraph[x][y])
    graph = [{} for _ in range(nx + ny + 2)]
    for x in range(nx):
        graph[0][x + 1] = (1, 0)
        graph[x + 1][0] = (0, 0)
    for x in range(nx):
        for y in bigraph[x]:
            graph[x + 1][y + nx + 1] = (1, max_weight - bigraph[x][y])
            graph[y + nx + 1][x + 1] = (0, bigraph[x][y] - max_weight)
    for y in range(ny):
        graph[y + nx + 1][nx + ny + 1] = (1, 0)
        graph[nx + ny + 1][y + nx + 1] = (0, 0)
    capa_graph = [{} for _ in range(nx + ny + 2)]
    for x in range(nx + ny + 2):
        for y in graph[x]:
            capa, _ = graph[x][y]
            capa_graph[x][y] = capa
    max_flow = Dinic(capa_graph, 0, nx + ny + 1).max_flow()
    min_cost = min_cost_flow(graph, 0, nx + ny + 1, max_flow)
    return max_flow * max_weight - min_cost
