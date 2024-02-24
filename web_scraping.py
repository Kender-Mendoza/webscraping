import re
import requests
import json
from lxml import html
from collections import defaultdict

# # mangas = ['Mato Seihei no Slave', 'Yumemiru Danshi wa Genjitsushugisha']
# mangas = ['Yumemiru Danshi wa Genjitsushugisha']

# #* primero formatear la nueva url
# base_url = 'https://www.leercapitulo.com'

# # * Buscando si el anime existe.
# # # TODO: evitar que reviente esta vaina.
# search_path = '/search-autocomplete?term='
# manga_name_for_url = mangas[0].replace(' ', '+')
# search_url = base_url + search_path + manga_name_for_url

# result = requests.get(search_url)

# # # if result.status_code == 200 :
# #* buscando perfil del anime.
# json_serie_result = json.loads(result.text)[0]
# serie_profil_url = base_url + json_serie_result['link']
# result = requests.get(serie_profil_url)
# result_string = result.text

# ? para guardar contenido en un archivo.
# with open('pagina_web.html', 'w', encoding='utf-8') as archivo:
#     archivo.write(result_string)

# ? para leer contenido de un archivo.
# with open('pagina_web.html', 'r', encoding='utf-8') as archivo:
#     Leer el contenido del archivo
#     result_string = archivo.read()

# serie_info = defaultdict(str)
# html_tree = html.fromstring(result_string)
# serie_info['title'] = html_tree.xpath('//h1/text()')[0]
# serie_info['image_url'] = base_url + json_serie_result['thumbnail']
# serie_info['sinopsis'] = html_tree.xpath('//div[@class="manga-content"]/p[@id="example2"]/text()')[0]
# serie_info['genre'] = html_tree.xpath('//p[@class="description-update"]/a/text()')
# serie_info['state'] = html_tree.xpath('//p[@class="description-update"]/span[text()="Estado: "]/following-sibling::text()')[0]
# serie_info['last_chapter'] = html_tree.xpath('//a[@class="xanh"]/text()')[0]
# serie_info['chapter_links'] = html_tree.xpath('//a[@class="xanh"]/@href')[0]

# print('#######################')
# print('Información de la serie')
# print('#######################')
# print(' ')
# for key, value in serie_info.items():
#     print(f'{key}: {value}')


## buscando los capitulos del manga ##
# 'https://mangasnosekai.com/manga/viaje-a-otro-mundo-guiado-por-la-luna/capitulo-91/'
# chapter_manga_url = 'https://es.novelcool.com/chapter/Cap-tulo-51/2905319-10-1.html'
# chapter_manga_result = requests.get(chapter_manga_url)
# chapter_manga_content = chapter_manga_result.text

# with open('pagina_web_chapter.html', 'w', encoding='utf-8') as archivo:
#     archivo.write(chapter_manga_content)

# with open('pagina_web_chapter.html', 'r', encoding='utf-8') as archivo:
#     # Leer el contenido del archivo
#     chapter_manga_content = archivo.read()

# chapter_image_links


Madan No Ou To Vanadis
Madan+No+Ou+To+Va