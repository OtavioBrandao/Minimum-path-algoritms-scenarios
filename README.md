# Minimal path algorithm implementations

## Scenario 1
Since this problem asks for the shortest path between **all pairs of vertices**, `we use the Floyd-Warshall algorithm`, which was designed specifically for this purpose. Furthermore, the problem requires a matrix to store these distances, which is precisely how the algorithm operates.
`We do not use Dijkstra's algorithm` because it finds the shortest path from a **single source vertex**. We would need to run the algorithm **N** times (once for each vertex). While this would work, Floyd-Warshall is more direct. As for `Bellman-Ford`, it would also work, but it is `very inefficient` for this case. Since we won't have negative edge weights (as we are dealing with metro distances), there is no compelling reason to implement it in this scenario. Additionally, like Dijkstra's, it also only analyzes paths from a single source vertex at a time.

## Scenario 2
In this scenario, we have negative weights. Therefore, `we choose the Bellman-Ford algorithm` because it was specifically designed to handle the possibility of negative weights. Since the problem only asks for the shortest path from a single source, it is the best choice. Even though `Floyd-Warshall` can handle negative weights, it calculates the shortest path `for all pairs`, which would be unnecessary here.
As for `Dijkstra's algorithm`, it `cannot handle negative weights`, so it cannot be implemented here, as it would fail.

## Scenario 3
For this scenario, `we choose Dijkstra's algorithm`, as there are no negative costs, and since the problem only requires a single shortest path, this would be the most efficient algorithm. 
We do not choose `Bellman-Ford or Floyd-Warshall` because they `are much slower` than Dijkstra, mostly because the grid example file represents a very huge graph, so it would probably take too long to run. Besides that they are designed for different problems (negative weights or all-pairs paths, respectively).

# How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/OtavioBrandao/Minimum-path-algoritms-scenarios
   cd Minimum-path-algoritms-scenarios
   ```
2. If you prefer, you can run it into a virtual env:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    ```
3. Or you can just run it directly into your machine:
    ```bash
    python main.py
    ```
# Observations
The pseudocode for each algorithm is provided in comments alongside the actual code for study and comparison. These were taken from the Algoritmos de Caminho Mínimo PDF in GraphExamples folder.