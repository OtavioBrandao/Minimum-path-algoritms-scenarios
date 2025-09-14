from GraphUtility import create_graph_from_file
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

'''
início
    d[11] ← 0
    d[1i] ← ∞ para todo i ∈ V - {1}      
    anterior[i] ← 0 para todo i 
    
    enquanto existir (j, i) ∈ A tal que d[1i] > d[1j] + v[ji] faça //varre todas as arestas aplicando o critério
        d[1i] ← d[1j] + v[ji]
        anterior[i] ← j
    fim-enquanto
fim
'''

def main_belmann_ford():
    while True:
        print("Scenario 2: Electric car with regeneration of battery")
        print("The car is supposed to go from a starting point to a destination with the minimum cost.")
        print("For that, we will use the Bellman-Ford algorithm.")
        print("=============================================================")
        try:
            complete_path = f"GraphExamples\\graph2.txt" 
            Graph = create_graph_from_file(complete_path, directed=True)
            if Graph is None:
                raise Exception("Graph could not be created. Please check the file and try again.")
            print("Graph successfully created. Here is the adjacency matrix:")
            Graph.print_graph()
            print("=============================================================================")
            print("Here's the result of the Bellman-Ford algorithm from vertex 0 to vertex 6:")
            Bellman_Ford_Algorithm(Graph, 0, 6)
            print("=============================================================================")
            break
        except Exception as e:
            print(f"Error: {e}")
            print("Press Enter to try again.")
            input()
            clear_screen()
            continue

def Bellman_Ford_Algorithm(Graph, start_vertex, end_vertex):
    num_vertex = Graph.NumVertices
    # Dicionários para armazenar as distâncias da origem para um dado vértice até agora e os o caminho percorrido
    distances = {}
    previous = {}
    
    # Inicializa d[11] ← 0, d[1i] ← ∞ para todo i ∈ V - {1} e anterior[i] ← 0 para todo i
    for vertex in Graph.vertices_list:
        if vertex == start_vertex:
            distances[vertex] = 0               # d[11] ← 0 (Define o custo do vértice inicial como 0)
        else:
            distances[vertex] = float('inf')    #  d[1i] ← ∞ para todo i ∈ V - {1} (Deixa o custo dos outros vértices como infinito)
        previous[vertex] = None                 # anterior[i] ← 0 para todo i (Define todos vértices anteriores como None)

    # Enquanto existir (j, i) ∈ A tal que d[1i] > d[1j] + v[ji] faça (Varre todas as arestas aplicando o critério)
    # Repetimos o processo |V| - 1 vezes para descobrir todos os caminhos possíveis e depois ver o menor
    for _ in range(num_vertex - 1):
        changed = False
        for u in Graph.vertices_list:                   # Varre todo vértice u do Grafo
            for v in Graph.getNeighbors(u, mode="+"):   # Vai checar em todos os vizinhos do vertice u atual
                cost = Graph.get_edge_weight(u, v)      # Pega o custo da aresta (u, v), definido na classe AdjGraph
                if distances[u] + cost < distances[v]:  # Se d[1i] > d[1j] + v[ji]
                    distances[v] = distances[u] + cost  #   d[1i] ← d[1j] + v[ji]
                    previous[v] = u                     #   anterior[i] ← j
                    changed = True                      # Flag para marcar que houve mudança na iteração

        if changed is False:
            break  # Se não houve mudança, o algoritmo pode parar mais cedo
    
    if distances[end_vertex] == float('inf'): # Se após todo o processo o custo do vértice 6 for infinito, é porque não houve substituição então não existe caminho
        print(f"A path from vertex {start_vertex} to vertex {end_vertex} does not exist.")
        return

    print(f"The shortest path from vertex {start_vertex} to vertex {end_vertex} is {distances[end_vertex]}.")
    path = []
    # Reconstroi o caminho a partir do dicionário previous, onde salva todo o caminho percorrido
    current_vertex = end_vertex
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous[current_vertex]
    path.reverse()
    print("The path taken is:", " -> ".join(map(str, path)))

if __name__ == "__main__":
    main_belmann_ford()