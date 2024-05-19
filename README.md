# Processamento de imagens: Máscara de Nitidez, Filtros de Suavização e Filtro Laplaciano
<img loading="lazy" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" width="40" height="40"/> <img loading="lazy" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/opencv/opencv-original-wordmark.svg" width="40" height="40"/>
          
Neste estudo, exploraremos o processamento de imagens aplicando filtros de nitidez, suavização e laplaciano. Esses filtros desempenham papéis cruciais na melhoria da qualidade das imagens.

## Funcionalidades

- Implementação do filtro de máscara de nitidez
- Implementação de filtros de Suavização
- Implementação do realce de bordas com o filtro laplaciano

Os filtros de Máscara de Nitidez, Filtros de Suavização e Realce de Bordas com o Filtro Laplaciano desempenham papéis importantes no processamento de imagens. A Máscara de Nitidez é utilizada para acentuar detalhes, aumentando a clareza da imagem através da realce de suas bordas. Os Filtros de Suavização, por outro lado, reduzem o ruído e suavizam a imagem ao atenuar variações bruscas de intensidade, proporcionando um efeito de desfoque que torna a imagem mais uniforme. Já o Filtro Laplaciano é um filtro de realce de bordas que destaca mudanças rápidas de intensidade, facilitando a detecção de contornos e detalhes estruturais na imagem. Esses filtros são essenciais para aprimorar a qualidade visual das imagens, seja na remoção de ruídos, na melhoria da nitidez ou na detecção de bordas e padrões.

>O propósito deste processo foi aplicar conceitos dos estudos de processamento 
>de imagem por meio da utilização dos filtros de Máscara de Nitidez, 
>Filtros de Suavização e Realce de Bordas com o Filtro Laplaciano.

## Tecnologias

Para realização do projeto foi utilizado:

- [OpenCV](https://opencv.org) - OpenCV é uma biblioteca de visão computacional.
- [Python](https://www.python.org) - Python é uma linguagem de programação que permite trabalhar rapidamente e integrar sistemas de forma mais eficaz.

## Instalação

Para executar, simplesmente instale o [Python 3](https://www.python.org) em seu computador e, em seguida, no terminal, instale o pacote "opencv-contrib-python".

```sh
pip3 install opencv-contrib-python
```
Após isso, basta executar o arquivo princial main.py.

## Resultados

O código vai solicitar qual filtro deve ser aplicaso, sendo 1 para máscara de nitidez, 2 para suavização e 3 para realce de borda, em seguida ele vai pedir o nome da imagem a qual vai ter o filtro aplicado (a imagem deve estar na pasta images). Para o filtro de suavização em específico, o código dará três opções sendo 1 para usar média, 2 para mediana e 3 para gaussiano. após aplicado os filtros, as imagens vai ser salva nos pasta 'processed-image'.
