import requests
from lxml import html

# this file is only for get chapters of serie.

#? For this page is necesary to create a promp for select te correct link.
#? i planing to create an interface for select or a comparer with other page

# TODO: need to pass in a environment variable files.

class SearchSeriesResult:
    BASE_URL = "https://es.novelcool.com/search/?wd="

    def __init__(self, serie_name):
      self.serie_name = serie_name

    def call(self):
      return self._format_data()

    def _search_serie_url(self):
      serie_name_formated = self.serie_name.replace(' ', '+')

      return self.BASE_URL + serie_name_formated

    def _get_html_of_page(self):
      # TODO: missing validations
      #* 1. validate and send error if the url is invalid
      #* 1. validate requests
      # search_serie_url = self._search_serie_url()
      # search_serie_page = requests.get(search_serie_url)
      #! Only for testing
      with open('madan_nosearch.html', 'r', encoding='utf-8') as archivo:
        # Leer el contenido del archivo
        chapter_manga_content = archivo.read()

      return chapter_manga_content #search_serie_page.text

    def _format_data(self):
      serie_results_content = self._get_html_of_page()
      html_tree = html.fromstring(serie_results_content)
      series_search_results_html = html_tree.xpath('//div[@class="book-item"]')

      return  list(map(lambda result: (
        {
          'name': result.xpath('.//div[@class="book-pic"]/@title')[0],
          'type': result.xpath('.//div[contains(@class, "book-type")]/text()')[0],
          'scoring': result.xpath('.//div[@class="book-rate-num"]/text()')[0],
          'views': result.xpath('.//div[@class="row-item book-data-num"]/text()')[0],
          'date_modified': result.xpath('.//span[@class="book-data-time" and @itemprop="dateModified"]/text()')[0],
          'profil_url': result.xpath('.//a[@itemprop="url"]/@href')[0],
          'image_url': result.xpath('.//img[@itemprop="image"]')[0]
        }
      ), series_search_results_html))
