class SeriesInfoService:
  def __init__(self, html_tree):
    self.html_tree = html_tree

  def call(self):
    serie_data = self._serie_data()
    serie_data['key_id'] = serie_data['name'].lower().strip().replace(' ', '_')
    serie_data['pending_chapters'] = self._pendign_chapters_data()

    return serie_data

  def _serie_data(self):
    serie_profil_info = self.html_tree.xpath('//div[@class="bookinfo-module"]')[0]

    return {
      'name': serie_profil_info.xpath('.//h1[@class="bookinfo-title"]/text()')[0],
      'type': serie_profil_info.xpath('.//div[@class="book-type book-type-manga"]/text()')[0],
      'pic_img': serie_profil_info.xpath('.//img[@class="bookinfo-pic-img"]/@src')[0],
      'state': serie_profil_info.xpath('.//div[@class="bk-cates"]')[0].xpath('.//a/text()')[0]
    }

  def _pendign_chapters_data(self):
    serie_profil_chapters_html = self.html_tree.xpath('//div[@class="chp-item"]')

    return list(map(lambda chapter: (
      {
        'number': chapter.xpath('.//a/@title')[0],
        'url': self._format_chapter_url(chapter.xpath('.//a/@href')[0]),
        'date_modified': chapter.xpath('.//span[@class="chapter-item-time"]/text()')[0]
      }
    ), serie_profil_chapters_html))

  def _format_chapter_url(self, chapter_url):
    return chapter_url[:-1] + '-10-1.html'
