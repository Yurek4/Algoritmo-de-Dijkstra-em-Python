import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import heapq
import sys

def ler_grafo_do_arquivo(caminho_arquivo: Path) -> Tuple[int, Dict[int, List[Tuple[int, int]]]]:
    """
    Lê o grafo a partir de um arquivo no formato diagonal inferior e o
    converte para uma Lista de Adjacência.
    """
    try:
        with open(caminho_arquivo, 'r') as f:
            linhas = f.readlines()
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {caminho_arquivo}")
        sys.exit(1)
    
    # Linha 1: Número de vértices (N)
    try:
        num_vertices = int(linhas[0].strip())
    except ValueError:
        print("Erro: A primeira linha deve ser um inteiro (número de vértices).")
        sys.exit(1)

    # Inicializa a lista de adjacência (vértice -> [(vizinho, peso), ...])
    # Dicionário é mais flexível, mas List[List] também seria válido.
    lista_adj: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(num_vertices)}
    
    # Processa as linhas da diagonal inferior (a partir da segunda linha)
    linha_atual = 1
    
    # A iteração vai de 0 a N-1, onde 'i' representa a linha da matriz
    for i in range(num_vertices):
        # Linhas vazias são ignoradas no loop
        if linha_atual >= len(linhas):
             break 
             
        # Pega os pesos da linha 'i' (apenas a parte inferior)
        pesos_str = linhas[linha_atual].strip().split()
        
        # Converte os pesos para inteiros
        try:
            pesos = [int(p) for p in pesos_str]
        except ValueError:
            print(f"Erro: Peso inválido na linha {linha_atual+1} do arquivo.")
            sys.exit(1)

        # O número de elementos deve ser igual a 'i + 1'
        if len(pesos) != i + 1:
            print(f"Erro: Número incorreto de pesos na linha {linha_atual+1}. Esperado: {i+1}, Obtido: {len(pesos)}.")
            sys.exit(1)

        # 'j' representa a coluna da matriz, vai de 0 até 'i'
        for j in range(i + 1):
            peso = pesos[j]
            
            # Se o peso não for -1 (aresta inexistente) e não for 0 (laço desconsiderado)
            if peso > 0:
                # O grafo é NÃO DIRECIONADO, então adicionamos a aresta (i, j) e (j, i)
                
                # Aresta (i -> j)
                lista_adj[i].append((j, peso))
                
                # Aresta (j -> i)
                lista_adj[j].append((i, peso))
        
        linha_atual += 1

    return num_vertices, lista_adj

# ----------------------------------------------------------------------
# 2. Implementação do Algoritmo de Dijkstra
# ----------------------------------------------------------------------

def dijkstra(num_vertices: int, lista_adj: Dict[int, List[Tuple[int, int]]], origem: int = 0) -> Tuple[Dict[int, int], Dict[int, Optional[int]]]:
    """
    Aplica o Algoritmo de Dijkstra para encontrar o menor caminho do vértice 'origem' 
    para todos os outros vértices.
    """
    
    # Usamos sys.maxsize para representar "infinito", pois é o maior inteiro
    # que o Python pode representar de forma nativa e eficiente.
    INFINITO = sys.maxsize
    
    # 1. Inicialização: 
    # distancias: Mapeia vértice -> custo do menor caminho conhecido
    distancias: Dict[int, int] = {v: INFINITO for v in range(num_vertices)}
    distancias[origem] = 0
    
    # predecessores: Mapeia vértice -> vértice anterior no caminho mais curto
    # Usado para reconstruir o caminho
    predecessores: Dict[int, Optional[int]] = {v: None for v in range(num_vertices)}
    
    # Fila de Prioridade (Min-Heap): Armazena (custo_atual, vertice)
    # heap: [(distancia_a, vertice_a), (distancia_b, vertice_b), ...]
    fila_prioridade: List[Tuple[int, int]] = [(0, origem)]
    
    # Conjunto de vértices que já tiveram seu caminho mais curto finalizado
    # Opcional, mas pode otimizar
    # visitados: Set[int] = set()

    # 2. Processo de Seleção e Relaxamento
    while fila_prioridade:
        # Extrai o elemento com menor custo conhecido (Min-Heap)
        dist_u, u = heapq.heappop(fila_prioridade)
        
        # Se a distância extraída for maior que a distância já registrada, 
        # é um "caminho obsoleto" e pode ser ignorado.
        if dist_u > distancias[u]:
            continue
            
        # Percorre todos os vizinhos (v) do vértice u
        for v, peso_uv in lista_adj.get(u, []):
            
            # Cálculo da nova distância: Custo de 0 -> u + Custo de u -> v
            nova_distancia = dist_u + peso_uv
            
            # 3. Relaxamento: Se encontrarmos um caminho mais curto para 'v'
            if nova_distancia < distancias[v]:
                
                # Atualiza a distância
                distancias[v] = nova_distancia
                
                # Atualiza o predecessor (o caminho mais curto para 'v' agora passa por 'u')
                predecessores[v] = u
                
                # Adiciona/Atualiza 'v' na Fila de Prioridade
                heapq.heappush(fila_prioridade, (nova_distancia, v))

    return distancias, predecessores

# ----------------------------------------------------------------------
# 3. Funções de Exibição do Resultado
# ----------------------------------------------------------------------

def construir_caminho(origem: int, destino: int, predecessores: Dict[int, Optional[int]]) -> Optional[List[int]]:
    """
    Reconstrói o caminho do 'origem' ao 'destino' usando o dicionário de predecessores.
    Retorna None se não houver caminho.
    """
    # Se o predecessor do destino for None e o destino não for a origem, não há caminho
    if predecessores.get(destino) is None and destino != origem:
        return None
    
    caminho = []
    # Começa pelo destino e volta até a origem
    atual = destino
    while atual is not None:
        caminho.append(atual)
        # Tenta pegar o predecessor, pode ser None se for a origem
        atual = predecessores.get(atual) 
        
        # Prevenção simples contra laços (embora Dijkstra não crie laços)
        if len(caminho) > len(predecessores):
            return None # Laço detectado (impossível em Dijkstra)
            
    # O caminho é construído do destino para a origem, então invertemos
    return caminho[::-1]

def exibir_resultados(num_vertices: int, distancias: Dict[int, int], predecessores: Dict[int, Optional[int]], origem: int = 0):
    """
    Exibe os resultados finais do menor caminho e custo para cada vértice.
    """
    print("\n--- Resultados do Algoritmo de Dijkstra (Origem: Vértice 0) ---")
    INFINITO = sys.maxsize
    
    # Itera sobre todos os vértices, exceto o de origem
    for destino in range(num_vertices):
        custo_total = distancias[destino]
        
        caminho = construir_caminho(origem, destino, predecessores)
        
        if custo_total == INFINITO or caminho is None:
            # Não há caminho
            print(f"Vértice {destino}: Não há caminho (Custo: N/A)")
        else:
            # Caminho encontrado
            caminho_str = " -> ".join(map(str, caminho))
            print(f"Vértice {destino}: Caminho: [{caminho_str}] | Custo Total: {custo_total}")


# ----------------------------------------------------------------------
# 4. Função Principal (Main)
# ----------------------------------------------------------------------

def main():
    """
    Função principal que coordena a leitura do arquivo, execução do Dijkstra e exibição.
    """
    # 4.1 Configuração do argparse para ler o arquivo da linha de comando
    parser = argparse.ArgumentParser(description="Implementação do Algoritmo de Dijkstra em Python.")
    parser.add_argument("arquivo_entrada", type=str, help="O caminho para o arquivo de entrada do grafo (e.g., inst01.txt).")
    
    args = parser.parse_args()
    caminho_arquivo = Path(args.arquivo_entrada)
    
    # 4.2 Leitura e Conversão
    print(f"Lendo o grafo de: {caminho_arquivo}")
    num_vertices, lista_adj = ler_grafo_do_arquivo(caminho_arquivo)
    print(f"Grafo carregado: {num_vertices} vértices.")

    # 4.3 Execução do Dijkstra
    # A origem é fixa: 0
    origem = 0
    distancias, predecessores = dijkstra(num_vertices, lista_adj, origem)
    
    # 4.4 Exibição dos Resultados
    exibir_resultados(num_vertices, distancias, predecessores, origem)

# Execução do programa
if __name__ == "__main__":
    main()