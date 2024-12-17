import json

class Storage:
  def save-to-file(self, fileName, data):
    try:
      with open(fileName, "w") as file:
        json.dump(data, file)
    except Exception as error:
      print(f"Error saving to file: {error}")

  def load-from-file(self, fileName):
    try:
      with open(fileName, "r") as file:
        return json.load(file)
    except Exception as error:
      print(f"Error loading from file: {error}")
      return None
