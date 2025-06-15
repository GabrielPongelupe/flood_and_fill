from typing import List, Tuple

def flood_fill(grid: List[List[int]], start_x: int, start_y: int, color: int):
    n = len(grid)
    m = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m and grid[x][y] == 0

    def dfs(x, y):
        grid[x][y] = color
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                dfs(nx, ny)

    if grid[start_x][start_y] == 0:
        dfs(start_x, start_y)

def preencher_todas_as_regioes(grid: List[List[int]]):
    n = len(grid)
    m = len(grid[0])
    cor = 2  # começa com 2 (2 = vermelho)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                flood_fill(grid, i, j, cor)
                cor += 1

def imprimir_grid(grid: List[List[int]]):
    for linha in grid:
        print(" ".join(str(cell) for cell in linha))
    print()

# --- Exemplo de uso ---
if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0]
    ]
    print("Grid inicial:")
    imprimir_grid(grid)

    preencher_todas_as_regioes(grid)

    print("Grid preenchido:")
    imprimir_grid(grid)
