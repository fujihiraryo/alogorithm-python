INF = 1 << 30


def minimum_cost_flow(graph, start, goal, flow):
    n = len(graph)
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
                for j in graph[i].keys():
                    capa, cost = graph[i][j]
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
            capa, _ = graph[last[x]][x]
            min_capa = min(min_capa, capa)
            x = last[x]
        residual_flow -= min_capa
        min_cost += min_capa * path_cost[goal]
        # update graph
        x = goal
        while x != start:
            capa, cost = graph[last[x]][x]
            graph[last[x]][x] = (capa - min_capa, cost)
            capa, cost = graph[x][last[x]]
            graph[x][last[x]] = (capa + min_capa, cost)
            x = last[x]
    return min_cost
