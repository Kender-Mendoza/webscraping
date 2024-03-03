import requests
from lxml import html

class BuildHtmlTreeService:
  def html_tree_of_page(self, url):
    try:
      page_content = requests.get(url)

      return html.fromstring(page_content.text)

    except Exception as e:
      print('Error: ', type(e).__name__)

      return None
