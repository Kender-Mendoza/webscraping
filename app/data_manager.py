import json

class DataManager:
  _instance = None
  __DB_NAME = "./db/db.json"

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)

    return cls._instance

  def save(self, data):
    # TODO: validate data
    old_data = list(self._read_data())
    data_to_save = [json.loads(data)]
    new_data = old_data + data_to_save
    self._write_data(new_data)

    return True

  def _read_data(self):
    with open(self.__DB_NAME, 'r') as file:
      data = file.read()

    return json.loads(data or "[]")

  def _write_data(self, data):
    with open(self.__DB_NAME, 'w') as file:
      json.dump(data, file, indent=4)
