def floyd(graph):
    #PSEUDOCÓDIGO: dados: G = (V, E)
    #graph é a matriz de adjacência recebida do arquivo
    
    vertex = len(graph) #Tamanho do grafo (número de vértices)

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
    for k in range(vertex):                                     #k é o vértice intermediário
        for i in range(vertex):                                 #i é o vértice de origem
            for j in range(vertex):                             #j é o vértice de destino
                if dist[i][k] + dist[k][j] < dist[i][j]:        
                    dist[i][j] = dist[i][k] + dist[k][j]        #Atualiza a distância mínima
                    route[i][j] = route[i][k]                   #Atualiza o próximo vértice no caminho mínimo

    return dist, route

def graph_read(archive):
    '''Lê o grafo no formato:
        <num_vertices> <num_arestas>
        <origem> <destino> <cost>
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

archive = "C:\\Users\\laris\\Desktop\Faculdade\\4° periodo\\Teoria de grafos\\Minimum-path-algoritms-scenarios\\Scenario 1\\graph1.txt"
graph = graph_read(archive)

dist, route = floyd(graph)


'''
Resultados esperados:
O nó que representa a estação central escolhida
Um vetor com as distâncias da estação central até os demais vértices
O vértice mais distante da estação central, junto com o valor de distância
Uma matriz em que cada linha representa um vértice candidato à estação central e cadacoluna é a 
                distância mínima entre o vértice candidato e o vértice representante da coluna.
'''