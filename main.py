from collections import deque

class LA:
    def __init__(self, vertices, arestas, direcionado):
        self.vertices = vertices
        self.arestas = arestas
        self.la = [[] for _ in range(len(self.vertices))]
        self.direcionado = direcionado

    def addAdjacencia(self):
        for idArestas, u, v, w in self.arestas:
            self.la[u].append((v, w))

            if not self.direcionado:
                self.la[v].append((u, w))

    def mostraLista(self):
        for i in range(len(self.vertices)):
            print(f'{i}: ', end=' ')
            for adjacencia, peso in self.la[i]:
                print(f'{adjacencia}({peso}) -> ', end='')
            print()

    def getDirecionado(self):
        return self.direcionado
    def getVertices(self):
        return self.vertices
    
    def getArestas(self):
        return self.arestas
    
    #1 (✔)
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
        cor = [-1] * len(self.vertices)

        for inicio in range(len(self.vertices)):
            if cor[inicio] == -1:
                cor[inicio] = 0
                fila = deque([inicio])

                while fila:
                    u = fila.popleft()
                    for adjacencia, _ in self.la[u]:
                        if cor[adjacencia] == -1:
                            cor[adjacencia] = 1 - cor[u]
                            fila.append(adjacencia)
                        elif cor[adjacencia] == cor[u]:
                            return 0
        return 1

    #3 (✔)
    def euleriano(self):
        if self.direcionado ==  True:
            return -1
        
        for adjacencias in self.la:
            if len(adjacencias) % 2 != 0:
                return 0
        return 1

    
    #4 (✔)
    def detectaCicloDirecionado(self):
        estado = [0] * len(self.vertices)  # 0 = Não Visitado, 1 = Visitando, 2 = Visitado

        def dfs(v):
            if estado[v] == 1:  
                return True
            if estado[v] == 2:  
                return False

            estado[v] = 1 
            for adjacencia, _ in self.la[v]:
                if dfs(adjacencia):
                    return True
            estado[v] = 2  
            return False

        
        for v in range(len(self.vertices)):
            if estado[v] == 0 and dfs(v):
                return 1  
        return 0 

    def detectaCicloNaoDirecionado(self):
        visitados = [False] * len(self.vertices)
        pais = [-1] * len(self.vertices) 

        def dfs(v, pai):
            visitados[v] = True
            for adjacencia, _ in self.la[v]:
                if not visitados[adjacencia]:
                    pais[adjacencia] = v
                    if dfs(adjacencia, v):
                        return True
                elif adjacencia != pai:  
                    return True
            return False

        
        for v in range(len(self.vertices)):
            if not visitados[v]:
                if dfs(v, -1):
                    return 1  
        return 0  
    
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
    print(conexo) #1

    bipartido = lista.bipartido()
    print(bipartido) #2

    euleriano = lista.euleriano()
    print(euleriano) #3

    if lista.getDirecionado():
        ciclo = lista.detectaCicloDirecionado() #4
    else: 
        ciclo = lista.detectaCicloNaoDirecionado() #4
    print(ciclo)



qtVertices, qArestas = map(int, input().split())
orientado = str(input())

menu(qtVertices, qArestas, orientado)
