import matplotlib.pyplot as plt
import networkx as nx
import os


def bfs(adj: dict, queue: list, visited: dict, parent: dict):
    current = queue.pop(0)
    for node in adj[current]:
        if not visited[node]:
            parent[node] = current
            visited[node] = True
            queue.append(node)


def print_path(source_parent, destination_parent,
               source, destination, intersect):
    Left_Path = []
    Right_Path = []
    node = intersect
    while node != source:
        Left_Path.append(source_parent[node])
        node = source_parent[node]
    Left_Path.reverse()
    node = intersect
    while node != destination:
        Right_Path.append(destination_parent[node])
        node = destination_parent[node]
    if not Left_Path:
        print("{", intersect, "} <-", " <- ".join(Right_Path))
    elif not Right_Path:
        print(" -> ".join(Right_Path), "-> {", intersect, "}")
    else:
        print(" -> ".join(Left_Path), "-> {", intersect, "} <-", " <- ".join(Right_Path))


def bidirectional_search(g: nx.Graph, source: str, destination: str):
    Adj = dict(g.adjacency())
    Adj = {i: list(Adj[i]) for i in Adj}
    source_visited = {i: False for i in Adj}
    destination_visited = {i: False for i in Adj}
    source_queue = [source]
    source_visited[source] = True
    destination_queue = [destination]
    destination_visited[destination] = True
    intersectNode = None
    source_parent = {source: None}
    destination_parent = {destination: None}
    while source_queue and destination_queue:
        bfs(Adj, source_queue, source_visited, source_parent)
        bfs(Adj, destination_queue, destination_visited, destination_parent)
        for node in Adj:
            if source_visited[node] and destination_visited[node]:
                intersectNode = node
        if intersectNode is not None:
            print("\n ~: Path Found :~ \n")
            print(" Intersection at:", intersectNode, "\n")
            print_path(source_parent, destination_parent,
                       source, destination, intersectNode)
            return
    print("\n ~: Path Not Found :~ ")


if __name__ == '__main__':
    D = {
        '4': ['0', '1'],
        '5': ['2', '3'],
        '6': ['4', '5', '7'],
        '8': ['7', '9', '10'],
        '9': ['11', '12'],
        '10': ['13', '14']
    }
    G = nx.Graph(D)
    while True:
        os.system("cls")
        print()
        print("==================================================")
        print("||      ~ : Created By  : Yogesh Kumar : ~      ||")
        print("||      ~ : Roll Number : 205118090    : ~      ||")
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
            bidirectional_search(G, Source, Destination)
        elif operation == '4':
            nx.draw_networkx(G, with_labels=True)
            plt.show()
        elif operation == '5':
            exit()
        else:
            print("\n Please Select a correct operation")
        input("\n Press Enter to Continue ...")
