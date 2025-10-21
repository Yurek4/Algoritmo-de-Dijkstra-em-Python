# 💾 Implementação do Algoritmo de Dijkstra

Este projeto faz parte do **Trabalho 01** da disciplina **Aspectos Teóricos da Computação (ATC)** e consiste na implementação do **Algoritmo de Dijkstra** para encontrar o caminho de menor custo em um grafo **ponderado e não-direcionado**.

---

## 🎯 Objetivo

Criar um programa em Python que:

- Leia um grafo a partir de um arquivo no formato de **matriz diagonal inferior**;
- Converta essa representação em uma **Lista de Adjacência**;
- Aplique o **Algoritmo de Dijkstra** para encontrar o caminho de menor custo do vértice de origem (vértice `0`) para todos os outros vértices;
- Exiba o **caminho** e o **custo total** de forma clara, informando quando um vértice não é alcançável.

---

## ⚙️ Tecnologias Utilizadas

| Ferramenta | Descrição |
|-------------|------------|
| **Python** | Linguagem de programação principal |
| **heapq** | Biblioteca nativa para a implementação da Fila de Prioridade (Min-Heap), essencial para a eficiência do Dijkstra `O(E + V log V)` |
| **argparse** | Utilizado para processar o arquivo de entrada via linha de comando |
| **pathlib**, **typing**, **sys** | Bibliotecas nativas para manipulação de caminhos, tipagem de código e definição de valor "infinito" (`sys.maxsize`) |

---

## 📂 Estrutura do Projeto

├── dijkstra.py # Código principal com o Algoritmo de Dijkstra
├── inst01.txt # Exemplo de arquivo de entrada (instância de teste)

## 📋 Formato do Arquivo de Entrada

O arquivo de entrada (ex: `inst01.txt`) representa a **diagonal inferior da matriz de adjacência** de um grafo não-direcionado.

- **Primeira Linha:** Número total de vértices (`N`);
- **Linhas Seguintes:** Pesos das arestas;
- O valor `-1` indica **ausência de aresta**;
- O formato é `P(i, 0) P(i, 1) ... P(i, i)`.

### 🧾 Exemplo (`inst01.txt`)
8
 0
 2  0
 7 -1  0
-1 -1 -1  0
 8 -1 -1 -1  0
-1  4 -1 -1 -1  0
-1 -1 -1 -1  3  8  0
-1 -1 -1  4 -1 -1 -1  0

#📈 Exemplo de Saída

Lendo o grafo de: inst01.txt
Grafo carregado: 8 vértices.

--- Resultados do Algoritmo de Dijkstra (Origem: Vértice 0) ---
Vértice 0: Caminho: [0] | Custo Total: 0
Vértice 1: Caminho: [0 -> 1] | Custo Total: 2
Vértice 2: Caminho: [0 -> 2] | Custo Total: 7
Vértice 3: Caminho: [0 -> 1 -> 5 -> 7 -> 3] | Custo Total: 10
Vértice 4: Não há caminho (Custo: N/A)
Vértice 5: Caminho: [0 -> 1 -> 5] | Custo Total: 6
Vértice 6: Caminho: [0 -> 2 -> 6] | Custo Total: 10
Vértice 7: Caminho: [0 -> 1 -> 5 -> 7] | Custo Total: 10
