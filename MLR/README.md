# Regressão Linear Múltipla

## Introduction
Nesse projeto, você será capaz de aplicar um modelo de regressão linear múltipla em um dataset contendo informações de 50 startups!

## Objetivos
- Carregar o dataset.
- Tratar dados categóricos.
- Dividir o dataset em treino e teste.
- Treinar o modelo de regressão linear múltipla.
- Prever o lucro das empresas contidas nos dados de teste.
- Avaliar performance do modelo.

## Sobre o dataset
As informações contidas nesse dataset foram coletadas de 50 startups de Nova York, Califórnia e Flórida. As variáveis usadas nesse   
dataset são: Lucros (Profit), gastos com P&D (R&D spending), gastos administrativos (administration spending), gastos com marketing  
(marketing spending) e o estado na qual a empresa está localizada (state).

## One Hot Encoding

Nesse dataset, é preciso aplicar One Hot Encoding à coluna State, isto é, realizar um pré-processamento dos dados. Nesse caso, essa  
coluna possui três valores: New York, Califórnia e Flórida; assim, corresponde a uma variável categórica. Dessa forma, teremos 3   
colunas composta por 1 e 0, onde 1 corresponde a um valor afirmativo.

## Conclusão
Com esse código é possível aplicar conhecimentos de Machine Learning aplicando um modelo de Regressão Linear Múltipla para prever  
os lucros de startups com base nos seus gastos com P&D, administrativos, e com marketing, além do estado na qual está cituada.
