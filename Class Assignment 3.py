def BFS(V,E):
    visited = {}
    for vector in V:                                    # set all vertices as not-visited
        visited[vector] = -1
    Q = ['A']                                           # enqueue 'A' as the starting vertex
    print("Vertex A enqueued.")
    print("Current Queue:", Q)
    visited['A'] = 0                                    # set the distance to zero because A is the source
    while(len(Q) != 0):                                 # while the queue is not empty
        print("Vertex " + Q[0] + " visited.")
        print(visited)
        for e in E:                                     # for ALL edges of the graph (whether on the path or not)
            # IF the edge's SOURCE vertex is the same as the top of the queue AND
            # IF the edge's DESTINATION vertex hasn't been visited yet
            if (e[0] == Q[0]) and (visited[e[1]] == -1):
                Q.append(e[1])                          # push the reachable adjacent (destination) vertex on queue
                print("Vertex enqueued: ", e[1])
                print("Current Queue: ", Q)
                visited[e[1]] = visited[Q[0]] + e[2]    # set the distance it took to reach that vertex from the source
        print("Vertex " + Q[0] + " dequeued.")
        Q.pop(0)
        print("Current Queue:", Q)
    return visited

V = ["A", "B", "C", "D", "E", "F", "G", "H"]
E = [["A", "E", 1], ["A", "H", 1], ["B", "A", 1], ["C", "F", 1], ["C", "G", 1], ["D", "A", 1], ["D", "E",1], ["E", "C", 1],
    ["F", "D", 1], ["F", "E", 1], ["G", "B", 1], ["G", "E", 1], ["H", "D", 1]]


visited = BFS(V,E)
print(visited)