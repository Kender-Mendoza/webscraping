import requests
from lxml import html

class GetSeriesChapters:
  def __init__(self, profil_url):
    self.profil_url = profil_url
    content_page = self._html_of_page()
    self.html_tree = html.fromstring(content_page)

  def call(self):
    return self._add_chapters_to_serie_info()

  def _html_of_page(self):
    # serie_profil_page_content = requests.get(self.profil_url)

    # Todo: try catch
    # #! Only for testing
    with open(('Madan No Ou To Michelia.html'), 'r', encoding='utf-8') as archivo:
      # Leer el contenido del archivo
      chapter_manga_content = archivo.read()

    return chapter_manga_content

    # return serie_profil_page_content.text

  def _serie_data(self):
    serie_profil_info = self.html_tree.xpath('//div[@class="bookinfo-module"]')[0]

    return {
      'name': serie_profil_info.xpath('.//h1[@class="bookinfo-title"]/text()')[0],
      'type': serie_profil_info.xpath('.//div[@class="book-type book-type-manga"]/text()')[0],
      'pic_img': serie_profil_info.xpath('.//img[@class="bookinfo-pic-img"]/@src')[0]
    }

  def _format_chapter_url(self, chapter_url):
    return chapter_url[:-1] + '-10-1.html'

  def _chapters_data(self):
    serie_profil_chapters_html = self.html_tree.xpath('//div[@class="chp-item"]')

    return list(map(lambda chapter: (
      {
        'number': chapter.xpath('.//a/@title')[0],
        'chapter_url': self._format_chapter_url(chapter.xpath('.//a/@href')[0]),
        'date_modified': chapter.xpath('.//span[@class="chapter-item-time"]/text()')[0]
      }
    ), serie_profil_chapters_html))

  def _add_chapters_to_serie_info(self):
    serie_data = self._serie_data()
    serie_data['chapters'] = self._chapters_data()

    return serie_data
