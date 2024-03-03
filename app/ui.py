
def ask_profil_url():
  print('Hi!!! Welcome to webscraping app')
  print('First you need to introduce the url profil')
  return input("url: ")

def ask_for_get_panels():
  print('you want to get the panels?')
  print('1.Yes 2.No')
  return input("option: ")

def ask_for_get_panels_or_get_new_serie():
  print("you whant to get panels or get new serie")
  print('1.new serie')
  print('2.get panels')
  print('3.download chapter')
  return input("option: ")

def ask_for_serie_to_get_panels(options):
  print("Currents options")
  for i, option in enumerate(options):
    print(f"{i + 1}. {option}")
  return input("option: ")
