import requests
from lxml import html
import time

class GetSeriesPanel:
  def __init__(self, serie_data):
    self.serie_data = serie_data
    self.chapters = serie_data['chapters']
    #! only for testing
    self.chapter = self.chapters[0]

  def _get_html_of_page(self):
    # chapter_url = self.chapter["chapter_url"]
    # print(chapter_url)
    # serie_panels_page_content = requests.get(chapter_url)

    # #! Only for testing
    # with open('pagina_web_1.html', 'w', encoding='utf-8') as archivo:
    #     archivo.write(serie_panels_page_content.text)

    with open('pagina_web_1.html', 'r', encoding='utf-8') as archivo:
      # Leer el contenido del archivo
      chapter_manga_content = archivo.read()

    html_tree = html.fromstring(chapter_manga_content)

    print(self.next_page(html_tree, "https://es.novelcool.com/chapter/Vol-1-Ch-1/4314037-10-1.html"))
    print(self.panels_link(html_tree))
    # return chapter_manga_content

  def _panels(self, url, panels_result=[]):
    if url:
      serie_panels_page_content = requests.get(url)
      html_code = serie_panels_page_content.text
      html_tree = html.fromstring(html_code)

      next_url = self.next_page(html_tree, url)
      panels_result = panels_result + self.panels_link(html_tree)

      time.sleep(5)
      return self._panels(next_url, panels_result)
    else:
      return panels_result

  def next_page(self, html_tree, current_url):
    next_page_container = html_tree.xpath(f'//select[@class="sl-page"]/option[@value="{current_url}"]')[0]
    next_page_url = next_page_container.xpath('following-sibling::option/@value')

    return None if next_page_url == [] else next_page_url[0]

  def panels_link(self, html_tree):
    panels_html = html_tree.xpath('//div[@class="pic_box text-center"]')

    return list(map(lambda panel: (
      {
        'page_number': list(html_tree.xpath('//select[@class="sl-page"]/option[@selected]/text()')[0])[0],
        'panel_number': panel.xpath('.//img/@i')[0],
        'panel_url': panel.xpath('.//img/@src')[0]
      }
    ), panels_html))

#! only for testing
data = {'name': 'Madan No Ou To Michelia', 'type': 'Manga', 'scoring': '0.0', 'views': '331', 'date_modified': 'Jun 21, 2020', 'profil_url': 'https://es.novelcool.com/novel/Madan-No-Ou-To-Michelia.html', 'chapters': [{'number': 'Capítulo 10', 'chapter_url': 'https://es.novelcool.com/chapter/Vol-1-Ch-1/4314037-10-1.html', 'date_modified': 'Jun 21, 2020'}, {'number': 'Capítulo 9', 'chapter_url': 'https://es.novelcool.com/chapter/Cap-tulo-9/4647958/', 'date_modified': 'May 29, 2020'}, {'number': 'Capítulo 8', 'chapter_url': 'https://es.novelcool.com/chapter/Cap-tulo-8/4625219/', 'date_modified': 'May 21, 2020'}, {'number': 'Capítulo 7', 'chapter_url': 'https://es.novelcool.com/chapter/Cap-tulo-7/4517633/', 'date_modified': 'Apr 20, 2020'}, {'number': 'Capítulo 6', 'chapter_url': 'https://es.novelcool.com/chapter/Cap-tulo-6/4470092/', 'date_modified': 'Apr 13, 2020'}, {'number': 'Capítulo 5', 'chapter_url': 'https://es.novelcool.com/chapter/Cap-tulo-5/4470091/', 'date_modified': 'Apr 13, 2020'}, {'number': 'Capítulo 4', 'chapter_url': 'https://es.novelcool.com/chapter/Cap-tulo-4/4375590/', 'date_modified': 'Mar 07, 2020'}, {'number': 'Vol. 1 Ch. 3', 'chapter_url': 'https://es.novelcool.com/chapter/Vol-1-Ch-3/4355122/', 'date_modified': 'Feb 29, 2020'}, {'number': 'Ch. 2', 'chapter_url': 'https://es.novelcool.com/chapter/Ch-2/4318426/', 'date_modified': 'Feb 18, 2020'}, {'number': 'Vol. 1 Ch. 1', 'chapter_url': 'https://es.novelcool.com/chapter/Vol-1-Ch-1/4314037/', 'date_modified': 'Feb 16, 2020'}]}

print(GetSeriesPanel(data)._panels('https://es.novelcool.com/chapter/Vol-1-Ch-1/4314037-10-1.html', []))


# ! missing only refactor, save data in json and download
