class Planet:
   
  def __init__(self, navn, solavstand, radius, a, b, c ,d, e, f,
               g: int = 10,
               h: int = 5):
    self.navn = navn
    self.solavstand = solavstand
    self.radius = radius
  
  def __str__(self):
    return f"Planeten {self.navn} er {self.solavstand} millioner km unna sola og har radius {self.radius} km."
  
  def print(self):
    print(f"Planeten {self.navn} er {self.solavstand} millioner km unna sola og har radius {self.radius} km.")

	def print():#klassemetode
  	print("Planet!lol")
      
jupiter = Planet("Jupiter", 778.5, 69911)

print(jupiter)