import math
def floyd_warshall(graph):
    n = len(graph)
    # stepping loop
    for k in range(n):
        # outer loop
        for i in range(n):
            # inner loop
            for j in range(n):
                # replace direct path with path through k if direct path is longer
                if i != j:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                else:
                    graph[i][j] = 0
        print('\n \n \nD',k+1,':')
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if graph[i][j]==sys.maxsize:
                    print(math.inf, end=" ")
                else:
                    print(graph[i][j],end=" ")
            print()
