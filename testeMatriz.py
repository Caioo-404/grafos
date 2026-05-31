from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado
from meu_grafo_matriz_adj_dir import MeuGrafo
grafo = MeuGrafo()

grafo.adiciona_vertice("A")
grafo.adiciona_vertice("B")
grafo.adiciona_vertice("C")
grafo.adiciona_vertice("D")
grafo.adiciona_vertice("E")
grafo.adiciona_vertice("F")
grafo.adiciona_aresta("a1", "A", "D", 3)
grafo.adiciona_aresta("a11", "A", "A", 1)
grafo.adiciona_aresta("a2", "B", "A", 2)
grafo.adiciona_aresta("a3", "B", "D", 4)
grafo.adiciona_aresta("a4", "C", "A", 2)
grafo.adiciona_aresta("a41", "C", "D", 4)
grafo.adiciona_aresta("a5", "D", "F", 1)
grafo.adiciona_aresta("a6", "E", "D", 3)
grafo.adiciona_aresta("a7", "E", "F", 5)
grafo.adiciona_aresta("a71", "F", "B", 1)


#print((grafo.indice_do_vertice(grafo.vertices[0])))
#print(grafo.matriz[0][0])
print(grafo.menor_caminho("A", "A"))


#print(grafo.warshall())
