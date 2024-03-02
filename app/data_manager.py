import json

class DataManager:
  _instance = None
  __DB_NAME = "/Users/kender/workspace/webscraping/data/db.json"

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)

    return cls._instance

  def save(self, data):
    try:
      if not self.can_save_data(data['key_id']):
        print('The element exist')
        return None

      old_data = list(self._read_data())
      json_string = json.dumps(data)
      data_to_save = [json.loads(json_string)]
      new_data = old_data + data_to_save
      self._write_data(new_data)

      return True
    except:
      print('Error: data can saved')
      return None

  def can_save_data(self, data_url):
    keys = self._key_id_saved()

    return False if data_url in keys else True

  def find_by_key_id(self, key_id):
    data_saved = list(self._read_data())

    return next((element for element in data_saved if element['key_id'] == key_id), None)

  def _key_id_saved(self):
    data_saved = list(self._read_data())

    return list(map(lambda element: (element['key_id']), data_saved))

  def _read_data(self):
    with open(self.__DB_NAME, 'r') as file:
      data = file.read()

    return json.loads(data or "[]")

  def _write_data(self, data):
    with open(self.__DB_NAME, 'w') as file:
      json.dump(data, file, indent=4)
