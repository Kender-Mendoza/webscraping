from resources.scripts.build_html_tree_service import BuildHtmlTreeService
from resources.scripts.download_serie_service import DownloadSerieService
from resources.scripts.nvlcl.series_info_service import SeriesInfoService
from resources.scripts.nvlcl.series_panels_service import SeriesPanelsService
from app.data_manager import DataManager
from app.ui import ask_profil_url, ask_for_get_panels, ask_for_get_panels_or_get_new_serie, ask_for_serie_to_get_panels

#! Decidi finalizar con lo que falta en este proyecto y dejarlo como prueba y base para continuarlo en swift
#! ya que me conviene mas que una aplicación web, por la razon de que voy a manejar cosas en local ademas de
#! mover archivos y tener un control de estos, asi que por el momento se me ocurrio esta solución tambien esta
#! la opción de manejar con una aplicacion web pero al manejar cosas del local siento que no conviene.
#! otra opción seria manejar la aplicación con dos interfaces una de descarga y manejo de archivo en swift
#! y otra para hacer scraping con python. pero no tendria mucho sentido ya que tendria que usar dos interfaces para
#! administrar.

#? Se me ocurrio hacer todo web y que al final se descargue un zip con la serie o capitulo y yo ya decidir donde guardar.

# * buscar un orden para los archivos.

# * buscar una forma para hacer testcases.
# * refactorizar luego de los testcasese ademas del perform.

# * refactorizar la parte de los import
# * refactorizar la parte de las path para que no esten quemada la ruta absoluta

# * analizar mientras se realiza el readme el alcance de la app para ver que es lo que quiero que haga
# * ver la instalación de los paquetes y la ejecución
# * ver si tendra prop en terminal o se hara un paquete

# * ver si sera consumida por una app web o una app en swift o ambas
# * crear clases nuevas para nuevas webs y aprobechar la poo

get_panels_or_new_serie_option = ask_for_get_panels_or_get_new_serie()

if get_panels_or_new_serie_option == '1':
  # ? new serie or update exist serie
  profil_url = ask_profil_url()
  html_tree = BuildHtmlTreeService().html_tree_of_page(profil_url)
  if html_tree is None:
    print('URL invalida')
  else:
    serie_data = SeriesInfoService(html_tree).call()

    if DataManager().save(serie_data) is None:
      print(serie_data)
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
elif get_panels_or_new_serie_option == '2':
  # ? get url for panels
  get_panels_option = ask_for_get_panels()
  if get_panels_option == "1":
    series_saved = DataManager().get_all()
    options = list(map(lambda serie: serie['name'], series_saved))

    option_selected = ask_for_serie_to_get_panels(options)
    serie_saved = series_saved[int(option_selected) - 1]
    chapter_to_download = serie_saved['pending_chapters'].pop(0)

    if 'chapters' not in serie_saved:
      serie_saved["chapters"] = []

    chapters_panels = SeriesPanelsService(chapter_to_download).call()
    serie_saved['chapters'].append(chapters_panels)
    if DataManager().update(serie_saved): print('serie updated')
elif get_panels_or_new_serie_option == '3':
  # ? download panels
  series_saved = DataManager().get_all()
  options = list(map(lambda serie: serie['name'], series_saved))
  option_selected = ask_for_serie_to_get_panels(options)
  serie_saved = series_saved[int(option_selected) - 1]
  serie_saved = DownloadSerieService(serie_saved).call()
  if DataManager().update(serie_saved): print('serie updated')
