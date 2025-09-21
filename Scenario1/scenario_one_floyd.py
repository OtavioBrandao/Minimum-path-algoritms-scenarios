def floyd(graph):
    '''
    PSEUDOCÓDIGO: 
    início
        dados: G = (V, E)
        matriz de valores: V(G)
        matriz de roteamento: R = [r_ij]
    '''
    #graph é a matriz de adjacência recebida do arquivo
    
    vertex = len(graph) #Tamanho do grafo G = (V,E) (número de vértices)

    '''
    PSEUDOCÓDIGO:
        r_ij ← j para todo i 
        D0 = [d_ij] ← V(G) 
    '''

    dist = [[graph[i][j] for j in range(vertex)] for i in range(vertex)]    #matriz d_ij com os valores das arestas
    route = [[j for j in range(vertex)] for i in range(vertex)]             #matriz r_ij com o próximo vértice no caminho (inicialmente o próprio j)

    '''
    PSEUDOCÓDIGO:
        para k = 1 até n faça
            para i = 1 até n faça
                para j = 1 até n faça
                    se d_ik + d_kj < d_ij então
                        d_ij ← d_ik + d_kj
                        r_ij ← r_ik
    '''
    for k in range(vertex):                                    
        for i in range(vertex):                                
            for j in range(vertex):                             
                if dist[i][k] + dist[k][j] < dist[i][j]:        
                    dist[i][j] = dist[i][k] + dist[k][j]        #Atualiza a distância mínima
                    route[i][j] = route[i][k]                   #Atualiza o próximo vértice no caminho mínimo

    return dist, route

def graph_read(archive):
    '''
    Lê o grafo no formato:
        <num_vertices> <num_arestas>
        <origem> <destino> <cost>
    
    Constrói a matriz de adjacência do grafo V(G).    

    '''
    with open(archive, 'r') as graph_file:
        lines = graph_file.readlines()
    
    num_vertices, num_arestas = map(int, lines[0].split())      #Número de vértices e arestas

    INF = float('inf')                                          #Define infinito como um valor muito grande
    graph = [[INF] * num_vertices for _ in range(num_vertices)] #Inicializa a matriz de adjacência com infinito

    for i in range(num_vertices):                               #Inicializa a diagonal principal com 0
        graph[i][i] = 0                                     

    for line in lines[1:]:
        u, v, cost = map(int, line.split())                     #Lê a aresta (u, v) com custo 
        graph[u-1][v-1] = cost                                  #índices ajustados para base 0
    
    return graph

def searching_central_station(dist):
    min_of_max_distance = float('inf')              #Inicializa a menor distância máxima como infinito, para ser mudada depois
    central_station = -1                            #Inicializa a estação central, como um valor inválido

    for i in range(len(dist)):                      #Percorre cada vértice, como um potencial estação central
        max_distance = max(dist[i])                 #Encontra a distância máxima do vértice i para todos os outros vértices
        if max_distance < min_of_max_distance:
            min_of_max_distance = max_distance      #Atualiza a menor distância máxima
            central_station = i + 1                 #Atualiza a estação central (ajustando para base 1 e não 0)

    return central_station, min_of_max_distance

def floyd_main():
    archive = "GraphExamples\\graph1.txt" 
    graph = graph_read(archive)
    dist, route = floyd(graph)      #dist é a matriz da última requisição do enunciado
    central_station, min_of_max_distance = searching_central_station(dist) #central_station é o nó que representa a estação central escolhida
    
    print("\nCentral Station:", central_station)
    print("\nDistances from the central station to the other vertices:", dist[central_station - 1]) #converte da base 0 para base 1 para indexação da matriz
    print(f"\nFarthest vertex from the central station: vertex {dist[central_station - 1].index(min_of_max_distance) + 1} with a distance of {min_of_max_distance}") 
    print("\nMatrix of minimum distances between all pairs of vertices:")
    for i, row in enumerate(dist):
        print(f"Vertex {i+1}: {row}")
  
'''
Resultados esperados:
O nó que representa a estação central escolhida
Um vetor com as distâncias da estação central até os demais vértices
O vértice mais distante da estação central, junto com o valor de distância
Uma matriz em que cada linha representa um vértice candidato à estação central e cadacoluna é a 
                distância mínima entre o vértice candidato e o vértice representante da coluna.
'''