# Redes Neurais para Aprendizado de Máquina

## Introdução


## Origem das Redes Neurais

As redes neurais têm suas raízes na neurociência e na tentativa de modelar o funcionamento do cérebro humano. A ideia de criar modelos matemáticos que imitassem a estrutura e o funcionamento dos neurônios biológicos surgiu na década de 1940.

### Modelo de McCulloch-Pitts (1943)

Warren McCulloch e Walter Pitts propuseram o primeiro modelo matemático de um neurônio artificial. Este modelo, conhecido como neurônio McCulloch-Pitts, é uma simplificação do neurônio biológico. Ele consiste em:

1. **Entradas (dendritos)**: Recebem sinais de outros neurônios.
2. **Pesos (sinapses)**: Cada entrada tem um peso associado que determina a importância daquela entrada.
3. **Soma**: A soma ponderada das entradas.
4. **Função de ativação**: Uma função que decide se o neurônio "dispara" ou não, baseado na soma ponderada.
5. **Saída (axônio)**: O resultado da função de ativação, que é passado para outros neurônios.

### Perceptron (1957)

Frank Rosenblatt desenvolveu o Perceptron, um modelo de neurônio artificial que podia aprender a partir de exemplos. O Perceptron é uma extensão do modelo de McCulloch-Pitts e inclui um algoritmo de aprendizado supervisionado.

- **Entradas:** $x_1, x_2, \ldots, x_n$
- **Pesos:** $w_1, w_2, \ldots, w_n$
- **Bias:** $b$
- **Função de ativação:** $f(z)$, onde $z = \sum_{i=1}^{n} (w_i x_i + b \right)$

A função de ativação mais comum no Perceptron é a função degrau (step function), que retorna 1 se $z \geq 0$ e 0 caso contrário.

A função de ativação mais comum no Perceptron é a função degrau (step function), que retorna 1 se \( z \geq 0 \) e 0 caso contrário.

## Conceitos Fundamentais

### Arquitetura de uma Rede Neural

Uma rede neural é composta por camadas de neurônios interconectados. As principais camadas são:

1. **Camada de Entrada**: Recebe os dados de entrada.
2. **Camadas Ocultas**: Processam os dados e extraem características.
3. **Camada de Saída**: Produz a saída final da rede.

### Funções de Ativação

As funções de ativação introduzem não-linearidade no modelo, permitindo que a rede aprenda padrões complexos. Algumas funções de ativação comuns são:

- **Sigmoid:** $\sigma(x) = \frac{1}{1 + e^{-x}}$
- **Tanh:** $\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$
- **ReLU (Rectified Linear Unit):** $\text{ReLU}(x) = \max(0, x)$

### Aprendizado Supervisionado

No aprendizado supervisionado, a rede neural é treinada com um conjunto de dados rotulados. O objetivo é ajustar os pesos da rede para minimizar a diferença entre as saídas previstas e as saídas reais.

## Exemplos Práticos

### Classificação de Imagens

Um exemplo clássico de aplicação de redes neurais é a classificação de imagens. Suponha que queremos classificar imagens de gatos e cachorros.

1. **Preparação dos Dados**: Coletamos um conjunto de imagens de gatos e cachorros e rotulamos cada imagem.
2. **Pré-processamento**: Redimensionamos as imagens para um tamanho padrão e normalizamos os valores dos pixels.
3. **Arquitetura da Rede**: Criamos uma rede neural com uma camada de entrada (para os pixels da imagem), uma ou mais camadas ocultas e uma camada de saída (com duas unidades, uma para gato e outra para cachorro).
4. **Treinamento**: Utilizamos um algoritmo de otimização, como o Gradiente Descendente, para ajustar os pesos da rede com base nos erros de previsão.
5. **Avaliação**: Testamos a rede com um conjunto de imagens não vistas durante o treinamento para avaliar sua precisão.

### Reconhecimento de Voz

Outro exemplo é o reconhecimento de voz, onde a rede neural é usada para converter áudio em texto.

1. **Preparação dos Dados**: Coletamos um conjunto de áudios e transcrições correspondentes.
2. **Pré-processamento**: Convertemos o áudio em características, como espectrogramas.
3. **Arquitetura da Rede**: Criamos uma rede neural com camadas de entrada, ocultas e de saída.
4. **Treinamento**: Utilizamos um algoritmo de otimização para ajustar os pesos da rede.
5. **Avaliação**: Testamos a rede com áudios não vistos durante o treinamento para avaliar sua precisão.
