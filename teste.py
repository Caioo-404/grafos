from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from meu_grafo_lista_adj_nao_dir import *

graph = MeuGrafo()
graph.adiciona_vertice("1")
graph.adiciona_vertice("4")
graph.adiciona_vertice("3")
graph.adiciona_vertice("2")

graph.adiciona_aresta("a1", "1", "2")
graph.adiciona_aresta("a2", "2", "3")
graph.adiciona_aresta("a4", "3", "3")
print(MeuGrafo.ha_ciclo(graph))
print([[1] * 7 for _ in range(7)])
'''
grafoListaAdj = dict()
for v in graph.vertices:
    grafoListaAdj[v.rotulo] = list()

for a in graph.arestas.values():
    grafoListaAdj[a.v1.rotulo].append(a.v2.rotulo)
    grafoListaAdj[a.v2.rotulo].append(a.v1.rotulo)

print(graph)
print("--" * 5, "\n", grafoListaAdj)
print(len(grafoListaAdj))
'''

'''
grafo = {'1': ['4', '3'], '4': [], '3': [], '2': []}
visitados = set()
vertice = list(grafo.keys())[0]
ciclo = True

def dfsParaCiclo(v, pai):
    visitados.add(v)
    
    for vizin in grafo[v]:
        if vizin not in visitados:
            if dfsParaCiclo(vizin, v):
                return True

        elif vizin != pai:
            return True
    
    return False 
'''
#conj = {graph.vertices[0].rotulo, graph.vertices[1].rotulo}
#par_atual = { frozenset([2, 3]), frozenset([4, 5]) }
'''
naoAdj = set()
if len(naoAdj) == 0:
    print("a")
else:
    print("B")


naoAdj = set()
vertex = graph.vertices
adjacencias = [{i.v1.rotulo, i.v2.rotulo} for i in graph.arestas.values()]
for i in range(len(vertex) - 1):
    for j in range(c, len(vertex)):
        if {vertex[i].rotulo, vertex[j].rotulo} not in adjacencias:
            naoAdj.add(f"{vertex[i].rotulo}-{vertex[j].rotulo}")
    c += 1
    print(naoAdj)

'''
#python -m unittest grafo_lista_adj_test_nao_dir.TestGrafo.test_ha_paralelas