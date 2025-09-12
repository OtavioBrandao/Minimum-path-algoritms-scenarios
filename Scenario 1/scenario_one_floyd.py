def floyd(graph):
    #PSEUDOCÓDIGO: dados: G = (V, E)
    #graph é a matriz de adjacência recebida do arquivo
    
    vertex = len(graph) #Tamanho do grafo (número de vértices)

    '''
    PSEUDOCÓDIGO:
        para todo i, j em V faça
        d_ij ← valor da aresta (i, j) em V(G)
        r_ij ← j
    '''

    #ver como fazer a inicialização da matriz de distancia
    #ver como fazer a inicialização da matriz de roteamento

    '''
    PSEUDOCÓDIGO:
        para k = 1 até n faça
            para i = 1 até n faça
                para j = 1 até n faça
                    se d_ik + d_kj < d_ij então
                    d_ij ← d_ik + d_kj
                        r_ij ← r_ik
    '''
    for k in range(vertex):                                 #k é o vértice intermediário
        for i in range(vertex):                             #i é o vértice de origem
            for j in range(vertex):                         #j é o vértice de destino
                if dist[i][k] + dist[k][j] < dist[i][j]:        
                    dist[i][j] = dist[i][k] + dist[k][j]    #Atualiza a distância mínima
                    route[i][j] = route[i][k]               #Atualiza o próximo vértice no caminho mínimo

    return dist, route

def graph_read(archive):
    
    '''Lê o grafo no formato:
        <num_vertices> <num_arestas>
        <origem> <destino> <cost>
    '''
    #fazer a leitura do arquivo
    
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