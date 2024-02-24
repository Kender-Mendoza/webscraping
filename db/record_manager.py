import json

# TODO: use singletow metodology

class RecordManager:
  def __init__(self):
    self.name = "./db/db.json"

  def save(self, data):
    # TODO: validate data
    old_data = list(self._read_data())
    data_to_save = [json.loads(data)]
    new_data = old_data + data_to_save
    self._write_data(new_data)

    return True

  def _read_data(self):
    with open(self.name, 'r') as file:
      data = file.read()

    return json.loads(data or "[]")

  def _write_data(self, data):
    with open(self.name, 'w') as file:
      json.dump(data, file, indent=4)
