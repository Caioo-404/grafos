from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        naoAdj = set()
        vertex = self.vertices
        adjacencias = [{a.v1.rotulo, a.v2.rotulo} for a in self.arestas.values()]
        TAMVERTEX = len(vertex)

        
        for i in range(TAMVERTEX - 1):
            for j in range(i + 1, TAMVERTEX):
                if {vertex[i].rotulo, vertex[j].rotulo} not in adjacencias:
                    naoAdj.add(f"{vertex[i].rotulo}-{vertex[j].rotulo}")

        return naoAdj
        #OK

    def ha_laco(self):
        ''' 
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.arestas:
            # print(self.arestas[a])
            if self.arestas[a].v1 == self.arestas[a].v2:
                return True;
        return False;
        #OK

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not(self.existe_rotulo_vertice(V)) : raise VerticeInvalidoError(f"O vertice {V} não está no grafo")

        grau = 0
        for a in self.arestas:
            if self.arestas[a].v1.rotulo == self.arestas[a].v2.rotulo and V == self.arestas[a].v1.rotulo:
                grau += 2
            elif self.arestas[a].v1.rotulo == V or self.arestas[a].v2.rotulo == V:
                grau += 1
        return grau
        #OK

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        ini = 1
        listaKeys = list(self.arestas.keys())
        #print(f"{len(listaKeys)} | {listaKeys} \n\n")
        #print(self.arestas)

        for i in range(len(listaKeys) - 1):
            for j in range(ini, len(listaKeys)):
                if self.arestas[listaKeys[i]] == self.arestas[listaKeys[j]]:
                    return True
            ini += 1
        return False
        #OK

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not(self.existe_rotulo_vertice(V)) : raise VerticeInvalidoError(f"O vertice {V} não está no grafo")
        adjacentes = set()
        for i in self.arestas:
            if self.arestas[i].v1.rotulo == V or self.arestas[i].v2.rotulo == V:
                adjacentes.add(self.arestas[i].rotulo)
        return adjacentes
        #OK

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_paralelas() or self.ha_laco() or (len(self.vertices_nao_adjacentes()) > 0):
            return False
        return True
        #OK

    def cria_grafoAdj(self):
        #Recriando o grafo como uma lista de adjacencia tipo: {'1': [], '4': [], '3': [], '2': []}
        grafoListaAdj = dict()
        for v in self.vertices:
            grafoListaAdj[v.rotulo] = list()

        for a in self.arestas.values():
            grafoListaAdj[a.v1.rotulo].append(a.v2.rotulo)
            grafoListaAdj[a.v2.rotulo].append(a.v1.rotulo)

        return grafoListaAdj


    def ha_ciclo(self):
        # Retornar True caso haja um ciclo no grafo
        
        grafoListaAdj = self.cria_grafoAdj()
        vertice = list(grafoListaAdj.keys())[0]

        #DFS para encontrar ciclo
        visitados = set()
        def dfsParaCiclo(v, pai):
            visitados.add(v)
    
            for vizin in grafoListaAdj[v]:
                if vizin not in visitados:
                    if dfsParaCiclo(vizin, v): # v -> pai 
                        return True # Volta true infinito
                    
                elif vizin != pai:
                    return True
            
            return False 
        
        #se o grafo for desconexo
        for vert in self.vertices:
            if vert not in visitados:
                if dfsParaCiclo(vertice, None):
                    return True
                
        return False
    

    def eh_arvore(self):
        #Vejo se tem ciclo
        if (self.ha_ciclo() == True): 
            return False
        
        grafoListaAdj = self.cria_grafoAdj()

        raiz = list(grafoListaAdj.keys())[0]
        folhas = list()
        visitados = set()

        def dfsEncontraFolha(v):
            visitados.add(v)
            #Ver se é folha
            if len(grafoListaAdj[v]) == 1 and v != raiz: 
                folhas.append(self.get_vertice(v))

            #Dfs padrao
            for vizin in grafoListaAdj[v]:
                if vizin not in visitados:
                    dfsEncontraFolha(vizin)
        

        dfsEncontraFolha(raiz)

        #Vendo se tá desconexo
        if (len(grafoListaAdj) != len(visitados)):
            return False
        
        return self.get_vertice(raiz), folhas
    

    def eh_bipartido(self):

        grafo = self.cria_grafoAdj()

        cores = dict()

        visitados = set();
        fila = list()
        fila.append(list(grafo.keys())[0])

        cores[fila[0]] = "branco"
        
        while fila:
            vertice = fila.pop(0)
            visitados.add(vertice)

            for v in grafo[vertice]:
                if v not in visitados:
                    if cores[vertice] == "branco":
                        cores[v] = "preto"
                    else:
                        cores[v] = "branco"

                    fila.append(v)
                    visitados.add(v)

                elif cores[v] == cores[vertice]:
                    return False; 
    
        return True

