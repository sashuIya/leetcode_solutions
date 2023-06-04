from pprint import pprint

def dfs(v, t, cf, used, min_cf, min_cf_final):
    used[v] = True

    if v == t:
        min_cf_final[0] = min_cf
        return True

    for (v_u_index, (u, c, u_v_index)) in enumerate(cf[v]):
        if c <= 0: continue
        if used[u]: continue

        if dfs(u, t, cf, used, min(min_cf, c), min_cf_final):
            cf[v][v_u_index][1] -= min_cf_final[0]
            cf[u][u_v_index][1] += min_cf_final[0]
            return True

    return False


# u: [(v, c), ...]
def max_flow(s, t, n, edges):
    cf = dict()
    for (u, u_edges) in edges.items():
        for (v, c) in u_edges:
            if u not in cf:
                cf[u] = []
            if v not in cf:
                cf[v] = []
            cf[u].append([v, c, len(cf[v])]) # [v, max flow u->v, link to opposite edge v->u]
            cf[v].append([u, 0, len(cf[u]) - 1]) # [u, max flow v->u, link to opposite edge v->u]

    pprint(cf)
    
    result = 0
    min_cf_final = [1e9]
    used = [False] * n
    while dfs(s, t, cf, used, 1e9, min_cf_final):
        result += min_cf_final[0]
        min_cf_final[0] = 1e9
        used = [False] * n
        pprint(cf)

    print('max flow: {}'.format(result))

    
edges = {
        0: [(1, 16), (2, 13)],
        1: [(2, 10), (3, 12)],
        2: [(4, 14), (1, 4)],
        3: [(2, 9), (5, 20)],
        4: [(3, 7), (5, 4)]
        }

max_flow(0, 5, 6, edges)
