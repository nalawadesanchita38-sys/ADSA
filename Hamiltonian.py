def hamiltonian(graph, path, pos, n):
    if pos == n:
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        return False

    for v in range(1, n):
        if graph[path[pos - 1]][v] == 1 and v not in path:
            path[pos] = v

            if hamiltonian(graph, path, pos + 1, n):
                return True

            path[pos] = -1

    return False


n = int(input("Enter number of vertices: "))
graph = []

print("Enter adjacency matrix:")
for i in range(n):
    graph.append(list(map(int, input().split())))

path = [-1] * n
path[0] = 0

if hamiltonian(graph, path, 1, n):
    print("Hamiltonian Cycle exists:")
    print(*(path + [path[0]]))
else:
    print("Hamiltonian Cycle does not exist")
