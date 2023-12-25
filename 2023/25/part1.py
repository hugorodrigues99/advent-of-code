import networkx

def solve(filename):
    input = open(filename, 'r').read().splitlines()

    graph = networkx.Graph()

    for line in input:
        components = line.split(" ")
        source = components[0][:-1]

        for neighbor in components[1:]:
            graph.add_edge(source, neighbor)
            graph.add_edge(neighbor, source)

    edges_to_remove = networkx.minimum_edge_cut(graph)
    graph.remove_edges_from(edges_to_remove)
    c1, c2 = networkx.connected_components(graph)

    return (len(c1) * len(c2))

res_test = solve("test.txt")
print(res_test)

res_final = solve("puzzle.txt")
print(res_final)
