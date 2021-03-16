def min_cost_flow(graph, start, goal, flow, INF=1 << 30):
    n = len(graph)
    residual_graph = [{} for _ in range(n)]
    for x in range(n):
        for y in graph[x]:
            residual_graph[x][y] = graph[x][y]
    residual_flow = flow
    min_cost = 0
    while residual_flow:
        # find path
        path_cost = [INF] * n
        path_cost[start] = 0
        last = [None] * n
        update = True
        while update:
            update = False
            for i in range(n):
                if path_cost[i] == INF:
                    continue
                for j in residual_graph[i].keys():
                    capa, cost = residual_graph[i][j]
                    if capa > 0 and path_cost[j] > path_cost[i] + cost:
                        path_cost[j] = path_cost[i] + cost
                        last[j] = i
                        update = True
        if path_cost[goal] == INF:
            return -1
        # min capacity
        min_capa = residual_flow
        x = goal
        while x != start:
            capa, _ = residual_graph[last[x]][x]
            min_capa = min(min_capa, capa)
            x = last[x]
        residual_flow -= min_capa
        min_cost += min_capa * path_cost[goal]
        # update graph
        x = goal
        while x != start:
            capa, cost = residual_graph[last[x]][x]
            residual_graph[last[x]][x] = (capa - min_capa, cost)
            capa, cost = residual_graph[x][last[x]]
            residual_graph[x][last[x]] = (capa + min_capa, cost)
            x = last[x]
    return min_cost
