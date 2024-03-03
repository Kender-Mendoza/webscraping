import requests
import os
import time

class DownloadSerieService:
  def __init__(self, serie):
    self.serie = serie
    self.folder_path = f"/Users/kender/workspace/webscraping/temp/{serie['name']}"

  def call(self):
    self._create_folder(self.folder_path)
    self._download_chapter()

    return self.serie

  def _create_folder(self, path):
    if os.path.exists(path): return None

    os.mkdir(path)

    return True

  def _chapters_to_download(self):
    chapters_to_download = []
    for chapter in self.serie['chapters']:
      if chapter['donwloaded']: next

      chapter['donwloaded'] = True
      chapters_to_download += [chapter]

    return chapters_to_download

  def _download_chapter(self):
    for chapter in self._chapters_to_download():
      folder_chapter = f"{self.folder_path}/{chapter['number']}"
      self._create_folder(folder_chapter)
      for panel in chapter['panels']:
        extention = panel['panel_url'].split('.')[-1]
        panel_name = f"{panel['page_number']}.{panel['panel_number']}.{extention}"
        self._download_panel(f"{folder_chapter}/{panel_name}", panel['panel_url'])
        time.sleep(5)

  def _download_panel(self, file_path, url):
    response = requests.get(url)

    if response.status_code == 200:
      with open(file_path, 'wb') as file:
        file.write(response.content)
      print(f"{file_path} with url {url} downloaded")
    else:
      print(f"Error with file {file_path} and url {url}")
