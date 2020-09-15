import matplotlib.pyplot as plt
import networkx as nx
import os


def dfs(g: nx.DiGraph, start_node: str):
    Adj = dict(g.adjacency())
    Adj = {i: list(Adj[i]) for i in Adj}
    Visited = {i: False for i in Adj}
    Stack = [start_node]
    Result = []
    while len(Stack):
        s = Stack[-1]
        Stack.pop()
        if not Visited[s]:
            Result.append(s)
            Visited[s] = True
        for node in Adj[s]:
            if not Visited[node]:
                Stack.append(node)
    print("\n", " -> ".join(Result))


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
        print("\n"+"{^_^} " * 5)
        print(" 1. For Add Node")
        print(" 2. For Add Edge")
        print(" 3. For DFS Traversal")
        print(" 4. For Plot Graph")
        print(" 5. For Exit")
        print("{^_^} " * 5+"\n")
        operation = input(" Select a Operation : ")
        if operation == '1':
            Node = input("\n Enter a New Node Name : ")
            G.add_node(Node)
        elif operation == '2':
            u = input("\n Edge Starting Node Name \t : ")
            v = input("\n Edge Ending Node Name \t : ")
            G.add_edge(u, v)
        elif operation == '3':
            Node = input("\n Traversal Start From Node : ")
            dfs(G, Node)
        elif operation == '4':
            nx.draw_networkx(G, with_labels=True)
            plt.show()
        elif operation == '5':
            exit()
        else:
            print("\n Please Select a correct operation")
        input("\n Press Enter to Continue ...")
