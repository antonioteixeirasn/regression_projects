# Regressão Linear Múltipla

## Introdução
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

Abaixo pode-se observar as 5 primeiras linhas desse dataset:

|R&D Spend| Administration| Marketing Spend| State| Profit|
|---| ---| ---| ---| ---| 
|165349.20|136897.80|471784.10|New York   |192261.83|
|162597.70|151377.59|443898.53|California |191792.06|
|153441.51|101145.55|407934.54|Florida    |191050.39|
|144372.41|118671.85|383199.62|New York   |182901.99|
|142107.34|91391.77 |366168.42|Florida    |166187.94|

## One Hot Encoding

Nesse dataset, é preciso aplicar One Hot Encoding à coluna State, isto é, realizar um pré-processamento dos dados. Nesse caso, essa  
coluna possui três valores: New York, Califórnia e Flórida; assim, corresponde a uma variável categórica. Dessa forma, teremos 3   
colunas composta por 1 e 0, onde 1 corresponde a um valor afirmativo.

## Conclusão
Com esse código é possível aplicar conhecimentos de Machine Learning aplicando um modelo de Regressão Linear Múltipla para prever  
os lucros de startups com base nos seus gastos com P&D, administrativos, e com marketing, além do estado na qual está cituada.
