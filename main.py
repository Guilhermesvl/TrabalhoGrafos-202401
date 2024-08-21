#Guilherme Henrique Silva Barbara - 202120499


from collections import deque

class LA:
    def __init__(self, vertices, arestas, direcionado):
        self.vertices = vertices
        self.arestas = arestas
        self.la = [[] for _ in range(len(self.vertices))]
        self.direcionado = direcionado

    def addAdjacencia(self):
        for idArestas, u, v, w in self.arestas:
            self.la[u].append((v, w, idArestas)) #LA[U] -> (v, w, id)

            if not self.direcionado:    #La[u] 
                self.la[v].append((u, w, idArestas)) #LA[v] -> (u, w, id) 

    def mostraLista(self): 
        for i in range(len(self.vertices)):
            print(f'{i}: ', end=' ')
            for  adjacencia, peso, idAresta in self.la[i]:
                print(f'{idAresta} -> {adjacencia}({peso})')
            print()

    def getDirecionado(self):
        return self.direcionado
    
    def getVertices(self):
        return self.vertices
    
    def getArestas(self):
        return self.arestas
    
    #1 (✔)
    def conexo(self):
        """
        Verifica se o grafo é conexo.

        Este método realiza uma busca em largura para determinar se o grafo é conexo, ou seja,
        se todos os vértices do grafo estão acessíveis a partir de qualquer outro vértice. Se o grafo 
        tiver mais de uma componente conectada, ele não é conexo.

        Retorna:
            int: 
                - Retorna 1 se o grafo for conexo.
                - Retorna 0 se o grafo for desconexo.
        """


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
                    for adjacencia, _, _  in self.la[u]:
                        if not visitados[adjacencia]:
                            visitados[adjacencia] = True
                            fila.append(adjacencia)
                            
        return 0 if componente > 1 else 1
    
    #2 (✔)
    def bipartido(self):
        """
        Verifica se o grafo é bipartido.

        Este método utiliza uma busca em largura para determinar se o grafo é bipartido, ou seja, 
        se os vértices do grafo podem ser divididos em dois conjuntos disjuntos, de modo que não haja 
        arestas entre vértices do mesmo conjunto. Se o grafo possuir um ciclo de comprimento ímpar, 
        ele não será bipartido.

        Retorna:
            int:
                - Retorna 1 se o grafo for bipartido.
                - Retorna 0 se o grafo não for bipartido.
        """
        
        cor = [-1] * len(self.vertices)

        for inicio in range(len(self.vertices)):
            if cor[inicio] == -1:
                cor[inicio] = 0
                fila = deque([inicio])

                while fila:
                    u = fila.popleft()
                    for adjacencia, _, _ in self.la[u]:
                        if cor[adjacencia] == -1:
                            cor[adjacencia] = 1 - cor[u]
                            fila.append(adjacencia)
                        elif cor[adjacencia] == cor[u]:
                            return 0
        return 1

    #3 (✔)
    def euleriano(self):
        """
        Verifica se o grafo é euleriano.

        Um grafo é euleriano se contém um ciclo euleriano, ou seja, um ciclo que percorre todas as arestas
        sem repeti-las.

        Para um grafo direcionado:
            - O grafo é euleriano se for fortemente conexo e se o grau de entrada de cada vértice for igual 
            ao seu grau de saída.

        Para um grafo não direcionado:
            - O grafo é euleriano se todos os vértices tiverem graus pares e se o grafo for conexo.

        Retorna:
            int:
                - Retorna 1 se o grafo for euleriano.
                - Retorna 0 se o grafo não for euleriano.
        """
        if self.direcionado:
            if self.componentesFortementeConexas() > 1:
                return 0  

            grauEntrada = [0] * len(self.vertices)
            grauSaida = [0] * len(self.vertices)

            for u in range(len(self.vertices)):
                for v, _, _ in self.la[u]:
                    grauSaida[u] += 1
                    grauEntrada[v] += 1

            for i in range(len(self.vertices)):
                if grauEntrada[i] != grauSaida[i]:
                    return 0  

            return 1 
        
        #Para grafos não orientados
        else:
            for adjacencias in self.la:
                if len(adjacencias) % 2 != 0:
                    return 0
            
            if not self.conexo():
                return 0
            
            return 1

    
    #4 (✔)
    def detectaCicloDirecionado(self):
        """
        Detecta a presença de ciclos em um grafo direcionado usando uma busca em profundidade.

        O método usa uma abordagem de busca em profundidade para detectar ciclos em um grafo direcionado.
        A ideia é marcar os vértices com três estados durante a busca:
        - 0: Não Visitado
        - 1: Visitando (parte da pilha de recursão atual)
        - 2: Visitado (já completado a busca)

        Um ciclo é detectado se, durante a DFS, for encontrado um vértice que está no estado 1 (Visitando),
        indicando que há um retorno para um vértice que ainda está na pilha de recursão atual.

        O algoritmo é executado para cada vértice não visitado para garantir que ciclos em diferentes componentes
        do grafo também sejam detectados.

        Retorna:
            int:
                - Retorna 1 se um ciclo for detectado no grafo direcionado.
                - Retorna 0 se nenhum ciclo for encontrado.
        """
        
        estado = [0] * len(self.vertices)  # 0 = Não Visitado, 1 = Visitando, 2 = Visitado

        def dfs(v):
            if estado[v] == 1:  
                return True 
            if estado[v] == 2:  
                return False

            estado[v] = 1 
            for adjacencia, _, _ in self.la[v]:
                if dfs(adjacencia):
                    return True
            estado[v] = 2  
            return False

        
        for v in range(len(self.vertices)):
            if estado[v] == 0 and dfs(v):
                return 1  
        return 0 

    def detectaCicloNaoDirecionado(self):
        """
        Detecta a presença de ciclos em um grafo não direcionado usando uma busca em profundidade.

        O método utiliza uma abordagem de busca em profundidade para identificar ciclos em um grafo não direcionado.
        Durante a busca, um ciclo é detectado se for encontrado um vértice que já foi visitado e que não é o pai do
        vértice atual, indicando que há uma aresta que forma um ciclo.

        O algoritmo marca os vértices com dois atributos principais:
        - `visitados`: Para rastrear se um vértice foi visitado durante a busca.
        - `pais`: Para rastrear o pai de cada vértice na árvore de busca em profundidade.

        Retorna:
            int:
                - Retorna 1 se um ciclo for detectado no grafo não direcionado.
                - Retorna 0 se nenhum ciclo for encontrado.
        """

        visitados = [False] * len(self.vertices)
        pais = [-1] * len(self.vertices) 

        def dfs(v, pai):
            visitados[v] = True
            for adjacencia, _ , _ in self.la[v]:
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
        """
        Calcula o número de componentes fortemente conexas em um grafo direcionado.
        Este método usa o algoritmo de Kosaraju, que realiza duas passagens de DFS:
        uma no grafo original para calcular a ordem de finalização e outra no grafo transposto
        para identificar as componentes.
        
        Retorna:
            int: O número de Componentes Fortemente Conexas no grafo. Retorna -1 se o grafo não for direcionado.
        """

        #Teste apenas para grafos não direcionados
        if self.direcionado == True:
            return -1
        
        componente = 0
        visitados = [False] * len(self.vertices)
        fila = deque()

        for source in range(len(self.vertices)):
            if not visitados[source]:
                componente+=1
                visitados[source] = True
                fila.append(source)

                while fila:
                    u = fila.popleft()
                    for adjacencia, _ , _ in self.la[u]:
                        if not visitados[adjacencia]:
                            visitados[adjacencia] = True
                            fila.append(adjacencia)

        return componente

    #6 (✔)
    def componentesFortementeConexas(self):
        """
        Detecta e conta o número de componentes fortemente conexas em um grafo direcionado.

        Este método utiliza o algoritmo de Kosaraju para encontrar componentes fortemente conexas em um grafo
        direcionado. O algoritmo realiza duas passagens de DFS para identificar todas as componentes:

        1. **Primeira Passagem**:
            - Realiza uma DFS no grafo original para obter a ordem de fechamento dos vértices.
            - Os vértices são adicionados à lista `fechamento` na ordem em que são completamente explorados.

        2. **Preparação do Grafo Transposto**:
            - Cria o grafo transposto (ou grafo inverso) onde todas as arestas são invertidas.
            - Este grafo é usado para encontrar os componentes fortemente conexos na segunda passagem.

        3. **Segunda Passagem**:
            - Realiza uma DFS no grafo transposto usando a ordem de fechamento obtida na primeira passagem.
            - Cada vez que uma nova DFS é iniciada, uma nova componente fortemente conexa é identificada.

        Retorna:
            int:
                - Retorna o número de componentes fortemente conexas encontradas no grafo direcionado.
                - Retorna -1 se o grafo não for direcionado (não é aplicável para grafos não direcionados).
        """

        #Apenas para grafos direcionados
        if not self.direcionado:
            return -1
        
        def dfs(u, visitados, fechamento):

            visitados[u] = True
            for v, _, _ in self.la[u]:
                if not visitados[v]:
                    dfs(v, visitados, fechamento)
            fechamento.append(u)  

        def dfsTransposto(u, visitados, componenteAtual):
            visitados[u] = True
            componenteAtual.append(u)
            for v, _, _ in self.transposto[u]:
                if not visitados[v]:
                    dfsTransposto(v, visitados, componenteAtual)

        visitados = [False] * len(self.vertices)
        fechamento = []
        
        for u in range(len(self.vertices)):
            if not visitados[u]:
                dfs(u, visitados, fechamento)

        self.transposto = [[] for _ in range(len(self.vertices))]
        for u in range(len(self.vertices)):
            for v, w, idArestas in self.la[u]:
                self.transposto[v].append((u, w, idArestas))


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

    #7 (✔)
    def verticeArticulação(self):
        """
        Identifica e imprime os vértices de articulação em um grafo não direcionado.

        Este método usa o algoritmo de Tarjan para encontrar vértices de articulação. O algoritmo realiza uma busca em profundidade e utiliza dois vetores auxiliares:
        - `descoberta`: Armazena o tempo de descoberta de cada vértice durante a DFS.
        - `low`: Armazena o menor tempo de descoberta alcançável a partir de um vértice, considerando suas arestas e as arestas de seus descendentes na DFS.

        A busca é realizada da seguinte forma:
        1. **Inicialização**:
            - Define os vetores `visitado`, `descoberta`, e `low` como não visitado e inicializa `tempo` e a lista de vértices de articulação.
        2. **DFS**:
            - Para cada vértice não visitado, realiza uma DFS recursiva.
            - Atualiza os vetores `descoberta` e `low` durante a exploração.
            - Identifica vértices de articulação com base em condições específicas:
                - Se o vértice for a raiz da DFS e tiver mais de um filho, é um vértice de articulação.
                - Se o vértice não for a raiz e se o menor tempo de descoberta do vizinho é maior ou igual ao tempo de descoberta do vértice, é um vértice de articulação.
        3. **Impressão**:
            - Ordena e imprime os vértices de articulação encontrados.

        Retorno:
            None - para que a saída fique de acordo com os resultados do beecrownd
            (Em formato de int oriundo do print, e não o retorno de uma lista, por exemplo)

        """
        #Apenas para grafos não-direcionados
        if self.direcionado:
            return -1
        
        def dfs(vertice, pai):
            nonlocal tempo
            filhos = 0
            visitado[vertice] = True
            descoberta[vertice] = low[vertice] = tempo
            tempo += 1
            
            for vizinho, _, _ in sorted(self.la[vertice]):
                if not visitado[vizinho]:  
                    filhos += 1
                    dfs(vizinho, vertice)
                    low[vertice] = min(low[vertice], low[vizinho])
                    
                    if pai is None and filhos > 1:
                        verticesArticulacao.append(vertice)
                    if pai is not None and low[vizinho] >= descoberta[vertice]:
                        verticesArticulacao.append(vertice)
                elif vizinho != pai:  
                    low[vertice] = min(low[vertice], descoberta[vizinho])
        
        visitado = [False] * len(self.vertices)
        descoberta = [-1] * len(self.vertices)
        low = [-1] * len(self.vertices)
        verticesArticulacao = []
        tempo = 0
        
        for i in range(len(self.vertices)):
            if not visitado[i]:
                dfs(i, None)
        
        for vertices in sorted(verticesArticulacao):
            print(vertices, end = " ")

        return None

    #8
    def arestasPonte(self):
        """
        Identifica e conta as arestas de ponte em um grafo não direcionado.

        Este método realiza uma busca em profundidade e utiliza dois vetores auxiliares:
        - `descoberta`: Armazena o tempo de descoberta de cada vértice durante a DFS.
        - `baixo`: Armazena o menor tempo de descoberta alcançável a partir de um vértice, considerando suas arestas e as arestas de seus descendentes na DFS.

        O processo é realizado da seguinte forma:
        1. **Inicialização**:
            - Define os vetores `visitado`, `descoberta`, e `baixo`, inicializa a lista de pontes e outras variáveis auxiliares.
        2. **DFS**:
            - Para cada vértice não visitado, realiza uma DFS recursiva.
            - Atualiza os vetores `descoberta` e `baixo` durante a exploração.
            - Identifica arestas de ponte com base na condição:
                - Se `baixo[vizinho] > descoberta[vertice]`, a aresta `(vertice, vizinho)` é uma aresta de ponte.
        3. **Contagem**:
            - Retorna o número de arestas de ponte encontradas.

        Retorno:
            int: Número de arestas de ponte no grafo. Retorna -1 se o grafo for direcionado.

        """
        #Apenas para grafos não-direcionados
        if self.direcionado == True:
            return -1
        
        def dfs(vertice, pai):
            nonlocal tempo
            visitado[vertice] = True
            descoberta[vertice] = baixo[vertice] = tempo
            tempo += 1
            
            for vizinho, _, _  in sorted(self.la[vertice]):
                if not visitado[vizinho]:
                    filhos[0] += 1
                    pilha.append((vertice, vizinho)) 
                    dfs(vizinho, vertice)
                    baixo[vertice] = min(baixo[vertice], baixo[vizinho])
                    
                    if baixo[vizinho] > descoberta[vertice]:
                        pontes.add((vertice, vizinho))
                elif vizinho != pai:
                    baixo[vertice] = min(baixo[vertice], descoberta[vizinho])

        visitado = [False] * len(self.vertices)
        descoberta = [-1] * len(self.vertices)
        baixo = [-1] * len(self.vertices)
        pontes = set()
        pilha = []
        filhos = [0]
        tempo = 0
        
        for i in range(len(self.vertices)):
            if not visitado[i]:
                dfs(i, None)
        
        return len(pontes)

    #Gerar ------------------------------------------------------------------------
    #9 (✔)

    def profundidade(self):
        """
        Realiza uma busca em profundidade a partir do vértice inicial (vértice 0) em um grafo dirigido ou não dirigido.
        Garante que as arestas sejam visitadas e retornadas na ordem lexicográfica dos vértices adjacentes.

        A função realiza a seguinte operação:
        1. Ordena as adjacências de cada vértice na ordem dos vértices de destino.
        2. Realiza uma DFS a partir do vértice 0.
        3. Coleta e imprime os IDs das arestas visitadas durante a DFS.

        A função segue os seguintes passos:
        - Inicializa uma lista de visitados para garantir que cada vértice seja visitado apenas uma vez.
        - Ordena as adjacências dos vértices para garantir que a DFS respeite a ordem lexicográfica.
        - Realiza a busca em profundidade (DFS), registrando os IDs das arestas conforme elas são visitadas.
        - Imprime os IDs das arestas visitadas na ordem em que foram exploradas.

        Returns:
            None
            print: os id's das arestas visitadas
    """    
        def dfs(u, visitados, arestasFinais):
            
            adjacencias = sorted(self.la[u], key=lambda x : (x[0], x[2]))
            visitados[u] = True
            for v, _, idArestas in adjacencias:
                if not visitados[v]:
                    arestasFinais.append(idArestas)
                    dfs(v, visitados, arestasFinais)
                    

        visitados = [False] * len(self.vertices)
        arestasFinais = []

        dfs(0, visitados, arestasFinais)
        
        
        for resultado in arestasFinais:
            print(resultado, end = ' ')
        
    #10 (✔)
    def largura(self):

        """
        Realiza uma busca em largura (BFS) a partir do vértice inicial (vértice 0) em um grafo dirigido ou não dirigido.
        Garante que as arestas sejam visitadas e retornadas na ordem lexicográfica dos vértices adjacentes e dos IDs das arestas.

        A função realiza a seguinte operação:
        1. Inicializa uma fila e uma lista de visitados para gerenciar os vértices a serem explorados e os que já foram visitados.
        2. Realiza uma BFS a partir do vértice 0.
        3. Coleta e imprime os IDs das arestas visitadas durante a BFS.

        A função segue os seguintes passos:
        - Adiciona o vértice inicial (0) à fila e marca-o como visitado.
        - Enquanto houver vértices na fila, remove o vértice da fila e explora seus vizinhos.
        - Ordena as adjacências dos vértices para garantir que a BFS respeite a ordem lexicográfica dos vértices adjacentes.
        - Adiciona os vizinhos não visitados à fila e marca-os como visitados.
        - Registra os IDs das arestas conforme elas são visitadas e adiciona esses IDs à lista de resultados.

        Returns:
            None
            print: os id's das arestas visitadas
    """
        visitados = [False] * len(self.vertices)
        fila = deque()
        arestasFinais = []

        def bfs(source):
            fila.append(source)
            visitados[source] = True

            while fila:
                u = fila.pop()
                adjacencias = sorted(self.la[u], key = lambda x: (x[0], x[2]))

                for v, _, idAresta in adjacencias:
                    if not visitados[v]:
                        #idAresta = self.getIdArestas(u, v, w)
                        fila.append(v)
                        visitados[v] = True
                        arestasFinais.append(idAresta)

        bfs(0)

        for resultado in arestasFinais:
            print(resultado, end = ' ')
        
        
    #11 (✔)
    def geradoraMinima(self):
        """
        Calcula o peso total da árvore geradora mínima (MST) para um grafo não direcionado.

        Este método utiliza o Algoritmo de Kruskal para encontrar a MST.

        O processo é realizado da seguinte forma:
        1. **Ordenação das Arestas**:
            - Ordena todas as arestas do grafo em ordem crescente de peso.
        2. **Inicialização**:
            - Inicializa estruturas para o Union-Find: `pai` e `rank`.
        3. **Construção da MST**:
            - Itera sobre as arestas ordenadas e adiciona as arestas à MST se não formarem um ciclo (usando o Union-Find).
            - Calcula o peso total das arestas incluídas na MST.
        4. **Retorno**:
            - Retorna o peso total da MST.

        Retorno:
            int: O peso total da árvore geradora mínima. Retorna -1 se o grafo for direcionado.

        
        """
        #Apenas para grafos não-direcionados
        if self.direcionado: 
            return -1
        
        def encontrar(pai, vertice):
            if pai[vertice] != vertice:
                pai[vertice] = encontrar(pai, pai[vertice])

            return pai[vertice]

        def uniao(pai, rank, raizV, raizU):
            if rank[raizU] < rank[raizV]:
                pai[raizU] = raizV
            elif rank[raizU] > rank[raizV]:
                pai[raizV] = raizU
            else:
                pai[raizV] = raizU
                rank[raizU] += 1


        arestasOrdenadas = sorted(self.getArestas(), key = lambda x:x[3])

        pai = []
        rank = []

        for v in range(len(self.vertices)):
            pai.append(v)
            rank.append(0)

        pesosTotal = 0
        iArestasOrdenadas = 0
        numeroArestas = 0
        parada = len(self.vertices)

        while numeroArestas < parada - 1 and iArestasOrdenadas < len(arestasOrdenadas):
            _, u, v, w = arestasOrdenadas[iArestasOrdenadas]

            iArestasOrdenadas+= 1

            raizU = encontrar(pai, u)
            raizV = encontrar(pai, v)

            if raizU != raizV:
                numeroArestas += 1
                pesosTotal += w

                uniao(pai, rank, raizV, raizU)

        return pesosTotal

        
    #12 (✔)
    def ordemTopologica(self):

        """
        Realiza a ordenação topológica de um grafo direcionado.

        O processo é realizado da seguinte forma:
        1. **Inicialização**:
            - Inicializa listas para marcar os vértices visitados e verificar a pilha recursiva.
        2. **Busca em Profundidade (DFS)**:
            - Executa DFS para cada vértice não visitado, construindo a ordenação topológica e detectando ciclos.
        3. **Detecção de Ciclos**:
            - Durante a DFS, verifica se há ciclos no grafo. Se um ciclo é detectado, a ordenação topológica não é possível.
        4. **Construção da Ordenação**:
            - Adiciona vértices à lista de ordenação no final da DFS e inverte a lista para obter a ordenação correta.

        Retorno:
            None - para que a saída fique de acordo com os resultados do beecrownd
            (Em formato de int oriundo do print, e não o retorno de uma lista, por exemplo)
            list[int] | int: Retorna a lista de vértices na ordem topológica se o grafo não contiver ciclos. 
            Retorna -1 se o grafo contiver ciclos, indicando que a ordenação topológica não é possível.

    """
        #Apenas para grafos direcionados
        if self.direcionado == False:
            return -1
        
        def dfs(u, visitados, ordem, pilhaRecursiva):
            visitados[u] =  True
            pilhaRecursiva[u] = True
            
            adjacencias = sorted(self.la[u], key=lambda x : (x[0], x[1]))

            for v, _, _ in adjacencias:
                if not visitados[v]:
                    if dfs(v, visitados, ordem, pilhaRecursiva):
                        return True
                    
                elif pilhaRecursiva[v]:
                    return True #foi detectado um ciclo
                
            pilhaRecursiva[u] = False
            ordem.append(u)
            return False

        visitados = [False] * len(self.vertices)
        pilhaRecursiva = [False] * len(self.vertices)
        ordem = []
        
        for u in sorted(range(len(self.vertices))):
            if not visitados[u]:
                if dfs(u, visitados, ordem, pilhaRecursiva):
                    return -1   


        ordem.reverse()    
        for i in ordem:
            print(i, end = ' ')     

        return None

    #13 (✔)
    def caminhoMinimo(self):
        """
        Calcula o caminho mínimo em um grafo ponderado não direcionado utilizando o algoritmo de Bellman-Ford.

        O algoritmo de Bellman-Ford é utilizado para encontrar o caminho mais curto de um vértice de origem a todos os 
                                        outros vértices em um grafo ponderado,

        O processo é realizado da seguinte forma:
        1. **Inicialização**:
            - Define a distância inicial de todos os vértices como infinito (`inf`), exceto a distância do vértice de origem, 
                                                    que é definida como 0.
        2. **Relaxamento das Arestas**:
            - Executa o relaxamento das arestas para ajustar as distâncias mais curtas possíveis para cada vértice.
        3. **Detecção de Ciclos de Peso Negativo**:
            - Verifica se ainda há caminhos que podem ser reduzidos, o que indicaria a presença de 
                                    um ciclo de peso negativo no grafo.
        4. **Retorno do Resultado**:
            - Retorna a distância do vértice de origem ao vértice de destino. 
            Se a distância final for `inf`, indica que o vértice de destino não é alcançável a partir do vértice de origem e retorna -1.

        Retorno:
            int: Retorna a distância mínima do vértice de origem ao vértice de destino se o caminho for encontrado. 
            Retorna -1 se o caminho não existir ou se um ciclo de peso negativo for detectado.

    """
        #Apenas para grafos não direcionados
        if self.direcionado:
            return -1
        
        source = 0
        destino = len(self.vertices) - 1 

        distancia = [float('inf')] * len(self.vertices)
        distancia[source] = 0

        def relaxamento(u, v, w):
            if distancia[u] + w < distancia[v]:
                distancia[v] = distancia[u] + w

        
        for _ in range(destino):
            for u in range(len(self.vertices)):
                for v, w,_ in self.la[u]:
                    relaxamento(u, v, w)

        
        for u in range(destino):
            for v, w,_ in self.la[u]:
                if distancia[u] + w < distancia[v]:
                    return -1 #ciclo de peso negativo
                

        return distancia[destino] if distancia[destino] != float('inf') else -1


    #14 (✔)
    def fluxoMaximo(self):
        """
        Calcula o fluxo máximo de um grafo direcionado utilizando o algoritmo de Ford-Fulkerson com busca em largura.

        O algoritmo de Ford-Fulkerson é utilizado para encontrar o fluxo máximo em uma rede de fluxo

        O processo é realizado da seguinte forma:
        1. **Inicialização**:
            - Define o vértice de origem (`s`) como o primeiro vértice (índice 0) e o vértice de destino (`t`) como o último vértice na lista.
            - Cria uma matriz de capacidade residual (`rg`) inicializada com as capacidades das arestas do grafo.
        2. **Busca em Largura (BFS)**:
            - Implementa uma busca em largura para encontrar um caminho de aumento do vértice de origem ao vértice de destino. 
                                Se encontrado, atualiza o fluxo e as capacidades residuais.
        3. **Atualização do Fluxo**:
            - Calcula o fluxo possível pelo caminho encontrado e atualiza as capacidades residuais das arestas.
        4. **Retorno do Resultado**:
            - Retorna o fluxo máximo total encontrado.

        Retorno:
            int: Retorna o valor do fluxo máximo possível do vértice de origem ao vértice de destino.
              Retorna -1 se o grafo não for direcionado, pois o algoritmo de Ford-Fulkerson é adequado apenas para grafos direcionados.
    """
        #Apenas para grafos não-direcionados
        if self.direcionado == False:
            return -1
        
        s = 0
        t = len(self.vertices) - 1

        def bfs(rg, s, t, pais):
            visitado = [False] * len(self.vertices)
            fila = deque([s])
            visitado[s] = True

            while fila:
                u = fila.popleft()

                for v in range(len(rg[u])):
                    if not visitado[v] and rg[u][v] > 0:
                        fila.append(v)
                        visitado[v] = True
                        pais[v] = u

                        if v == t:
                            return True
            return False

        rg = [[0] * len(self.vertices) for _ in range(len(self.vertices))]
        for u in range(len(self.vertices)):
            for v, w,_ in self.la[u]:
                rg[u][v] = w

        pais = [-1] * len(self.vertices)
        fluxoMax = 0

        while bfs(rg, s, t, pais):
            caminhoFluxo = float('Inf')
            v = t

            while v != s:
                u = pais[v]
                caminhoFluxo = min(caminhoFluxo, rg[u][v])
                v = pais[v]

            v = t
            while v != s:
                u = pais[v]
                rg[u][v] -= caminhoFluxo
                rg[v][u] += caminhoFluxo
                v = pais[v]

            fluxoMax += caminhoFluxo

        return fluxoMax
    
    #15 (✔)
    def fechoTransitivo(self):
        """
        Calcula o fecho transitivo do vértice de origem (índice 0) em um grafo direcionado.

        O fecho transitivo de um vértice é o conjunto de todos os vértices que podem ser alcançados a partir desse vértice através de uma série de arestas direcionadas. Este método usa uma busca em profundidade (DFS) para encontrar todos os vértices acessíveis a partir do vértice de origem e os retorna.

        O processo é realizado da seguinte forma:
        1. **Inicialização**:
            - Cria um conjunto `fecho` para armazenar os vértices do fecho transitivo, garantindo que não haja duplicatas.
            - Cria uma lista `visitado` para marcar os vértices que já foram visitados durante a busca.
        2. **Busca em Profundidade (DFS)**:
            - Implementa uma DFS que começa no vértice de origem (índice 0) e explora todos os vértices alcançáveis a partir dele. Os vértices encontrados são adicionados ao conjunto `fecho`.
        3. **Exibição do Resultado**:
            - Imprime todos os vértices no conjunto `fecho` em ordem crescente.

        Retorno:
            int: Retorna -1 se o grafo não for direcionado, pois o fecho transitivo é calculado apenas para grafos direcionados.

        Observações:
            - O método supõe que o grafo é direcionado e que a lista de adjacência `self.la` está corretamente representada.
            - O fecho transitivo é impresso na saída padrão em ordem crescente dos vértices.

        Exceções:
            - O método assume que o grafo é direcionado. Se não for, o método retorna -1.

        """

        #Apenas para grafos não-direcionados
        if self.direcionado == False:
            return -1

        
        fecho = set() #Evita dupliações
        visitado = [False] * len(self.vertices)  

        def dfs(v):
            visitado[v] = True
            fecho.add(v)
            for vizinho,_, _ in sorted(self.la[v]): 
                if not visitado[vizinho]:
                    dfs(vizinho)

        dfs(0)  

        for i in fecho:
            print(i, end = ' ')


def menu(qtVertices, qArestas, orientado, operacoes):
    arestas = []
    for _ in range(qArestas):
        idArestas, u, v, w = map(int, input().split())
        arestas.append((idArestas, u, v, w))

    lista = LA(list(range(qtVertices)), arestas, orientado == 'direcionado')
    lista.addAdjacencia()

    #lista.mostraLista() #----- Só para ver se esta adicionando da forma certa

    if operacoes[0] == 0:
        operacoes = [indice + 1 for indice in operacoes]

    
    for i in operacoes:

        if i == 1:
            conexo = lista.conexo()
            print(conexo) #1

        elif i == 2:    
            bipartido = lista.bipartido()
            print(bipartido) #2

        elif i == 3:
            euleriano = lista.euleriano()
            print(euleriano) #3

        elif i == 4:
            if lista.getDirecionado():
                ciclo = lista.detectaCicloDirecionado() #4
            else: 
                ciclo = lista.detectaCicloNaoDirecionado() #4
            print(ciclo)

        elif i == 5:
            componente = lista.componentesConexas() #5 
            print(componente)

        elif i == 6:
            componenteFortemente = lista.componentesFortementeConexas() #6
            print(componenteFortemente)

        elif i == 7:
            verticerticulacao = lista.verticeArticulação() #7
            print(verticerticulacao)

        elif i == 8:
            arestaPonte = lista.arestasPonte() #8
            print(arestaPonte)
        
        elif i == 9:
            profundidade = lista.profundidade() #9
            print()

        elif i == 10:
            largura = lista.largura() #10 
            print()

        elif i == 11:
            geradora = lista.geradoraMinima() #11
            print(geradora)

        elif i == 12:
            ordenacaoTopologica = lista.ordemTopologica() #12
            print(ordenacaoTopologica)

        elif i == 13:
            caminhoMinimo = lista.caminhoMinimo() #13
            print(caminhoMinimo)
        
        elif i == 14:
            fluxoMaximo = lista.fluxoMaximo() #14
            print(fluxoMaximo)

        elif i == 15:
            fechoTransitivo = lista.fechoTransitivo() #15
            print(fechoTransitivo)



operacoes = list(map(int, input().split()))
qtVertices, qArestas = map(int, input().split())
orientado = str(input())

menu(qtVertices, qArestas, orientado, operacoes)
