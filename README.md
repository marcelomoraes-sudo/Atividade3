# Atividade 3 - UFPB
**Disciplina:** Estrutura de Dados e Complexidade de Algoritmos  
**Entrega 01:** 21/05/2026
**Entrega 02:** 28/05/2026
**Discente:** Marcelo Moraes

## Descrição
Este projeto contém a implementação dos algoritmos **Kruskal**, **Prim** e **Dijkstra** em Python, conforme as especificações da atividade. 
O objetivo é encontrar  o desempenho de ambos em vetores de diferentes tamanhos (1.000 a 100.000 elementos) contendo números inteiros positivos e negativos.

Foi feita a inclusão dos algoritmos **Merge Sort** e **Quick Sort** em Python, conforme as especificações da atividade para a entrega de 27/04.
O objetivo consiste em encontrar um subconjunto 𝑇 ⊂ 𝐸, onde 𝑇 é acíclico, toque em todos os vértices e a soma de suas arestas seja minimizada.

## Como Executar
1. **Exemplo: Para rodar os três algorítmos para o arquivo dij10.txt:**
```bash
    python3 atividade3.py dij10.txt
```

## Saídas esperadas

```bash
moraes@vm-marcelo:~/EDCA/Kruskal_Prim_Dijkstra$ python3 atividade3.py dij10.txt
Grafo carregado de 'dij10.txt' (10 vértices)

--- 1. RESULTADO: ALGORITMO DE KRUSKAL ---
Aresta (3 -- 4) com peso 151
Aresta (8 -- 9) com peso 236
Aresta (5 -- 6) com peso 241
Aresta (0 -- 1) com peso 270
Aresta (4 -- 5) com peso 272
Aresta (2 -- 3) com peso 504
Aresta (7 -- 8) com peso 1274
Aresta (5 -- 7) com peso 1560
Aresta (1 -- 4) com peso 2564
Custo total da MST: 7072

--- 2. RESULTADO: ALGORITMO DE PRIM (Início no Nó 0) ---
Aresta (0 -- 1) com peso 270
Aresta (1 -- 4) com peso 2564
Aresta (4 -- 3) com peso 151
Aresta (4 -- 5) com peso 272
Aresta (5 -- 6) com peso 241
Aresta (3 -- 2) com peso 504
Aresta (5 -- 7) com peso 1560
Aresta (7 -- 8) com peso 1274
Aresta (8 -- 9) com peso 236
Custo total da MST: 7072

--- 3. RESULTADO: ALGORITMO DE DIJKSTRA (Origem no Nó 0) ---
Caminho até o Vértice 0: [0] | Distância Total = 0
Caminho até o Vértice 1: [0, 1] | Distância Total = 270
Caminho até o Vértice 2: [0, 1, 2] | Distância Total = 3173
Caminho até o Vértice 3: [0, 1, 3] | Distância Total = 2985
Caminho até o Vértice 4: [0, 1, 4] | Distância Total = 2834
Caminho até o Vértice 5: [0, 1, 5] | Distância Total = 3025
Caminho até o Vértice 6: [0, 1, 5, 6] | Distância Total = 3266
Caminho até o Vértice 7: [0, 7] | Distância Total = 3738
Caminho até o Vértice 8: [0, 8] | Distância Total = 4947
Caminho até o Vértice 9: [0, 8, 9] | Distância Total = 5183
moraes@vm-marcelo:~/EDCA/Kruskal_Prim_Dijkstra$
```

