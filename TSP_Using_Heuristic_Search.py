import matplotlib.pyplot as plt
import networkx as nx
import os


def a_star(g: nx.Graph, source: str, destination: str):
    Adj = dict(g.adjacency())
    GRAPH = {i: {j: Adj[i][j]['weight'] for j in Adj[i]} for i in Adj}
    heuristic_value = nx.get_node_attributes(G, 'weight')
    queue = [([source], 0, heuristic_value[source])]
    Result = None
    while queue:
        queue.sort(key=lambda x: x[2])
        if Result is not None and Result['Dist'] < queue[0][2]:
            break
        visited, dist, total_dist = queue.pop(0)
        last_node = visited[-1]
        for node in GRAPH[last_node]:
            if node == destination:
                Result = {'Path': visited+[node],
                          'Dist': dist+GRAPH[last_node][node]}
            elif node not in visited:
                new_dist = dist+GRAPH[last_node][node]
                queue.append((visited+[node], new_dist, new_dist+heuristic_value[node]))
    if Result is not None:
        print("\n ~: Path Found :~ \n")
        print(" With Distance:", Result['Dist'], "\n")
        print(" -> ".join(Result['Path']))
    else:
        print("\n ~: Path Not Found :~ ")


if __name__ == '__main__':
    G = nx.Graph()
    G.add_node('A', pos=(1, 2), weight=2)
    G.add_node('B', pos=(1, 3), weight=6)
    G.add_node('C', pos=(2, 2), weight=2)
    G.add_node('D', pos=(2, 3), weight=3)
    G.add_node('G', pos=(3, 3), weight=0)
    G.add_node('S', pos=(2, 1), weight=4)
    G.add_edge('A', 'S', weight=1)
    G.add_edge('A', 'C', weight=1)
    G.add_edge('A', 'B', weight=3)
    G.add_edge('B', 'D', weight=3)
    G.add_edge('C', 'D', weight=1)
    G.add_edge('C', 'G', weight=2)
    G.add_edge('D', 'G', weight=3)
    G.add_edge('G', 'S', weight=12)
    while True:
        os.system("cls")
        print()
        print("==================================================")
        print("||     ~ : Created By  : Yogesh Kumar : ~       ||")
        print("||     ~ : Roll Number : 205118090    : ~       ||")
        print("||==============================================||")
        print("|| 1. For Add Point                             ||")
        print("|| 2. For Add Path                              ||")
        print("|| 3. For Remove Point                          ||")
        print("|| 4. For Remove Path                           ||")
        print("|| 5. For Find Mini Path                        ||")
        print("|| 6. For Display Map                           ||")
        print("|| 7. For Exit                                  ||")
        print("||==============================================||")
        operation = input(" Select a Operation : ")
        if operation == '1':
            Name = input("\n Enter a New Point Name              : ")
            HeuV = input("\n Enter a New Point Heuristic Value   : ")
            X, Y = input("\n Enter a New Point Coordinate X,Y    : ").split()
            G.add_node(Name, pos=(int(X), int(Y)), weight=int(HeuV))
        elif operation == '2':
            u = input("\n Path Starting Point Name   : ")
            v = input("\n Path Ending Point Name     : ")
            w = input("\n Path Weight                : ")
            if u not in G.nodes:
                print("Starting Point not Find in Map")
            elif v not in G.nodes:
                print("Ending Point not Find in Map")
            else:
                G.add_edge(u, v, weight=int(w))
        elif operation == '3':
            N = input("\n Enter Point Name   : ")
            G.remove_node(N)
        elif operation == '4':
            u = input("\n Path Starting Point Name  : ")
            v = input("\n Path Ending Point Name    : ")
            G.remove_edge(u, v)
        elif operation == '5':
            print("\n In Default Heuristic value Source as S and Destination as D")
            Source = input("\n Source Point Name      : ")
            Destination = input("\n Destination Point Name : ")
            a_star(G, Source, Destination)
        elif operation == '6':
            fig, ax = plt.subplots()
            pos = nx.get_node_attributes(G, 'pos')
            nx.draw(G, pos, node_size=1500, node_shape='o')
            labels = nx.get_edge_attributes(G, 'weight')
            node_labels = nx.get_node_attributes(G, 'weight')
            node_labels = {N: N + "=" + str(node_labels[N]) for N in node_labels}
            nx.draw_networkx_labels(G, pos, node_labels, font_color="white", font_weight="bold")
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
            ax.set_xlim([0.5, 3.5])
            ax.set_ylim([0.5, 3.5])
            plt.title("Graph")
            plt.show()
        elif operation == '7':
            exit()
        else:
            print("\n Please Select a correct operation")
        input("\n Press Enter to Continue ...")
