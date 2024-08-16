# TrabalhoGrafos-202401

## Sobre o projeto 
Este é um projeto idealizado pelo Professor Mayron Cesar de Oliveira Moreira, docente da disciplina de Algoritmos em Grafos da Universidade Federal de Lavras (UFLA) - 2024/01, desenvolvido pelo aluno Guilherme Henrique Silva Barbara (202120499) da turma 14A, que aborda os seguintes requisitos:

#### Objetivo

Implementar algoritmos para análise de propriedades de grafos, avançando gradualmente à medida que a disciplina progride.

## Descrição

### Casos de Teste

## Padrão de Leitura dos Grafos

O padrão de leitura dos grafos seguirá o seguinte formato:

#vertices #arestas
direcionado_ou_nao_direcionado
id_aresta vertice_u vertice_v peso_da_aresta
...


### Exemplo de Entrada

Considerando um grafo `G = (V, E)` não-direcionado e não-ponderado, onde:
- **V** = {0, 1, 2, 3}
- **E** = {(0, 1), (1, 2), (1, 3), (2, 3)}

A entrada seria:

4 4
nao_direcionado
0 0 1 1
1 1 2 1
2 1 3 1
3 2 3 1


## Regras de Submissão e Plágio

- **Plágio**: Qualquer tentativa de plágio na submissão implicará em **nota zero** para todos os membros dos grupos envolvidos.
- **Plágio Indireto**: Cuidado com o "plágio indireto", onde um grupo A copia a resposta de alguma fonte da web e outro grupo B, que não teve contato com o grupo A, copia do mesmo repositório.

## Funções a Serem Testadas

As seguintes funções devem ser implementadas e testadas:

### Verificar:

1. **Conexo** (conectividade fraca, em grafos orientados)
2. **Bipartido**
3. **Euleriano**
4. **Possui ciclo**

### Listar:

5. **Componentes conexas** (ordem lexicográfica)
6. **Componentes fortemente conexas** (ordem lexicográfica)
7. **Uma trilha Euleriana** (priorizando a ordem lexicográfica dos vértices)
8. **Vértices de articulação**
9. **Identificador das arestas ponte**

### Gerar:

10. **Árvore de profundidade** (priorizando a ordem lexicográfica dos vértices; 0 é a origem; você deve imprimir o identificador das arestas; em caso de desconexão, considere apenas a árvore com a raiz 0)
11. **Árvore de largura** (priorizando a ordem lexicográfica dos vértices; 0 é a origem; você deve imprimir o identificador das arestas; em caso de desconexão, considere apenas a árvore com a raiz 0)
12. **Árvore geradora mínima** (priorizando a ordem lexicográfica dos vértices ou arestas, para grafos não-orientados com pelo menos um peso diferente nas arestas; você deve imprimir o identificador das arestas)
13. **Ordem topológica** (Esta função não fica disponível em grafos não-direcionados; deve-se priorizar a ordem lexicográfica dos vértices)
14. **Valor do caminho mínimo** entre dois vértices (para grafos não-orientados com pelo menos um peso diferente nas arestas; 0 é a origem; n-1 é o destino)
15. **Valor do fluxo máximo** (Esta função não fica disponível em grafos não-direcionados; deve-se priorizar a ordem lexicográfica dos vértices; 0 é o vértice origem; n-1 é o vértice destino)
16. **Fecho transitivo** (Esta função não fica disponível em grafos não-direcionados; deve-se priorizar a ordem lexicográfica dos vértices; 0 é o vértice escolhido)

## Exemplo de Saída

Em relação ao grafo apresentado no exemplo, a saída para cada função seria:

1. **Conexo**: 1
2. **Bipartido**: 0
3. **Euleriano**: 0
4. **Possui ciclo**: 1
5. **Componentes conexas**: 0 1 2 3
6. **Componentes fortemente conexas**: -1
7. **Uma trilha Euleriana**: 0 1 2 3 1
8. **Vértices de articulação**: 1
9. **Identificador das arestas ponte**: 0
10. **Árvore de profundidade**: 0 1 3
11. **Árvore de largura**: 0 1 2
12. **Árvore geradora mínima**: -1
13. **Ordem topológica**: -1
14. **Valor do caminho mínimo**: -1
15. **Valor do fluxo máximo**: -1
16. **Fecho transitivo**: -1

