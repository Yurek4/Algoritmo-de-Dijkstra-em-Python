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
