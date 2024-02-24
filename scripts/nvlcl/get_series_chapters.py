import requests
from lxml import html

class getSeriesChapters:
  def __init__(self, serie_data):
    self.serie_data = serie_data

  def call(self):
    return self._add_chapters_to_serie()

  # def _validate_if_serie_exist:
    # validate by url

  def _get_html_of_page(self):
    # serie_profil_url = self.serie_data['profil_url']
    # serie_profil_page_content = requests.get(serie_profil_url)

    #! Only for testing
    with open((self.serie_data['name'] + '.html'), 'r', encoding='utf-8') as archivo:
      # Leer el contenido del archivo
      chapter_manga_content = archivo.read()

    return chapter_manga_content # serie_profil_page_content.text

  def _format_data(self):
    serie_profil_content = self._get_html_of_page()
    html_tree = html.fromstring(serie_profil_content)
    serie_profil_chapters_html = html_tree.xpath('//div[@class="chp-item"]')

    return list(map(lambda chapter: (
      {
        'number': chapter.xpath('.//a/@title')[0],
        'chapter_url': self._format_chapter_url(chapter.xpath('.//a/@href')[0]),
        'date_modified': chapter.xpath('.//span[@class="chapter-item-time"]/text()')[0]
      }
    ), serie_profil_chapters_html))

  def _format_chapter_url(self, chapter_url):
    return chapter_url[:-1] + '-10-1.html'

  def _add_chapters_to_serie(self):
    serie_data = self.serie_data
    serie_data['chapters'] = self._format_data()

    return serie_data


#! only for testing
data = {
  'name': 'Madan No Ou To Michelia',
  'type': 'Manga',
  'scoring': '0.0',
  'views': '331',
  'date_modified': 'Jun 21, 2020',
  'profil_url': 'https://es.novelcool.com/novel/Madan-No-Ou-To-Michelia.html'
}

'https://es.novelcool.com/novel/Madan-No-Ou-To-Michelia.html'
print(getSeriesChapters(data).call())