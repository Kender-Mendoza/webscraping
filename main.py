from resources.scripts.build_html_tree_service import BuildHtmlTreeService
from resources.scripts.nvlcl.series_info_service import SeriesInfoService
from app.data_manager import DataManager
from app.ui import ask_profil_url

profil_url = ask_profil_url()
html_tree = BuildHtmlTreeService().html_tree_of_page('profil_url')
serie_data = SeriesInfoService(html_tree).call()

if DataManager().save(serie_data) is None:
  serie_saved = DataManager().find_by_key_id(serie_data['key_id'])

  # ? Checking state
  if serie_data['state'] != serie_saved['state']:
    serie_saved['state'] = serie_data['state']

  # ? Checking chapters
  serie_saved_chapters = list(map(lambda chapter: (chapter['url']), serie_saved['pending_chapters']))
  serie_saved_chapters += list(map(lambda chapter: (chapter['url']), serie_saved['chapters']))
  serie_data_chapters = list(map(lambda chapter: (chapter['url']), serie_data['pending_chapters']))

  if len(serie_saved_chapters) != len(serie_data_chapters):
    serie_data_chapters_set = set(serie_data_chapters)
    serie_saved_chapters_set = set(serie_saved_chapters)

    result = list(serie_data_chapters_set - serie_saved_chapters_set)

    if result != []:
      new_chapter = next((element for element in serie_data['pending_chapters'] if element['url'] == result[0]), None)
      serie_saved['pending_chapters'].append(new_chapter)
      if DataManager().update(serie_saved): print('serie updated')
