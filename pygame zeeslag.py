#### IMPORTS ####
import pygame
import random
import time

# Scherm parameters
screenwidth = 1000
screenheight = 800

# Functie die het spel opstart
def setup():
      global scherm
      global clock
      pygame.init()
      scherm = pygame.display.set_mode((screenwidth, screenheight)) # Scherm
      pygame.display.set_caption("Zeeslag") # Titel voor scherm

      clock = pygame.time.Clock()

      # Achtergrond
      global bg
      bg = pygame.image.load('bg.jpg')
      bg = pygame.transform.scale(bg, (screenwidth, screenheight))

# Class die een button maakt en als je dit wil een achtergrond
class tekst(object):
      def __init__(self, tekst, fontnaam, grootte_tekst, posX_tekst, posY_tekst):
            self.tekst = tekst
            self.fontnaam = fontnaam
            self.grootte_tekst = grootte_tekst
            self.posX_tekst = posX_tekst
            self.posY_tekst = posY_tekst
            self.font = pygame.font.Font(fontnaam, grootte_tekst)
            self.textSurf, self.textRect = self.text_objects(tekst, self.font)
            self.drawTekst()

      def text_objects(self, text, font):
            textSurface = font.render(text, True, (0,0,0))
            return textSurface, textSurface.get_rect()

      def drawTekst(self):
            self.textRect.center = (self.posX_tekst, self.posY_tekst)
            scherm.blit(self.textSurf, self.textRect)

      def drawBG(self, lengte, breedte, X, Y, kleur):
            pygame.draw.rect(scherm, kleur,(X,Y,lengte,breedte))

# Class voor het bord met bijbehorende functies
class board(object):
      def __init__(self, box_size, aantalboxen):
            self.box_size = box_size
            self.aantalboxen = aantalboxen
            self.rijstart = 50
            self.kolomstart = 50
            self.compbord = []
            self.bombord = []
            self.geraakte_schepen = 0
            self.gebruikte_bommen = 0
            self.check_result = None

      def draw(self, win): # Functie die het bord tekent
            y = self.rijstart
            list_x = 0
            for row in self.compbord:
                  x = self.kolomstart
                  list_y = 0
                  for col in row:
                        if self.bombord[list_x][list_y] == 'O':
                              pygame.draw.rect(win, (0,0,255), (x,y,self.box_size,self.box_size))
                        else:
                              if self.compbord[list_x][list_y] != 'O':
                                    pygame.draw.rect(win, (255,0,0), (x,y,self.box_size,self.box_size))
                              else:
                                    pygame.draw.rect(win, (0,0,0), (x,y,self.box_size,self.box_size))
                        x+=self.box_size+4
                        list_y += 1
                  y+=self.box_size+4
                  list_x += 1

      
      def bordmaker(self): # Functie om de twee dimentionale lijsten voor het spel te maken en de schepen te plaatsen
            self.geraakte_schepen = 0
            self.gebruikte_bommen = 0
            self.bombord = []
            self.compbord = []

            ############### SINGLEPLAYER ###############
            for x in range(0, self.aantalboxen):
                  # De rijen van het bord maken aan de hand van de eerder aangegeven grootte
                  self.compbord.append([])
                  self.bombord.append([])

                  for y in range(0, self.aantalboxen):
                        # De kolommen maken met dezelfde groottte
                        self.compbord[x].append('O')
                        self.bombord[x].append('O')
                      
            # Slagschip plaatsen
            while not self.schip_plaatser('S', 5, random.randint(1,2), random.randint(0,self.aantalboxen-1), random.randint(0,self.aantalboxen-1), self.compbord):
                  print()

            # Kruiser plaatsen
            while not self.schip_plaatser('K', 4,  random.randint(1,2), random.randint(0,self.aantalboxen-1), random.randint(0,self.aantalboxen-1), self.compbord):
                  print()

            # Eerste fregat plaatsen
            while not self.schip_plaatser('F', 3,  random.randint(1,2), random.randint(0,self.aantalboxen-1), random.randint(0,self.aantalboxen-1), self.compbord):
                  print()

            # Tweede fregat plaatsen
            while not self.schip_plaatser('F', 3,  random.randint(1,2), random.randint(0,self.aantalboxen-1), random.randint(0,self.aantalboxen-1), self.compbord):
                  print()

            # Mijnenveger plaatsen
            while not self.schip_plaatser('M', 2,  random.randint(1,2), random.randint(0,self.aantalboxen-1), random.randint(0,self.aantalboxen-1), self.compbord):
                  print()
            for row in self.compbord:
                  print(row)

      def schip_plaatser(self, schip, schipgrote, richting, x, y, bord): # Functie die het schip plaatst in het bord
            if richting == 1:
                  if y + schipgrote > len(bord[x]):
                        #############  LINKSAF  ############
                        # For loop die checkt of er boven of onder het schip een ander schip zit.
                        i = 0
                        while i < schipgrote:
                              if x == 0:
                                    if bord[x+1][y-i] != 'O':
                                          return False
                              elif x == len(bord)-1:
                                    if bord[x-1][y-i] != 'O':
                                          return False
                              elif bord[x-1][y-i] != 'O' or bord[x+1][y-i] != 'O':
                                    return False
                              i+=1

                        # Checken of er voor of achter het schip een ander schip zit.
                        if y+1 < len(bord[x])-1:
                              if bord[x][y+1] != 'O':
                                    return False
                        if y-schipgrote > 0:
                              if bord[x][y-schipgrote] != 'O':
                                    return False

                        # For loop voor linksaf het schip te plaatsen
                        for i in range(y, y-schipgrote, -1):
                              if bord[x][i] == 'O':
                                    bord[x][i] = schip
                              else:
                                    return False
                        return True
                  else:
                        ########################  Rechtsaf  ########################
                        # For loop die checkt of er boven of onder een schip zit
                        i = 0
                        while i < schipgrote:
                              if x == 0:
                                    if bord[x+1][y+i] != 'O':
                                          return False
                              elif x == len(bord)-1:
                                    if bord[x-1][y+i] != 'O':
                                          return False
                              elif bord[x-1][y+i] != 'O' or bord[x+1][y+i] != 'O':
                                    return False
                              i+=1

                        # Checken of er voor of achter het schip een ander schip zit.
                        if y+schipgrote < len(bord[x])-1:
                              if bord[x][y+schipgrote] != 'O':
                                    return False
                        if y-1 > 0:
                              if bord[x][y-1] != 'O':
                                    return False
                              
                        # For loop voor rechtsaf
                        for i in range(y, y+schipgrote):
                              if bord[x][i] == 'O':
                                    bord[x][i] = schip
                              else:
                                    return False
                        return True
            elif richting == 2:
                  # Naar boven of naar beneden?
                  if x + schipgrote > len(bord):
                        ########################  Naar boven  ########################
                        i = 0
                        while i < schipgrote:
                              if y == 0:
                                    if bord[x-i][y+1] != 'O':
                                          return False
                              elif y == len(bord[x])-1:
                                    if bord[x-i][y-1] != 'O':
                                          return False
                              elif bord[x-i][y-1] != 'O' or bord[x-i][y+1] != 'O':
                                    return False
                              i+=1

                        if x+1 < len(bord)-1:
                              if bord[x+1][y] != 'O':
                                    return False
                        if x-schipgrote > 0:
                              if bord[x-schipgrote][y] != 'O':
                                    return False
                        
                        for i in range(x, x-schipgrote, -1):
                              if bord[i][y] == 'O':
                                    bord[i][y] = schip
                              else:
                                    return False
                        return True
                  else:
                        ########################  Naar onder  ########################
                        i = 0
                        while i < schipgrote:
                              if y == 0:
                                    if bord[x+i][y+1] != 'O':
                                          return False
                              elif y == len(bord[x])-1:
                                    if bord[x+i][y-1] != 'O':
                                          return False
                              elif bord[x+i][y-1] != 'O' or bord[x+i][y+1] != 'O':
                                    return False
                              i+=1

                        # Checken of er boven of onder het schip een ander schip zit
                        if x+schipgrote < len(bord)-1:
                              if bord[x+schipgrote][y] != 'O':
                                    return False
                        if x-1 > 0:
                              if bord[x-1][y] != 'O':
                                    return False

                        for i in range(x, x+schipgrote):
                              if bord[i][y] == 'O':
                                    bord[i][y] = schip
                              else:
                                    return False

                        return True
      def bordchecker(self, x, y, geraakte_schepen, gebruikte_bommen, win): # Functie die checkt of bij input een schip geraakt is of niet
            global player
            # Startcoordinaten voor de rij en de kolom
            rij = self.rijstart
            kolom = self.kolomstart

            # Teller variabelen
            x_counter = 0
            y_counter = 0

            # Boolean variabel voor de zolang lussen
            rij_niet_klaar = True

            # Zolang de x_counter kleiner is dan het aantal vakken
            while rij_niet_klaar and x_counter < self.aantalboxen:

                  # Checken of de x waarde groter is dan de rij coordinaat en
                  # kleiner is dan de rijcoordinaat + de grootte van de box.
                  if x > rij and x < rij+self.box_size+4:

                        # Geef waarde x_coor de waarde van x_counter zodat die plaats in de lijst opgezocht kan worden
                        x_coor = x_counter

                        # Zolang de y_counter kleiner is dan het aantalboxen
                        while rij_niet_klaar and y_counter < self.aantalboxen:

                              # Checken of de y waarde kleiner is dan de kolom coordinaat en
                              # groter is dan de kolom coordinaat - boxsize.
                              if y > kolom and y < kolom+self.box_size+4:

                                    # y_coor de waarde van y_counter geven zodat die plaats in de lijst opgezocht kan worden
                                    y_coor = y_counter

                                    # Rij_klaar boolean veranderen naar True zodat de zolang lussen niet doorgaan.
                                    rij_niet_klaar = False

                                    # Checken of in het bord op plaats y_coor en x_coor een schip zit of niet.
                                    if self.compbord[y_coor][x_coor] != 'O':

                                          # Er zit een schip.
                                          if self.bombord[y_coor][x_coor] == 'O':
                                                self.bombord[y_coor][x_coor] = 'X'
                                                self.geraakte_schepen+=1
                                                self.gebruikte_bommen+=1
                                                return True
                                          else:
                                                return False
                                    else:
                                          # Er zit geen schip
                                          if self.bombord[y_coor][x_coor] == 'O':
                                                self.bombord[y_coor][x_coor] = 'X'
                                                self.gebruikte_bommen+=1
                                                return True
                                          else:
                                                return False

                              else:
                                    # Kolom naar beneden plaatsen. Grootte is de grootte van één vierkant in dit geval 'boxsize'.
                                    kolom = kolom+self.box_size+4

                              # 1 bij y_counter optellen
                              y_counter+=1
                  else:
                        # Rij naar rechts verplaatsen en opnieuw checken. Grootte is de grootte van één vierkant in dit geval 'boxsize'.
                        rij = rij+self.box_size+4

                  # 1 bij x_counter optellen
                  x_counter+=1


# Functie om het scherm te updaten
def redrawgamescreen(player):
      # Scherm update en achtergrond toevoeging
      scherm.blit(bg, (0,0))
      
      if player == 1:
            player1.draw(scherm)
            playerName = tekst('Player 1 is aan de beurt', 'secret.ttf', 30, 700, 750)
      elif player == 2:
            player2.draw(scherm)
            playerName = tekst('Player 2 is aan de beurt', 'secret.ttf', 30, 700, 750)
      else:
            bord.draw(scherm)
      exitBTN = tekst('Stop', 'secret.ttf', 30, 900, 100)
      pygame.display.update()

def gewonnen(winnaar, bommen, verliezer = None, schepen_verliezer = None):
      global clock
      gewonnen_speler = 'Speler '+str(winnaar)+' heeft gewonnen!'
      bommen_gegooid = str(bommen)+' bommen zijn er gegooid'
      verloren_speler = 'Speler '+str(verliezer)+' heeft '+str(schepen_verliezer)+' schepen geraakt'
      
      run = True
      while run:
            clock.tick(27)
            for event in pygame.event.get():
                  if event.type ==pygame.QUIT:
                        run = False
                  if event.type == pygame.MOUSEBUTTONDOWN:
                        run = False
            scherm.blit(bg, (0,0))
            if winnaar != 0:
                  gewonnen_winnaar = tekst(gewonnen_speler, 'secret.ttf', 50, 500, 100)
                  verliezer = tekst(verloren_speler, 'secret.ttf', 25, 500, 570)
            else:
                  single_winnaar = tekst('Je hebt gewonnen!', 'secret.ttf', 50, 500, 100)
            gegooid = tekst(bommen_gegooid, 'secret.ttf', 25, 500, 620)
            
            terug = tekst('Klik op het scherm om terug te gaan', 'secret.ttf', 20, 500, 770)
            
            pygame.display.update()

# Functie die het spel start
def gamestart():
      global player
      global clock
      global bord
      global player1
      global player2
      run = True

      if player != None:
            print('-- Player 1 --')
            player1 = board(60, 10)
            player1.bordmaker()
            print('-- Player 2 --')
            player2 = board(60, 10)
            player2.bordmaker()
            print('Player 1 begint')
      else:
            bord = board(60, 10)
            bord.bordmaker()
      
      #### WHILE LOOP VOOR HET DRAAIEN VAN HET SPEL ####
      while run:
            clock.tick(27)
            #### For loop die de events uitvoert die opgevangen worden door het spel ####
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        run = False
                  if event.type == pygame.MOUSEBUTTONDOWN:
                        pos_click = pygame.mouse.get_pos()
                        if pos_click[0] > 855 and pos_click[0] < 940 and pos_click[1] > 80 and pos_click[1] < 120:
                              run = False
                        if player == 1:
                              if pos_click[0] > 50 and pos_click[0] < 50 + (player1.box_size + 4)*10 and pos_click[1] > 50 and pos_click[1] < 50 + (player1.box_size + 4)*10:
                                    player1.check_result = player1.bordchecker(pos_click[0], pos_click[1], 0, 0, scherm)
                                    redrawgamescreen(player)
                                    time.sleep(0.5)
                                    if player1.check_result == True:
                                          player = 2
                                    if player1.geraakte_schepen == 17:
                                          gewonnen(1, player1.gebruikte_bommen, 2, player2.geraakte_schepen)
                                          run = False
                                    redrawgamescreen(player)
                        elif player == 2:
                              if pos_click[0] > 50 and pos_click[0] < 50 + (player2.box_size + 4)*10 and pos_click[1] > 50 and pos_click[1] < 50 + (player2.box_size + 4)*10:
                                    player2.check_result = player2.bordchecker(pos_click[0], pos_click[1], 0, 0, scherm)
                                    redrawgamescreen(player)
                                    time.sleep(0.5)
                                    if player2.check_result == True:
                                          player = 1
                                    if player2.geraakte_schepen == 17:
                                          gewonnen(2, player2.gebruikte_bommen, 1, player1.geraakte_schepen)
                                          run = False
                                    redrawgamescreen(player)
                        else:
                              bord.check_result = bord.bordchecker(pos_click[0], pos_click[1], 0, 0, scherm)
                              if bord.geraakte_schepen == 17:
                                    gewonnen(0, bord.gebruikte_bommen)
                                    run = False
            redrawgamescreen(player)


def startmenu():
      setup()
      global clock
      global player
      intro = True
      #### WHILE LOOP VOOR HET DRAAIEN VAN HET SPEL ####
      while intro:
            clock.tick(27)
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        intro = False
                  if event.type == pygame.MOUSEBUTTONDOWN:
                        pos_click = pygame.mouse.get_pos()
                        if pos_click[0] > 350 and pos_click[0] < 650:
                              if pos_click[1] > 400 and pos_click[1] < 450:
                                    print('singleplayer')
                                    player = None
                                    gamestart()
                              elif pos_click[1] > 500 and pos_click[1] < 550:
                                    print('multiplayer')
                                    player = 1
                                    gamestart()
                                    
            scherm.blit(bg, (0,0))
            largeText = pygame.font.Font('secret.ttf',115)
            smallText = pygame.font.Font('secret.ttf',30)
            title = tekst('Zeeslag', 'secret.ttf', 115, screenwidth/2, screenheight/4)
            
            singleplayerBTN = tekst('singleplayer', 'secret.ttf', 30, 500, 420)
            multiplayerBTN = tekst('multiplayer', 'secret.ttf', 30, 500, 520)
            pygame.display.update()
      pygame.quit()

startmenu()

