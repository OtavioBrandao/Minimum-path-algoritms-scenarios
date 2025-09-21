from typing import Generator
from abc import ABC, abstractmethod

class GraphBase(ABC):
  """
  Generic class for a graph
  ...

  Attributes
  ----------
  n : int
      Cardinality of the set of vertices V.
  m : int
      Cardinality of the set of edges E.
  directed : bool
      Defines if the graph is directed or not.

  """

  def __init__(self, NumVertices: int, directed: bool = False) -> None:
    self.NumVertices, self.NumEdges, self.directed = NumVertices, 0, directed
    self.MatrizAdj = [[0.0] * (self.NumVertices + 1) for _ in range(self.NumVertices + 1)]
  @abstractmethod
  def addEdge(self, vertice: int, wertice: int):
    ''' Adds edge verticewertice to the graph

    Parameters
    ----------
    vertice: int
      first vertex.
    wertice: int
      second vertex.
    '''
    pass

  @abstractmethod
  def removeEdge(self, vertice: int, wertice: int):
    ''' Removes edge verticewertice from the graph

    Parameters
    ----------
    vertice: int
      first vertex.
    wertice: int
      second vertex.
    '''
    pass

  @abstractmethod
  def getNeighbors(self, vertice: int, mode : str = "*", closed : bool = False) -> Generator[int, None, None]:
    '''Provides the neighbors of vertex v.

    Parameters
    ----------
    vertice: int
      vertex.
    mode : str
      Only for directed graph. "-" if input neighborhood, "+" if output neighborhood and "*" if any.
    closed : bool
      Defines if it is a closed or open interval. True if the neighboorhood should include v or False if it should exclude.
    iterateOverNode : bool
      Defines if the iterator gives the pair of vertices (False) or a pair consisting of v and a node

    Yields
    ----------
    int
      neighbor of vertex v.

    '''
    pass

  @abstractmethod
  def isNeighbor(self, vertice: int, wertice: int) -> bool:
    '''Checks if v and w are adjacent

    Parameters
    ----------
    vertice: int
      first vertex.
    wertice: int
      second vertex.

    Returns
    ----------
    bool
      True if vertice and wertice are adjacent, False otherwise.
    '''
    pass

  def Vertices(self) -> Generator[int, None, None]:
    """
    Retorna a lista de vértices.
    """
    for i in range(1, self.n+1):
      yield i

  def Edges(self, iterateOverNode = False) -> Generator[tuple[int,int], None, None] | Generator[tuple[int, object], None, None]:
    """
    Retorna a lista de arestas vertice x wertice
    """

    for vertice in self.Vertices():
      for wertice in self.getNeighbors(vertice, mode = "+" if self.directed else "*"):
        count = True

        if not self.directed: # avoid double counting
          werticeint = int(wertice) # assures int, even if it's an object/node
          count = vertice < werticeint

        if count:
          yield (vertice, wertice)
          