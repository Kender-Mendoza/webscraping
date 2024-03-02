import requests
from lxml import html
import time

class SeriesPanelsService:
  def __init__(self, chapter):
    self.chapter = chapter

  def call(self):
    url = self.chapter['url']
    self.chapter['panels'] = self._panels(url)

    return self.chapter

  def _panels(self, url, panels_result=[]):
    if url:
      serie_panels_page_content = requests.get(url)
      html_code = serie_panels_page_content.text
      html_tree = html.fromstring(html_code)

      next_url = self._next_page(html_tree, url)
      panels_result = panels_result + self._panels_link(html_tree)

      time.sleep(5)

      return self._panels(next_url, panels_result)
    else:
      return panels_result

  def _next_page(self, html_tree, current_url):
    next_page_container = html_tree.xpath(f'//select[@class="sl-page"]/option[@value="{current_url}"]')[0]
    next_page_url = next_page_container.xpath('following-sibling::option/@value')

    return None if next_page_url == [] else next_page_url[0]

  def _panels_link(self, html_tree):
    panels_html = html_tree.xpath('//div[@class="pic_box text-center"]')

    return list(map(lambda panel: (
      {
        'page_number': list(html_tree.xpath('//select[@class="sl-page"]/option[@selected]/text()')[0])[0],
        'panel_number': panel.xpath('.//img/@i')[0],
        'panel_url': panel.xpath('.//img/@src')[0]
      }
    ), panels_html))
