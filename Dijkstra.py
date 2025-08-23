from Graph import GraphBase

def read_file(filename):
    V = []
    E = []
    NumVertice = 0
    #IMPLEMENTAR UMA LOGICA PARA COLOCAR O EDGE COMO ANY
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("#"): #ignora comentários
                continue
            elif line.startswith("DIRECTED"):
                directed = True
                continue
            elif line.startswith("UNDIRECTED"):
                directed = False
                continue
            elif line.startswith("VERTICES"):
                vertices = line.split()[1:] #pega os vértices da linha
                V.extend(vertices) #adiciona os vértices à lista V
                NumVertice = len(V)
                continue
            elif line.startswith("EDGE"):
                parts = line.split()
                vertice, wertice = int(parts[1]), int(parts[2]) #ignora os espaços, pega os vérticies e depois o peso
                if len(parts) > 3:
                    peso = float(parts[3])
                else:
                    peso = 0.0  # peso padrão se não for informado
                E.append((vertice, wertice, peso))

    return V, E, directed, NumVertice

def create_graph_from_file(filename: str) -> GraphBase:
    V, E, directed, NumVertice = read_file(filename)
    Graph = GrafoAdj(NumVertice, directed, V)
    for vertice, wertice, peso in E:
        Graph.addEdge(vertice, wertice, peso)
    return Graph

class GrafoAdj(GraphBase):
    def __init__(self, NumVertices: int, directed: bool = False, vertices: list = []):
        super().__init__(NumVertices, directed)
        self.lista_vertices = vertices
        #self.MatrizAdj = [[0] * (self.n + 1) for _ in range(self.n + 1)]
        
    def addEdge(self, vertice, wertice, weight):
        self.MatrizAdj[vertice][wertice] = weight       #adiciona a aresta na matriz de adjacência
        if not self.directed:
            self.MatrizAdj[wertice][vertice] = weight   #se o grafo não for direcionado, adiciona a aresta na direção oposta
        self.NumEdges += 1

    def removeEdge(self, vertice: int, wertice: int):
        self.MatrizAdj[vertice][wertice] = 0       #remove a aresta da matriz de adjacência
        if not self.directed:
            self.MatrizAdj[wertice][vertice] = 0   #se o grafo nao for direcionado, remove a aresta na direção oposta
        self.NumEdges -= 1 

    def isNeighbor(self, vertice, wertice):
        return self.MatrizAdj[vertice][wertice] == 1 

    def getNeighbors(self, vertice, mode = "*", closed = False):
        if closed:
            yield vertice  #se é fechado, retorna o próprio vértice

        wertice = 1

        while wertice <= self.NumVertices:
            if self.directed:
                if mode == "*" and (self.isNeighbor(vertice, wertice) or self.isNeighbor(wertice, vertice)): #retorna todos os vizinhos
                    yield wertice
                elif mode == "+" and self.isNeighbor(vertice, wertice): #retorna apenas os vizinhos de saida
                    yield wertice
                elif mode == "-" and self.isNeighbor(wertice, vertice): #retorna apenas os vizinhos de entrada
                    yield wertice
            else:
                if self.isNeighbor(vertice, wertice): #se não for direcionado, retorna todos os vizinhos
                    yield wertice

            wertice += 1
            
    def print_graph(self):
        print("Matriz de Adjacência:")
        for row in self.MatrizAdj[1:]:
            print(row[1:])
            
        print("Lista de Vértices:", [vertice for vertice in self.lista_vertices])

''' PSEUDOCÓDIGO DIJKSTRA
inicio 
    d11 <- 0; d1i <- ∞ para todo i pertencente a V - {1}
    A <- V; F <- ∅; Anterior(i) <- 0 para todo i;
    enquanto A ≠ ∅ faça
        inicio
            r <- v pertecente a V | d1r = min<[d1i]
            F <- F ∪ {r}; A <- A - {r};
            S <- A união N+(r)
            para todo i pertecente a S faça
                inicio
                    P <- min[d1i, (d1i, d1r + vri)]
                    se P < d1i então
                        inicio
                            d1i <- P; Anterior(i) <- r;
                        fim
                fim
        fim
fim
'''  
            
class Dijkstra:
    def __init__(self, grafo: GrafoAdj, origem, destino):
        self.grafo, self.origem, self.destino = grafo, origem, destino
        self.distancia = 0
        
    def algoritmo(self):
        '''distancia[0, 0] = 0
        distancia[0, self.destino] = 99999999999'''
        pass

def main():
    nome_arquivo = input("Digite o nome do arquivo de entrada: ")
    
    grafo = create_graph_from_file(nome_arquivo)
    grafo.print_graph()


if __name__ == "__main__":
    main()