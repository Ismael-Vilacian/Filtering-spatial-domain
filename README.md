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

O código solicitará qual filtro deve ser aplicado: 1 para máscara de nitidez, 2 para suavização e 3 para realce de bordas. Em seguida, ele pedirá o nome da imagem a ser processada (a imagem deve estar na pasta "images"). Para o filtro de suavização, haverá três opções: 1 para média, 2 para mediana e 3 para gaussiano. Após a aplicação dos filtros, as imagens serão salvas na pasta "processed-image".

Aplicando filtro de nitidez, observamos um realce das cores, resultando em uma imagem com aparência mais viva e destacada.

<img loading="lazy" src="https://imgur.com/1Aj0Iq1.png"/>

Ao aplicar o filtro de suavização, notamos que a imagem adquiriu um certo desfoque. Para perceber as diferenças entre os filtros de suavização média, mediana e gaussiana, é necessário dar um zoom nas bordas, onde as maiores diferenças são mais evidentes. 

>Usando a suavização por média, observamos que as bordas da imagem ficaram mais suavizadas, tornando-se menos visíveis.

<img loading="lazy" src="https://imgur.com/r24PxVf.png"/>

>Usando a suavização por mediana, notamos que a imagem adquire um desfoque, porém as bordas mantêm o seu destaque.

<img loading="lazy" src="https://imgur.com/31GZKR0.png"/>

>Usando a suavização gaussiana, observamos que as bordas da imagem ficaram mais suaves. No entanto, diferente do filtro de média, as bordas mantiveram uma melhor visibilidade.

<img loading="lazy" src="https://imgur.com/W7HSYjH.png"/>

Ao aplicar o filtro laplaciano, percebemos que apenas as bordas se destacam, fazendo com que o restante da imagem fique escuro.

<img loading="lazy" src="https://imgur.com/ekve0fT.png"/>
