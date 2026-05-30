from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado
from meu_grafo_matriz_adj_dir import MeuGrafo
grafo = MeuGrafo()

grafo.adiciona_vertice("A")
grafo.adiciona_vertice("B")
grafo.adiciona_vertice("C")

grafo.adiciona_aresta("a1", "A", "B")
grafo.adiciona_aresta("a2", "B", "C")
grafo.adiciona_aresta("a3", "C", "B")

print((grafo.indice_do_vertice(grafo.vertices[0])))
print(grafo.matriz[0][0])
print(grafo.menor_caminho("A", "B"))


#print(grafo.warshall())
