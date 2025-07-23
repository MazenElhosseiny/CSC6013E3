def BFS(V,E):
    for i in range(len(V)):
        V[i] = -1
    count = 0
    for i in range(len(V)):
        if (V[i] == -1):
            Q = [i]
            V[i], count = count, count+1
            while(len(Q) != 0):
                for e in E:
                    if (e[0] == Q[0]) and (V[e[1]] == -1):
                        Q.append(e[1])
                        print(f"Vertex enqueued: {e[1]}")
                        V[e[1]], count = count, count+1
                        print(f"Vertex visited: {e[1]}")
                print(f"Vertex {Q.pop(0)} popped")

V = [0]*8
#E = [["A", "E", 1], ["A", "H", 1], ["B", "A", 1], ["C", "F", 1], ["C", "G", 1], ["D", "A", 1], ["D", "E",1], ["E", "C", 1],
#["F", "D", 1], ["F", "E", 1], ["G", "B", 1], ["G", "E", 1], ["H", "D", 1]]

E = [["A", "E", 1], ["A", "H", 1], ["E", "C", 1], ["H", "D", 1], ["C", "F", 1], ["C", "G", 1], ["D", "A", 1], ["D", "E", 1],
    ["F", "D", 1], ["F", "E", 1],  ["G", "B", 1], ["G", "E", 1], ["B", "A", 1]]


BFS(V,E)
print(V)