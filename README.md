# FloodFill - Colorindo Regiões de um Terreno com Obstáculos

## 👥 Integrantes

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/FernandoIbrahim">
        <img src="https://avatars.githubusercontent.com/u/80763509?v=4" width="100px;" height="100px;" style="border-radius:50%;" alt="Gabriel Pongelupe"/><br />
        <sub><b>Fernando Ibrahim</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/GabrielPongelupe">
        <img src="https://avatars.githubusercontent.com/u/130582324?v=4" width="100px;" height="100px;" style="border-radius:50%;" alt="Gabriel Pongelupe"/><br />
        <sub><b>Gabriel Pongelupe</b></sub>
      </a>
    </td>
   
</table>

## Descrição do Projeto


Este projeto implementa o algoritmo **Flood Fill** para identificar e preencher automaticamente todas as regiões conectadas em um grid bidimensional. O sistema foi desenvolvido para mapear terrenos com obstáculos, simulando um ambiente de navegação para robôs autônomos que precisam identificar e classificar diferentes áreas de um terreno previamente desconhecido.

## Problema Resolvido

O projeto soluciona o problema de **identificação e preenchimento de regiões conectadas** em um grid 2D utilizando o Algoritmo Flood Fill. O terreno é representado como uma matriz bidimensional onde:

- **0**: Terreno navegável (células livres - representadas em branco)
- **1**: Obstáculos (células bloqueadas - representadas em preto)
- **2, 3, 4, ...**: Regiões já preenchidas com cores diferentes (vermelho, laranja, amarelo, etc.)

O algoritmo identifica automaticamente todas as áreas livres conectadas e as preenche com cores distintas, facilitando a visualização e o planejamento de operações em terrenos complexos.

## Funcionamento do Algoritmo Flood Fill

O algoritmo Flood Fill implementado funciona da seguinte forma:

### Processo Principal:
1. **Varredura do Grid**: O algoritmo percorre sistematicamente todo o grid em busca de células navegáveis (valor 0)
2. **Identificação de Regiões**: Quando encontra uma célula navegável, inicia o processo de preenchimento
3. **Preenchimento Recursivo**: Utiliza busca em profundidade (DFS) para preencher todas as células conectadas
4. **Incremento de Cor**: A cada nova região encontrada, incrementa a cor utilizada (2, 3, 4, ...)

### Algoritmo de Preenchimento (DFS):
1. **Célula Inicial**: Marca a célula atual com a cor especificada
2. **Exploração de Vizinhos**: Verifica as 4 células adjacentes (cima, baixo, esquerda, direita)
3. **Validação**: Para cada vizinho, verifica se:
   - Está dentro dos limites do grid
   - É uma célula navegável (valor 0)
4. **Recursão**: Se válido, aplica recursivamente o algoritmo na célula vizinha
5. **Controle de Fronteiras**: Respeita obstáculos (valor 1) e limites do grid

### Características Importantes:
- **Conectividade Ortogonal**: Considera apenas adjacências horizontais e verticais (não diagonais)
- **Preservação de Obstáculos**: Mantém intactos os obstáculos e regiões já coloridas
- **Preenchimento Automático**: Continua o processo até que todas as células navegáveis sejam preenchidas
- **Cores Sequenciais**: Utiliza uma sequência numérica crescente para diferenciar as regiões

## Configuração e Execução

### Pré-requisitos
- Python 3.6 ou superior
- Nenhuma biblioteca externa necessária (utiliza apenas bibliotecas padrão do Python)

### Estrutura do Projeto
```
projeto-floodfill/
├── flood_and_fill.py
└── README.md
```

### Como Executar

1. **Clone ou baixe o repositório**
2. **Navegue até o diretório do projeto**
3. **Execute o programa**:
   ```bash
   python flood_and_fill.py
   ```

### Modificando o Grid de Entrada

Para testar com diferentes configurações, modifique a variável `grid` no arquivo `flood_and_fill.py`:

```python
grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0]
]
```

## Exemplos de Funcionamento

### Exemplo 1

**Entrada:**
```
Grid inicial:
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
```

**Saída:**
```
Grid preenchido:
2 2 1 3 3
2 1 1 3 3
2 2 1 1 1
1 1 4 4 4
```

**Explicação:**
- **Região 2 (Vermelho)**: Área conectada no canto superior esquerdo (3 células na coluna 0 e 2 células na linha 0)
- **Região 3 (Laranja)**: Área conectada no canto superior direito (4 células)
- **Região 4 (Amarelo)**: Área conectada no canto inferior direito (3 células)

### Exemplo 2

**Entrada:**
```
Grid inicial:
0 1 0 0 1
0 1 0 0 1
0 1 1 1 1
0 0 0 1 0
```

**Saída:**
```
Grid preenchido:
2 1 3 3 1
2 1 3 3 1
2 1 1 1 1
2 2 2 1 4
```

**Explicação:**
- **Região 2 (Vermelho)**: Coluna da esquerda + células da linha inferior
- **Região 3 (Laranja)**: Área central-direita (4 células)
- **Região 4 (Amarelo)**: Célula isolada no canto inferior direito

## Representação Visual das Cores

| Valor | Cor | Significado |
|-------|-----|-------------|
| 0 | Branco | Terreno navegável (não preenchido) |
| 1 | Preto | Obstáculo |
| 2 | Vermelho | Primeira região preenchida |
| 3 | Laranja | Segunda região preenchida |
| 4 | Amarelo | Terceira região preenchida |
| 5+ | Verde, Azul, etc. | Regiões adicionais |

## Estrutura do Código

### Funções Principais:

1. **`flood_fill(grid, start_x, start_y, color)`**
   - Implementa o algoritmo Flood Fill para uma região específica
   - Utiliza DFS recursivo para preencher células conectadas

2. **`preencher_todas_as_regioes(grid)`**
   - Varre todo o grid em busca de regiões não preenchidas
   - Aplica o Flood Fill automaticamente em cada região encontrada

3. **`imprimir_grid(grid)`**
   - Exibe o grid formatado no terminal
   - Facilita a visualização do estado atual da matriz

### Características Técnicas:
- **Complexidade Temporal**: O(n×m) onde n e m são as dimensões do grid
- **Complexidade Espacial**: O(n×m) no pior caso devido à recursão
- **Tipo de Busca**: Busca em Profundidade (DFS)
- **Conectividade**: 4-conectada (ortogonal)

