import pygame as pg

# Initialiserer/starter pygame
pg.init()

clock = pg.time.Clock()
fps = 10
# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, fart, radius, vindusobjekt):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.fart = fart
    self.radius = radius
    self.vindusobjekt = vindusobjekt
    self.pygameobjekt = pg.Rect(self.x, self.y, self.radius, self.radius)
  
  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(self.vindusobjekt, (255, 69, 0), (self.x, self.y), self.radius) 

  def flytt(self):
    """Metode for å flytte ballen"""
    # Sjekker om ballen er utenfor høyre/venstre kant
    if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
      self.fart = -self.fart
    
    # Flytter ballen
    self.x += self.fart

# Lager et Ball-objekt
ball = Ball(250, 250, 10/fps, 20, vindu)

# Gjenta helt til brukeren lukker vinduet
fortsett = True

short_time = 0
while fortsett:
    if short_time >=20:
        fortsett = False
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
        if event.type == pg.MOUSEBUTTONUP:
            if ball.pygameobjekt.collidepoint(event.pos):
                # man har klikket i firkanten
                # … hva skal skje da
                #print(event.pos)
                fortsett = False
                mouseX, mouseY = event.pos #hvis man trenger dem til noe
                
        elif event.type == pg.KEYDOWN:
            pass
            #fortsett = False
            # pygame.KEYUP
            # en gang pr tast
            if event.key == pg.K_LEFT:
                forsett = False
                # … flytt rektangel til venstre
                #if rektangel.colliderect(målrektangel):
                    # man har truffet målet
                    # … hva skal skje da

    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235))

    # Tegner og flytter ballen
    ball.tegn()
    ball.flytt()
    #ball.rect.update(ball.x, ball.y, ball.radius, ball.radius)

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()
    clock.tick(fps)
    short_time +=1/fps

# Avslutter pygame
pg.quit()