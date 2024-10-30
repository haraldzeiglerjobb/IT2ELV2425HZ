class Maaned():
  def __init__(self, maanedsnummer):
    self._maanedsnummer = maanedsnummer
  
  def angiMaaned(self, maanedsnummer):
    if (maanedsnummer < 1 or maanedsnummer > 12):
      print("Månedsnummeret må være mellom 1 og 12.")
    else:
      self._maanedsnummer = maanedsnummer

  def hentMaaned(self):
    return self._maanedsnummer
  
januar = Maaned(2)
januar.angiMaaned(14)
januar.angiMaaned(1)
print(januar.hentMaaned())