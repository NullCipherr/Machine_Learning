# Redes de Crença
#
# As redes de crenças, também chamadas de Redes Bayesianas, é uma estrutura probabilistica que representa um conjunto de variáveis e suas dependências condicionais por meio de um Grafo Aciclico Dirigido, onde os nós são variáveis randômicas.
# As redes de crenças, são uma implementação direta do Teorema de Bayes, que permite a modelagem de incertezas e a realização de inferências em aprendizado de máquina e inteligência artificial.

# Funcionamento
#
# Uma rede Bayesiana é um modelo gráfico que representa um conjunto de variáveis aleatórias e suas dependências condicionais usando um grafo direcionado acíclico (DAG). Cada nó no grafo representa uma variável, e cada aresta indica uma relação de dependência entre duas variáveis.
# 
# Elementos
#
# - Nós
#   - Representam variáveis aleatórias que podem ser observáveis(dados) ou não observáveis(ocultas).
#   - Cada nó possui uma distribuição de probabilidade que descreve a incerteza sobre a variável.
# - Arestas
#   - Indicadores de dependência direta.
#   - A---B : A é Pai de B, e B é condicionalmente dependente de A.
# - Distribuições Condicionais.
#   - Cada nó possui uma tabela de distribução probabilidade condicional P(X|Pais(X)).
