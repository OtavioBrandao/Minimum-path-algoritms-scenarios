from GraphUtility import AdjGraph

def idx(r, c, cols):
    return r * cols + c

def idx_to_pos(index, cols):
    return index // cols, index % cols

def inside(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

def main_dijkstra():
    print("\nScenario 3: Robot needs to reach somewhere with the minimum cost and avoid any obstacles. The map is represented as a grid example file.")
    file_dir = "GraphExamples\\grid_example.txt"
    Graph, start_vertex, goal_vertex, rows, cols, grid = read_map(file_dir)
    path = dijkstra_algorithm(Graph, start_vertex, goal_vertex, rows, cols)
    print_path(path, rows, cols, grid)

def weight(character):                              #Pegar o peso da aresta
    if character == '.':
        return 1
    if character == 'G' or character == 'S':
        return 1
    elif character == '#':
        return None
    elif character == '~':
        return 3
    else:
        raise ValueError(f"Invalid character: {character}")

def print_path(path, rows, cols, grid):
    sum = 0
    grid_copy = grid.copy()
    for vertex in path:
        row, col = idx_to_pos(vertex, cols)
        if grid_copy[row][col] not in ['S', 'G']:
            sum += weight(grid[row][col])                       
            grid_copy[row][col] = '|'
            
    print("\nGrid with marked path:")
    for row in grid_copy:
        print(''.join(row))
            
    print(f"\nThe minimum cost to reach G from S is {sum} with {len(path)} steps")
    
def read_map(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    dimensions = lines[0].strip().split()     #Vai ler a primeira linha
    rows = int(dimensions[0])                 #le o primeiro numero (linha)
    cols = int(dimensions[1])                 #le o segundo numero (coluna)  

    V = []      
    num_vertex = 0
    Graph = None    
    grid = []   
     
    #Primeira leitura do mapa
    for row in range(rows):
        grid_row = []
        current_line = lines[row + 1].strip() #Remove '\n' e espaços extras
        
        #verificação para garantir que a linha tem o tamanho esperado
        if len(current_line) != cols:
            raise ValueError(f"A linha {row + 1} do mapa tem {len(current_line)} colunas, mas o esperado eram {cols}.")

        for col in range(cols):
            char = current_line[col]
            V.append(char)              #Adiciona o caractere na lista de vértices
            num_vertex += 1             #Incrementa o número de vértices
            vertex_index = idx(row, col, cols)
            grid_row.append(char)
            
            if char == "S":
                start_vertex = vertex_index
            if char == "G":
                goal_vertex = vertex_index
        grid.append(grid_row)       
             
    #print(f"Number of vertices: {num_vertex}")
    #print(f"Vertices: {V}") 
            
    Graph = AdjGraph(num_vertex, False, V)

     #Direções cardinais: Norte, Sul, Oeste, Leste
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for current_line in range(rows):
        for current_col in range(cols):
            current_char = V[idx(current_line, current_col, cols)]
            if current_char == '#':
                continue
            
            for variation_line, variation_col in directions:
                new_line = current_line + variation_line
                new_col = current_col + variation_col

                if not inside(new_line, new_col, rows, cols):
                    continue
             
                u = idx(current_line, current_col, cols)
                v = idx(new_line, new_col, cols)
                character = V[idx(new_line, new_col, cols)]

                if character == '#':
                    continue
                
                Graph.addEdge(u, v, weight(character))
                
                    
    #Graph.print_graph()
    return Graph, start_vertex, goal_vertex, rows, cols, grid

def dijkstra_algorithm(Graph, start_vertex, goal_vertex, rows, cols):
    #d[1i] ← ∞ para todo i ∈ V - {1} (distância inicial infinita)
    distances = [float('inf')] * Graph.NumVertices
    
    #d[11] ← 0 (distância da origem até ela mesma é 0)
    distances[start_vertex] = 0

    #A ← V (conjunto de vértices abertos)
    unvisited = set(range(Graph.NumVertices))

    #F ← ∅ (conjunto de vértices fechados)
    visited = set()

    #anterior[i] ← 0 para todo i
    previous = [None] * Graph.NumVertices

    #enquanto A ≠ ∅ faça
    while unvisited:
        
        #r ← v ∈ V | d[1r] = min{d[ij]} (escolhe vértice com menor distância)
        current_vertex = min(unvisited, key=lambda v: distances[v])
        
        #F ← F ∪ {r} (move r para fechado)
        visited.add(current_vertex)
        
        #A ← A - {r} (remove r de aberto)
        unvisited.remove(current_vertex)

        if current_vertex == goal_vertex:
            break

        #S ← A ∩ N+(r) (sucessores de r que ainda estão em A)
        for neighbor in Graph.getNeighbors(current_vertex, mode="+"):
            if neighbor not in visited:  #para todo i ∈ S faça
                edge_weight = Graph.get_edge_weight(current_vertex, neighbor)
                if edge_weight is not None:
                    #p ← min(d[1i][k-1], (d[1r] + v[ri]))
                    new_distance = distances[current_vertex] + edge_weight
                    #se p < d[1i][k-1] então
                    if new_distance < distances[neighbor]:
                        #d[1i][k] ← p 
                        distances[neighbor] = new_distance
                        #anterior[i] ← r (atribui a nova distância)
                        previous[neighbor] = current_vertex

    if distances[goal_vertex] == float('inf'):
        print("No path found.")
        return None

    path = []
    current_vertex = goal_vertex
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous[current_vertex]
    path.reverse()

    return path
    
   
if __name__ == "__main__":
    main_dijkstra()