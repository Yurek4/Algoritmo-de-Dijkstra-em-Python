# Algoritmo-de-Dijkstra-em-Python

Passo a Passo: Desenvolvimento do Projeto Dijkstra em Python
🎯 1. Objetivo do Trabalho (Resumo)O objetivo principal é implementar o Algoritmo de Dijkstra em Python para encontrar os caminhos de menor custo (custo mínimo) do vértice de origem (vértice 0) para todos os outros vértices em um grafo não direcionado e ponderado, cuja entrada é fornecida em um formato especial de matriz diagonal inferior em um arquivo.
🧠 2. Conceito do Algoritmo de DijkstraO Algoritmo de Dijkstra é um algoritmo guloso (greedy) que resolve o problema do caminho mais curto de fonte única para um grafo com pesos de arestas não negativos.
Raciocínio Passo a Passo:
Inicialização:
Define-se a distância do vértice de origem (nosso caso, o 0) para ele mesmo como 0.
A distância para todos os outros vértices é definida como infinito ($\infty$).
Um conjunto de vértices "visitados" (ou finalizados) é mantido, inicialmente vazio.
Usa-se uma Fila de Prioridade (Min-Heap) para armazenar os vértices a serem explorados, priorizando aqueles com a menor distância conhecida até o momento a partir da origem.
Processo de Seleção e Relaxamento:
Enquanto a Fila de Prioridade não estiver vazia, o algoritmo retira o vértice u com a menor distância conhecida atual (o topo da fila).
Se u já foi finalizado (visitado), o algoritmo o ignora e continua.O vértice u é marcado como visitado (ou finalizado).
Relaxamento: Para cada vizinho v de u:O algoritmo verifica se o caminho de $0 \to u \to v$ é mais curto do que o caminho mais curto conhecido para v até agora.
Matematicamente: Se $dist(u) + peso(u, v) < dist(v)$, então atualizamos $dist(v) = dist(u) + peso(u, v)$.
Essa atualização (relaxamento) significa que encontramos um caminho mais curto para v passando por u. O novo par (nova_distância, v) é adicionado à Fila de Prioridade.Resultado:Ao final, a distância registrada para cada vértice é o custo do caminho mais curto de 0 até ele.
Resultado:
Ao final, a distância registrada para cada vértice é o custo do caminho mais curto de 0 até ele.

Biblioteca,Tipo,Função
heapq,Padrão (Nat. C),"Implementa o algoritmo de heap (fila de prioridade). Essencial para o Dijkstra, pois permite extrair o menor custo em tempo O(logN)."
argparse,Padrão (Nat. Python),Fornece um mecanismo para analisar argumentos de linha de comando. Usada para ler o nome do arquivo de entrada.
pathlib,Padrão (Nat. Python),Oferece uma interface orientada a objetos para manipulação de caminhos de sistema de arquivos. Usada para garantir a compatibilidade e robustez ao lidar com o arquivo de entrada.
typing,Padrão (Nat. Python),"Fornece dicas de tipo (type hints) para melhorar a legibilidade, a capacidade de manutenção e auxiliar ferramentas de análise estática de código (como o MyPy)."
sys,Padrão (Nat. C),"Usada para acessar parâmetros e funções específicas do interpretador Python, como sys.maxsize, que é usado como um valor prático de ""infinito"" no algoritmo."
