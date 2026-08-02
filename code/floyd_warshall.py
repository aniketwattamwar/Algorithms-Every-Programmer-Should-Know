def floyd_warshall(graph):
    """
    Executes the Floyd-Warshall algorithm to find all-pairs shortest paths.
    
    Args:
        graph (list of lists): The initial adjacency matrix representing the graph. 
                               Use float('inf') for disconnected nodes.
                               
    Returns:
        list of lists: A 2D array containing the shortest distances between all pairs.
    """
    V = len(graph)
    
    dist = [[float('inf') for _ in range(V)] for _ in range(V)] #A
    
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j] #B
            
    for k in range(V): #C
        for i in range(V): #D
            for j in range(V): #E
                
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    
                    if dist[i][k] + dist[k][j] < dist[i][j]: #F
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
    return dist

if __name__ == "__main__":
    INF = float('inf')
    
    # Example 1: 4 nodes graph from standard examples
    graph1 = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]
    print("Example 1 Output:")
    res1 = floyd_warshall(graph1)
    for row in res1:
        print(row)
    print()
        
    # Example 2: Graph with negative weights (no negative cycles)
    graph2 = [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
    ]
    print("Example 2 Output:")
    res2 = floyd_warshall(graph2)
    for row in res2:
        print(row)
    print()
    
    # Example 3: Disconnected components
    graph3 = [
        [0, 2, INF, INF],
        [INF, 0, INF, INF],
        [INF, INF, 0, 3],
        [INF, INF, INF, 0]
    ]
    print("Example 3 Output:")
    res3 = floyd_warshall(graph3)
    for row in res3:
        print(row)
    print()

    # Example 4: Graph from user prompt (nodes 1-4 mapped to 0-3)
    # 1 -> 2 (2), 2 -> 4 (3), 2 -> 1 (4), 4 -> 1 (2), 4 -> 3 (3), 3 -> 2 (1)
    graph4 = [
        [0, 2, INF, INF],
        [4, 0, INF, 3],
        [INF, 1, 0, INF],
        [2, INF, 3, 0]
    ]
    print("Example 4 Output:")
    res4 = floyd_warshall(graph4)
    for row in res4:
        print(row)
