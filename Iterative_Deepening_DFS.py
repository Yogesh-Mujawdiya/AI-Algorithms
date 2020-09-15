import matplotlib.pyplot as plt
import networkx as nx
import os


def get_level(g: dict, start_node: str):
    Visited = {i: False for i in g}
    Queue = [start_node]
    Visited[start_node] = False
    Level = {start_node: 0}
    while Queue:
        s = Queue.pop(0)
        for node in g[s]:
            if not Visited[node]:
                Queue.append(node)
                Visited[s] = True
                if node in Level:
                    Level[node] = min(Level[node],Level[s]+1)
                else:
                    Level[node] = Level[s]+1
    return Level


def dfs(g: dict, level: dict, source: str,
        destination: str, max_depth: int):
    Stack = [source]
    Visited = {i: False for i in g}
    Result = []
    Find = False
    while len(Stack):
        s = Stack.pop()
        if level[s] < max_depth:
            continue
        if not Visited[s]:
            Result.append(s)
            Visited[s] = True
        if s == destination:
            Find = True
            break
        for node in g[s]:
            if not Visited[node]:
                Stack.append(node)
        max_depth = 0
    return Find, Result


def iterative_deepening_dfs(g: nx.DiGraph, source: str, destination: str):
    Adj = dict(g.adjacency())
    Adj = {i: list(Adj[i]) for i in Adj}
    Level = get_level(g, source)
    max_depth = max(map(int, Level.values()))
    for depth in range(max_depth+1):
        Result, Path = dfs(Adj, Level, source, destination, depth)
        if Result:
            break
    if Result:
        print("\n ~: Path Found :~ \n")
        print(" -> ".join(Path))
    else:
        print("\n ~: Path Not Found :~ ")


if __name__ == '__main__':
    D = {
        '1': ['2'],
        '2': ['3'],
        '3': ['4'],
        '4': ['1'],
        '5': ['1', '4']
    }
    G = nx.DiGraph(D)
    while True:
        os.system("cls")
        print()
        print("==================================================")
        print("||     ~ : Created By  : Yogesh Kumar : ~       ||")
        print("||     ~ : Roll Number : 205118090    : ~       ||")
        print("||==============================================||")
        print("|| 1. For Add Node                              ||")
        print("|| 2. For Add Edge                              ||")
        print("|| 3. For Search Using Iterative Deepening DFS  ||")
        print("|| 4. For Plot Graph                            ||")
        print("|| 5. For Exit                                  ||")
        print("||==============================================||")
        operation = input(" Select a Operation : ")
        if operation == '1':
            Node = input("\n Enter a New Node Name : ")
            G.add_node(Node)
        elif operation == '2':
            u = input("\n Edge Starting Node Name \t : ")
            v = input("\n Edge Ending Node Name \t : ")
            G.add_edge(u, v)
        elif operation == '3':
            Source = input("\n Source Node \t : ")
            Destination = input("\n Destination Node : ")
            iterative_deepening_dfs(G, Source, Destination)
        elif operation == '4':
            nx.draw_networkx(G, with_labels=True)
            plt.show()
        elif operation == '5':
            exit()
        else:
            print("\n Please Select a correct operation")
        input("\n Press Enter to Continue ...")
