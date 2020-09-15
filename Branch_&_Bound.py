import matplotlib.pyplot as plt
import networkx as nx
import os


def branch_and_bound(g: nx.Graph, source: str, destination: str):
    Adj = dict(g.adjacency())
    GRAPH = {i: {j: Adj[i][j]['weight'] for j in Adj[i]} for i in Adj}
    queue = [([source], 0)]
    Result = None
    node_dist = {source: 0}
    while queue:
        queue.sort(key=lambda x: x[1])
        if Result is not None and Result['Dist'] <= queue[0][1]:
            break
        visited, dist = queue.pop(0)
        last_node = visited[-1]
        for node in GRAPH[last_node]:
            new_dist = dist+GRAPH[last_node][node]
            if node_dist.get(node,new_dist) < new_dist:
                continue
            if node == destination:
                if Result is not None and Result['Dist'] > new_dist:
                    Result = {'Path': visited+[node],
                              'Dist': new_dist}
                elif Result is None:
                    Result = {'Path': visited+[node],
                              'Dist': new_dist}
            elif node not in visited:
                node_dist[node] = min(node_dist.get(node, new_dist), new_dist)
                queue.append((visited+[node], new_dist))
    if Result is not None:
        print("\n ~: Path Found :~ \n")
        print(" With Distance:", Result['Dist'], "\n")
        print(" -> ".join(Result['Path']))
    else:
        print("\n ~: Path Not Found :~ ")


if __name__ == '__main__':
    G = nx.Graph()
    G.add_node('A', pos=(1, 4))
    G.add_node('B', pos=(1, 3))
    G.add_node('C', pos=(1, 2))
    G.add_node('D', pos=(2, 4))
    G.add_node('E', pos=(2, 3))
    G.add_node('F', pos=(2, 2))
    G.add_node('G', pos=(3, 3.5))
    G.add_edge('A', 'D', weight=4)
    G.add_edge('A', 'B', weight=5)
    G.add_edge('B', 'C', weight=4)
    G.add_edge('B', 'D', weight=3)
    G.add_edge('B', 'E', weight=6)
    G.add_edge('C', 'E', weight=4)
    G.add_edge('C', 'F', weight=7)
    G.add_edge('D', 'E', weight=8)
    G.add_edge('D', 'G', weight=15)
    G.add_edge('E', 'F', weight=2)
    G.add_edge('E', 'G', weight=2)
    while True:
        os.system("cls")
        print()
        print("==================================================")
        print("||     ~ : Created By  : Yogesh Kumar : ~       ||")
        print("||     ~ : Roll Number : 205118090    : ~       ||")
        print("||==============================================||")
        print("|| 1. For Add Node                              ||")
        print("|| 2. For Add Edge                              ||")
        print("|| 3. For Remove Node                           ||")
        print("|| 4. For Remove Edge                           ||")
        print("|| 5. For Find Path Using A Star Algorithm      ||")
        print("|| 6. For Plot Graph                            ||")
        print("|| 7. For Exit                                  ||")
        print("||==============================================||")
        operation = input(" Select a Operation : ")
        if operation == '1':
            Name = input("\n Enter a New Node Name              : ")
            print("\n Coordinate between 0 to 5")
            X, Y = input(" Enter a New Node Coordinate X Y    : ").split()
            G.add_node(Name, pos=(int(X), int(Y)))
        elif operation == '2':
            u = input("\n Edge Starting Node Name   : ")
            v = input("\n Edge Ending Node Name     : ")
            w = int(input("\n Edge Weight               : "))
            G.add_edge(u, v, w)
        elif operation == '3':
            N = input("\n Enter Node Name   : ")
            if N not in G.nodes:
                print("Node not Find in Graph")
            else:
                G.remove_node(N)
        elif operation == '4':
            u = input("\n Edge Starting Node Name \t : ")
            v = input("\n Edge Ending Node Name \t : ")
            if u not in G.nodes:
                print("Starting Node not Find in Graph")
            elif v not in G.nodes:
                print("Ending Node not Find in Graph")
            else:
                G.remove_edge(u, v)
        elif operation == '5':
            Source = input("\n Source Node \t : ")
            Destination = input("\n Destination Node : ")
            if Source not in G.nodes:
                print("Source Node not Find in Graph")
            elif Destination not in G.nodes:
                print("Destination Node not Find in Graph")
            else:
                branch_and_bound(G, Source, Destination)
        elif operation == '6':
            fig, ax = plt.subplots()
            pos = nx.get_node_attributes(G, 'pos')
            nx.draw(G, pos, node_size=1500, node_shape='o', with_labels=True)
            labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
            ax.set_xlim([0, 5])
            ax.set_ylim([0, 5])
            plt.title("Graph")
            plt.show()
        elif operation == '7':
            exit()
        else:
            print("\n Please Select a correct operation")
        input("\n Press Enter to Continue ...")
