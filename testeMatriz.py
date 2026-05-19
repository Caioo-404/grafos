from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado

grafo = GrafoMatrizAdjacenciaDirecionado()

grafo.adiciona_vertice("A")
grafo.adiciona_vertice("B")
grafo.adiciona_vertice("C")

grafo.adiciona_aresta("a1", "A", "B")
grafo.adiciona_aresta("a2", "A", "C")
grafo.adiciona_aresta("a3", "B", "C")

print(grafo)
print(grafo.matriz[0][1]["a1"])
