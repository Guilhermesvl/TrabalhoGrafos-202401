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
    
    #2 (✔)
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

    #5 (✔)
    def componentesConexas(self):

        if self.direcionado:
            return -1
        
        componente = 0
        visitados = [False] * len(self.vertices)
        fila = deque()

        for source in range(len(self.vertices)):
            if not visitados[source]:
                componente+=1
                visitados[source-1] = True
                fila.append(source)

                while fila:
                    u = fila.popleft()
                    for adjacencia, _ in self.la[u]:
                        if not visitados[adjacencia]:
                            visitados[adjacencia] = True
                            fila.append(adjacencia)

        return componente

    #6 (✔)
    def componentesFortementeConexas(self):
        if not self.direcionado:
            return -1
        
        def dfs(u, visitados, fechamento):

            visitados[u] = True
            for v, _ in self.la[u]:
                if not visitados[v]:
                    dfs(v, visitados, fechamento)
            fechamento.append(u)  

        def dfsTransposto(u, visitados, componenteAtual):
            visitados[u] = True
            componenteAtual.append(u)
            for v, _ in self.transposto[u]:
                if not visitados[v]:
                    dfsTransposto(v, visitados, componenteAtual)

        visitados = [False] * len(self.vertices)
        fechamento = []
        
        for u in range(len(self.vertices)):
            if not visitados[u]:
                dfs(u, visitados, fechamento)

        self.transposto = [[] for _ in range(len(self.vertices))]
        for u in range(len(self.vertices)):
            for v, w in self.la[u]:
                self.transposto[v].append((u, w))


        visitados = [False] * len(self.vertices)
        componente = 0

        while fechamento:
            u = fechamento.pop()
            if not visitados[u]:
                componenteAtual = []
                dfsTransposto(u, visitados, componenteAtual)
                componente += 1

        return componente
    
    #7.1 -----EXTRA
    def trilhaEuleriana(self):
        print("EXTRA")

    #7
    def verticeArticulação(self):
        print("AINDA NÃO FIZ")

    #8
    def arestasPonte(self):
        print('AINDA NÃO FIZ')

    #Gerar ------------------------------------------------------------------------
    #9 (✔)
    def profundidade(self):
        
        def dfs(u, visitados, arestasFinais):
            visitados[u] = True

            adjacencias = sorted(self.la[u], key=lambda x : (x[0], x[1]))

            for v, w, in adjacencias:
                idArestas = getIdArestas(u, v, w)
                if not visitados[v]:
                    arestasFinais.append(idArestas)
                    dfs(v, visitados, arestasFinais)


        def getIdArestas(u, v, w):
            for idArestas, u_, v_, w_ in self.arestas:
                if(u == u_ and v == v_ and w == w_) or (not self.direcionado and 
                                                   u == v_ and v == u_ and w == w_):
                    return idArestas
            return None

        visitados = [False] * len(self.vertices)
        arestasFinais = []

        dfs(0, visitados, arestasFinais)

        for i in range(len(self.vertices)):
            if not visitados[i]:
                return arestasFinais
            
        return arestasFinais
    
    #10
    def largura(self):
        print()

    #11
    def geradoraMinima(self):
        print()

    #12
    def ordemTopologica(self):
        print()

    #13
    def caminhoMinimo(self):
        print()

    #14
    def fluxoMaximo(self):
        print()

    #15
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

    componente = lista.componentesConexas() #5 
    print(componente)

    componenteFortemente = lista.componentesFortementeConexas() #6
    print(componenteFortemente)

    verticerticulacao = lista.verticeArticulação() #7
    print(verticerticulacao)


    arestaPonte = lista.arestasPonte() #8
    print(arestaPonte)

    profundidade = lista.profundidade() #9
    print(profundidade)


qtVertices, qArestas = map(int, input().split())
orientado = str(input())

menu(qtVertices, qArestas, orientado)
