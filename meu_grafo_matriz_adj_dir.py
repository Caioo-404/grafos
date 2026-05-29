from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        pass

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass


    def grau_entrada(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def grau_saida(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass

    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        :return: Uma lista de listas que representa a matriz de alcançabilidade de Warshall associada ao grafo
        '''
        matrizAlc = list()
        QNTVERT = len(self.vertices)

        for v in range(QNTVERT):
            matrizAlc.append([0] * QNTVERT)
            for a in range(QNTVERT):
                if len(self.matriz[v][a]) > 0:
                    matrizAlc[v][a] = 1

        # i = intermediario 
        for i in range(QNTVERT):
            for j in range(QNTVERT):
                if matrizAlc[j][i] == 1: 
                    for k in range(QNTVERT):
                        matrizAlc[j][k] = max(matrizAlc[j][k], matrizAlc[i][k])

        return matrizAlc


    def menor_caminho(self, vi, vf):
        if not(self.existe_rotulo_vertice(vi)) : raise VerticeInvalidoError(f"O vertice {vi} não está no grafo")
        if not(self.existe_rotulo_vertice(vf)) : raise VerticeInvalidoError(f"O vertice {vf} não está no grafo")
        
        QNTVERT = len(self.vertices)

        for i in range(QNTVERT):
            for j in range(QNTVERT):
                if len(self.matriz[i][j]) > 0:
                    for a in self.matriz[i][j]:
                        if self.matriz[i][j][a].peso < 0:
                            raise MatrizInvalidaError("Para essa função a matriz não pode ter peso negativo")
                        
        visitados = set()
        # rotulo, distancia e previous
        # nao_visitados = list([a.rotulo, ] for a in self.vertices)



                    
        