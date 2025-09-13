from GraphBase import GraphBase

#------------------------- Graph Implementation -------------------------#

class AdjGraph(GraphBase):
    def __init__(self, NumVertices: int, directed: bool = False, vertices: list = []):
        super().__init__(NumVertices, directed)
        self.vertices_list = vertices
        
    def addEdge(self, vertice, vertice2, weight):
        self.MatrizAdj[vertice][vertice2] = weight       #adiciona a aresta na matriz de adjacência
        if not self.directed:
            self.MatrizAdj[vertice2][vertice] = weight   #se o grafo não for direcionado, adiciona a aresta na direção oposta
        self.NumEdges += 1

    def removeEdge(self, vertice: int, vertice2: int):
        self.MatrizAdj[vertice][vertice2] = 0       #remove a aresta da matriz de adjacência
        if not self.directed:
            self.MatrizAdj[vertice2][vertice] = 0   #se o grafo nao for direcionado, remove a aresta na direção oposta
        self.NumEdges -= 1 

    def isNeighbor(self, vertice, vertice2):
        return self.MatrizAdj[vertice][vertice2] != 0  # para tratar peso negativo e positivo

    def getNeighbors(self, vertice, mode = "*", closed = False):
        if closed:
            yield vertice  #se é fechado, retorna o próprio vértice

        vertice2 = 1

        while vertice2 <= self.NumVertices:
            if self.directed:
                if mode == "*" and (self.isNeighbor(vertice, vertice2) or self.isNeighbor(vertice2, vertice)): #retorna todos os vizinhos
                    yield vertice2
                elif mode == "+" and self.isNeighbor(vertice, vertice2): #retorna apenas os vizinhos de saida
                    yield vertice2
                elif mode == "-" and self.isNeighbor(vertice2, vertice): #retorna apenas os vizinhos de entrada
                    yield vertice2
            else:
                if self.isNeighbor(vertice, vertice2): #se não for direcionado, retorna todos os vizinhos
                    yield vertice2

            vertice2 += 1

    def get_edge_weight(self, vertice, vertice2):
        return self.MatrizAdj[vertice][vertice2]

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.MatrizAdj[1:]:
            print(row[1:])

        print("List of Vertices:", [vertice for vertice in self.vertices_list])


# For the Scenario 3, we need to read a different file format
class GridGraph(GraphBase):
    pass

'''------------------------- Functions for reading the graph examples -------------------------'''      

# Function to read the graph examples to problems 1 and 2
def read_graph_from_file(file):
    '''
    File format:
        <num_vertices> <num_edges>
        <start> <destination> <cost>
    '''
    try:
        with open(file, 'r') as graph_file:

            V = [] # List of vertices
            E = [] # E is a list of all the graph edges. The parameter is a list of tuples (start, destination, cost)
            lines = graph_file.readlines()

            for index, line in enumerate(lines): # Index will be a flag to identify the first line
                if index == 0:
                    n_vertices, n_edges = map(int, line.split())
                    V = list(range(1, n_vertices + 1))
                    continue

                start, destination, cost = map(int, line.split())
                E.append((start, destination, cost))

            return V, E
    except Exception as e:
        print(f"Error reading graph from file: {e}")
        return None
    
# Make a function to read the grid example file
def read_grid_example_file(file):
    pass

'''------------------------- Functions to create graph instances from the read data -------------------------'''

# We probably can use AdjGraph for problem 1 and 2, not sure for problem 3 tho
def create_graph_from_file(file, directed: bool):
    ''' 
        This function will create a graph with its own weights for each edge. You can define if
    the graph is directed or not by using True or False in the directed parameter.

    '''

    data = read_graph_from_file(file)
    if data is None:
        return None

    V, E = data
    num_vertices = len(V)
    Graph = AdjGraph(num_vertices, directed, V)

    for start, destination, cost in E:
        Graph.addEdge(start, destination, cost)

    return Graph

def create_grid_graph_from_file(file):
    pass

'''
# Testing the graph creation from file
if __name__ == "__main__":
    filename = "graph1.txt"  # Replace with your file path
    directed = False  # Change to False if the graph is undirected

    graph = create_graph_from_file(filename, directed)
    if graph:
        graph.print_graph()

'''
