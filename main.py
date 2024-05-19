from unsharp_mask_filter import Sharpness
from smoothing_filters import Smoothing
from laplacian_filter import Laplacian
import os

def validate_image(value):
    if os.path.isfile(f'images/{value}') is False:
        print("A imagem não foi encontrada")
        return False

choice = int(input('''
---------------------------------------
|  1 - Filtro de Máscara de Nitidez   |
|  2 - Filtros de Suavização          |
|  3 - Realce de Bordas (Laplaciano)  |
---------------------------------------
\nEscolha o filtro: '''))

image = input('Digite o nome da imagem com a extensão da imagem (Ex: img.jpeg, img.png): ')

if choice == 1:
    
    if validate_image(image) is False:
        exit()

    Sharpness(105, image).sharpness_filter()

elif choice == 2:
    if validate_image(image) is False:
        exit()
    
    type_filter = int(input('''
--------------------------
| 1 - Média              |   
| 2 - Mediana            |
| 3 - Gaussiano          |
--------------------------    
\nEscolha o tipo do filtro:                        
'''))
    
    Smoothing(3, image, type_filter).smoothing_filter()

elif choice == 3:
    if validate_image(image) is False:
        exit()
    
    Laplacian(image).laplacian_filter()

else:
    print('Opção inválida')