
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
            