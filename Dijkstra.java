// algoritmo de Dijkstra

public class Dijkstra {
    private static final int INFINITO = Integer.MAX_VALUE;

    public static int[] dijkstra(int[][] grafo, int origem) {
        int numVertices = grafo.length;
        int[] distancias = new int[numVertices];
        boolean[] visitado = new boolean[numVertices];

        // Inicializa as distâncias com infinito e a distância da origem com 0
        for (int i = 0; i < numVertices; i++) {
            distancias[i] = INFINITO;
            visitado[i] = false;
        }
        distancias[origem] = 0;

        for (int count = 0; count < numVertices - 1; count++) {
            int u = verticeMinimo(distancias, visitado);
            visitado[u] = true;

            for (int v = 0; v < numVertices; v++) {
                if (!visitado[v] && grafo[u][v] != 0 && distancias[u] != INFINITO
                        && distancias[u] + grafo[u][v] < distancias[v]) {
                    distancias[v] = distancias[u] + grafo[u][v];
                }
            }
        }

        return distancias;
    }

    private static int verticeMinimo(int[] distancias, boolean[] visitado) {
        int min = INFINITO;
        int minIndex = -1;

        for (int v = 0; v < distancias.length; v++) {
            if (!visitado[v] && distancias[v] <= min) {
                min = distancias[v];
                minIndex = v;
            }
        }

        return minIndex;
    }

    public static void main(String[] args) {
        int[][] grafo = {
                {0, 7, 9, 0, 0, 14},
                {7, 0, 10, 15, 0, 0},
                {9, 10, 0, 11, 0, 2},
                {0, 15, 11, 0, 6, 0},
                {0, 0, 0, 6, 0, 9},
                {14, 0, 2, 0, 9, 0}
        };

        int origem = 0;
        int[] distancias = dijkstra(grafo, origem);

        // Exibe as distâncias a partir do vértice de origem
        System.out.println("Distâncias a partir do vértice " + origem + ":");
        for (int i = 0; i < distancias.length; i++) {
            if (distancias[i] == INFINITO) {
                System.out.println("Vértice " + i + ": Infinito");
            } else {
                System.out.println("Vértice " + i + ": " + distancias[i]);
            }
        }
    }
}