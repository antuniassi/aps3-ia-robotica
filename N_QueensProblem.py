from aigyminsper.search.search_algorithms import BuscaProfundidade
from aigyminsper.search.graph import State

import numpy as np
import time

class N_QueensProblem(State):

    def __init__(self, size, board=None, column=0):
        super().__init__(None)
        self.size = size
        self.column = column

        if board is None:
            self.board = np.zeros((size, size), dtype=int)
        else:
            self.board = board

    def env(self):
        return self.board

    def successors(self):
        sucessores = []

        if self.column >= self.size:
            return sucessores

        for row in range(self.size):

            if self.posicao_valida(row, self.column):
                novo_tabuleiro = self.board.copy()
                novo_tabuleiro[row][self.column] = 1

                novo_estado = N_QueensProblem(
                    self.size,
                    novo_tabuleiro,
                    self.column + 1
                )
                sucessores.append(novo_estado)
        return sucessores


    def posicao_valida(self, row, col):
        for coluna_anterior in range(col):
            for linha_anterior in range(self.size):
                if self.board[linha_anterior][coluna_anterior] == 1:
                    if linha_anterior == row:
                        return False

                    if abs(linha_anterior - row) == abs(coluna_anterior - col):
                        return False
        return True

    def is_goal(self):
        return self.column == self.size


    def description(self):
        return "N Queens Problem"

    def cost(self):
        return 1

def main():

    for N in range(4, 9):

        print("N =", N)
        state = N_QueensProblem(N)
        algorithm = BuscaProfundidade()
        start = time.time()
        result = algorithm.search(
            state,
            m=N,
        )
        end = time.time()

        if result is not None:
            print("Solucao encontrada:")
            print(result.state.env())
            print("Tempo:", end - start, "segundos")
        else:
            print("Nao encontrou solucao")

if __name__ == '__main__':
    main()