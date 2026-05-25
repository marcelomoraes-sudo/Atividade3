import heapq
import sys  
import os

# ==========================================
# ESTRUTURA AUXILIAR PARA O KRUSKAL
# ==========================================
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False


# ==========================================
# FUNÇÃO DE LEITURA DO ARQUIVO TXT
# ==========================================
def ler_grafo_do_arquivo(nome_arquivo):
    arestas = []
    with open(nome_arquivo, 'r') as f:
        linhas = [linha.strip() for linha in f.readlines() if linha.strip()]
        
    num_vertices = int(linhas[0])
    
    for i in range(1, len(linhas)):
        u = i - 1  
        pesos = list(map(int, linhas[i].split()))
        
        for idx, peso in enumerate(pesos):
            v = u + 1 + idx
            arestas.append((peso, u, v))
            
    return num_vertices, arestas


# ==========================================
# ALGORITMO DE KRUSKAL
# ==========================================
def kruskal(num_vertices, arestas):
    arestas_ordenadas = sorted(arestas, key=lambda item: item[0])
    uf = UnionFind(num_vertices)
    mst = []
    custo_total = 0

    for peso, u, v in arestas_ordenadas:
        if uf.union(u, v):
            mst.append((u, v, peso))
            custo_total += peso
            if len(mst) == num_vertices - 1:
                break
    return mst, custo_total


# ==========================================
# ALGORITMO DE PRIM
# ==========================================
def prim(num_vertices, arestas, origem=0):
    grafo = [[] for _ in range(num_vertices)]
    for peso, u, v in arestas:
        grafo[u].append((peso, v))
        grafo[v].append((peso, u))

    visitados = [False] * num_vertices
    mst = []
    custo_total = 0
    min_heap = []

    def adicionar_arestas(u):
        visitados[u] = True
        for peso, v in grafo[u]:
            if not visitados[v]:
                heapq.heappush(min_heap, (peso, v, u))

    adicionar_arestas(origem)

    while min_heap and len(mst) < num_vertices - 1:
        peso, v, u = heapq.heappop(min_heap)
        if visitados[v]:
            continue
        mst.append((u, v, peso))
        custo_total += peso
        adicionar_arestas(v)

    return mst, custo_total


# ==========================================
# ALGORITMO DE DIJKSTRA
# ==========================================
def dijkstra(num_vertices, arestas, origem=0):
    grafo = [[] for _ in range(num_vertices)]
    for peso, u, v in arestas:
        grafo[u].append((peso, v))
        grafo[v].append((peso, u))

    distancias = {i: float('inf') for i in range(num_vertices)}
    distancias[origem] = 0
    predecessores = {i: None for i in range(num_vertices)}
    min_heap = [(0, origem)]

    while min_heap:
        dist_atual, u = heapq.heappop(min_heap)

        if dist_atual > distancias[u]:
            continue

        for peso, v in grafo[u]:
            distancia_alternativa = dist_atual + peso
            if distancia_alternativa < distancias[v]:
                distancias[v] = distancia_alternativa
                predecessores[v] = u
                heapq.heappush(min_heap, (distancia_alternativa, v))

    return distancias, predecessores

def mapear_caminho(predecessores, destino):
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = predecessores[atual]
    return caminho[::-1]


# ==========================================
# EXECUÇÃO PRINCIPAL
# ==========================================
if __name__ == "__main__":
    # Verifica se o usuário passou o argumento do nome do arquivo
    if len(sys.argv) < 2:
        print("\n\nErro: Você deve informar o nome do arquivo de texto.")
        print("Exemplo: python atividade3.py dij10.txt\n\n")
        sys.exit(1)
        
    arquivo = sys.argv[1]
    
    # Valida se o arquivo realmente existe antes de abrir
    if not os.path.exists(arquivo):
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        sys.exit(1)
    
    # Processa os dados
    num_vertices, arestas_grafo = ler_grafo_do_arquivo(arquivo)
    
    print(f"Grafo carregado de '{arquivo}' ({num_vertices} vértices)\n")
    
    print("--- 1. RESULTADO: ALGORITMO DE KRUSKAL ---")
    mst_kruskal, custo_kruskal = kruskal(num_vertices, arestas_grafo)
    for u, v, peso in mst_kruskal:
        print(f"Aresta ({u} -- {v}) com peso {peso}")
    print(f"Custo total da MST: {custo_kruskal}\n")

    print("--- 2. RESULTADO: ALGORITMO DE PRIM (Início no Nó 0) ---")
    mst_prim, custo_prim = prim(num_vertices, arestas_grafo, origem=0)
    for u, v, peso in mst_prim:
        print(f"Aresta ({u} -- {v}) com peso {peso}")
    print(f"Custo total da MST: {custo_prim}\n")

    print("--- 3. RESULTADO: ALGORITMO DE DIJKSTRA (Origem no Nó 0) ---")
    distancias, predecessores = dijkstra(num_vertices, arestas_grafo, origem=0)
    for v in range(num_vertices):
        caminho = mapear_caminho(predecessores, v)
        print(f"Caminho até o Vértice {v}: {caminho} | Distância Total = {distancias[v]}")
