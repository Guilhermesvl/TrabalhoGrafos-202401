from collections import deque

class LA:
    def __init__(self, vertices, arestas, direcionado):
        self.vertices = vertices
        self.arestas = arestas
        self.la = [[] for _ in range(len(self.vertices))]
        self.direcionado = direcionado

    def addAdjacencia(self):
        for u, v, w in self.arestas:
            self.la[u].append((v, w))

            if not self.direcionado:
                self.la[v].append((u, w))

    def mostraLista(self):
        for i in range(len(self.vertices)):
            print(f'{i}: ', end=' ')
            for adjacencia, peso in self.la[i]:
                print(f'{adjacencia}({peso}) -> ', end='')
            print()

    def getVertices(self):
        return self.vertices
    
    def getArestas(self):
        return self.arestas
    
    #1
    def conexo(self):
        componente = 0
        visitados = [False] * len(self.vertices)
        fila = deque()

        for source in range(len(self.vertices)):
            if not visitados[source]:
                componente += 1
                visitados[source] = True
                fila.append(source)

                while fila:
                    u = fila.popleft()
                    for adjacencia, _ in self.la[u]:
                        if not visitados[adjacencia]:
                            visitados[adjacencia] = True
                            fila.append(adjacencia)
            
        return 0 if componente > 1 else 1
    
    #2
    def bipartido(self):
        print()

    #3
    def euleriano(self):
        print()
    
    #4
    def possuiCiclo(self):
        print()
    
    ## Listar -------------------------------------------------------------------
    #5
    def componentesConexas(self):
        print()

    #6
    def componentesFortementeConexas(self):
        print()
    
    #7
    def trilhaEuleriana(self):
        print()

    #8
    def verticeArticulação(self):
        print()

    #9
    def arestasPonte(self):
        print()

    #Gerar ------------------------------------------------------------------------
    #10
    def profundidade(self):
        print()
    #11
    def largura(self):
        print()

    #12
    def geradoraMinima(self):
        print()

    #13
    def ordemTopologica(self):
        print()

    #14
    def caminhoMinimo(self):
        print()

    #15
    def fluxoMaximo(self):
        print()

    #16
    def fechoTransitivo(self):
        print()

def menu(qtVertices, qArestas, orientado):
    arestas = []
    for _ in range(qArestas):
        idArestas, u, v, w = map(int, input().split())
        arestas.append((idArestas, u, v, w))

    lista = LA(list(range(qtVertices)), arestas, orientado == 'direcionado')
    lista.addAdjacencia()
    lista.mostraLista()
    conexo = lista.conexo()
    print(conexo)


qtVertices, qArestas = map(int, input().split())
orientado = str(input())

menu(qtVertices, qArestas, orientado)
