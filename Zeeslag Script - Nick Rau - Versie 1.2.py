# Geinporteerde modules
import turtle
import random
import time
from playsound import playsound

# Globale variabelen voor het hele bord
vullijst = []
aantalvakken = 10

#################################### VISUALISATIE BORD #####################################

# Globale variabelen voor de visualisatie
boxsize = 50
rijstart = -350
kolomstart = 250
bordbreedte = rijstart + boxsize*aantalvakken
bordlengte = kolomstart - boxsize*aantalvakken

# Functie die een vierkant tekent en een vulkleur geeft.
def boxmaker(x, y, color):
      win = turtle.Turtle()
      win.speed(0)
      win.hideturtle()
      win.color(color)
      win.begin_fill()
      box(x, y, win)
      win.end_fill()

# Functie die draait als het spel is afgelopen
def spelklaar():
      # De eind tijd pakken, de vertreken tijd berekenen en converteren in een leesbaar getal
      global eind_tijd
      eind_tijd = time.time()
      vertreken_tijd = eind_tijd - start_tijd
      vertreken_tijd_seconden = str("{:.1f}".format(vertreken_tijd)) + ' seconden'

      # Scherm oproepen
      klaar = turtle.Screen()
      klaar.clear()

      # Titel
      title = turtle.Turtle()
      title.hideturtle()
      title.penup()
      title.goto(0,300)
      title.write('Gewonnen!!!', True, align="center", font=("Stencil", "40"))

      # Aantal bommen met label
      bommen_titel = turtle.Turtle()
      bommen_titel.hideturtle()
      bommen_titel.penup()
      bommen_titel.goto(0,200)
      bommen_titel.write('Bommen gebruikt', True, align="center", font=("Stencil", "20"))

      bommen = turtle.Turtle()
      bommen.hideturtle()
      bommen.penup()
      bommen.goto(0,160)
      bommen.write(gebruikte_bommen, True, align="center", font=("Stencil", "20"))

      # Speeltijd met label
      speeltijd_titel = turtle.Turtle()
      speeltijd_titel.hideturtle()
      speeltijd_titel.penup()
      speeltijd_titel.goto(0,80)
      speeltijd_titel.write('Speeltijd', True, align="center", font=("Stencil", "20"))

      speeltijd = turtle.Turtle()
      speeltijd.hideturtle()
      speeltijd.penup()
      speeltijd.goto(0,30)
      speeltijd.write(vertreken_tijd_seconden, True, align="center", font=("Stencil", "20"))

      # Stopknop met label
      spelklaar_stopknop = turtle.Turtle()
      spelklaar_stopknop.penup()
      spelklaar_stopknop.goto(0,-50)
      spelklaar_stopknop.shape('square')
      spelklaar_stopknop.fillcolor('white')
      spelklaar_stopknop.shapesize(3,9)
      spelklaar_stopknop.onclick(return_naar_main)

      spelklaar_stoplabel = turtle.Turtle()
      spelklaar_stoplabel.penup()
      spelklaar_stoplabel.hideturtle()
      spelklaar_stoplabel.goto(0,-62)
      spelklaar_stoplabel.write('Stoppen', True, align="center", font=("Stencil", "15"))


"""
Functie die de x en y coordinaten van het scherm neemt en kijkt waar je zit en waar in de lijst dit is.
Zolang de teller waarden binnen het aantal gegeven vakken zit. Kijkt de functie of de coordinaten van het
onscreenclick tussen een van de vakjes zit. Zodra het juiste vakje is gevonden kijkt de functie waar in de lijst dit is
en kijkt daarna of hier een schip zit.
"""
def bord_plaats_checker(x, y, rij, kolom):
      # Globale variabelen oproepen die gewijzigd gaan worden
      global geraakte_schepen
      global gebruikte_bommen
      # Checken of in het bord op plaats y_coor en x_coor een schip zit of niet.
      if compbord[x][y] != 'O':

            # Er zit een schip, dus rood vierkant tekenen.
            boxmaker(rij, kolom, "red")
            playsound('oof.mp3')
            if bombord[x][y] == 'O':
                  bombord[x][y] = 'X'
                  geraakte_schepen+=1
                  gebruikte_bommen+=1
                  if geraakte_schepen == 17:
                        spelklaar()

      else:
            # Er zit geen schip, dus zwart vierkant tekenen.
            boxmaker(rij, kolom, "black")
            if bombord[x][y] == 'O':
                  bombord[x][y] = 'X'
                  gebruikte_bommen+=1

def bordchecker_single(x,y):
      x, y, rij, kolom = bordchecker(x,y)
      # Checken of in het bord op plaats y_coor en x_coor een schip zit of niet.
      bord_plaats_checker(x, y, rij, kolom)
      
def bordchecker(x, y):
      # Startcoordinaten voor de rij en de kolom
      rij = rijstart
      kolom = kolomstart

      # Teller variabelen
      x_counter = 0
      y_counter = 0

      # Boolean variabel voor de zolang lussen
      rij_niet_klaar = True

      # Zolang de x_counter kleiner is dan het aantal vakken
      while rij_niet_klaar and x_counter < aantalvakken:

            # Checken of de x waarde groter is dan de rij coordinaat en
            # kleiner is dan de rijcoordinaat + de grootte van de box.
            if x > rij and x < rij+boxsize:

                  # Geef waarde x_coor de waarde van x_counter zodat die plaats in de lijst opgezocht kan worden
                  x_coor = x_counter

                  # Zolang de y_counter kleiner is dan het aantalvakken
                  while rij_niet_klaar and y_counter < aantalvakken:

                        # Checken of de y waarde kleiner is dan de kolom coordinaat en
                        # groter is dan de kolom coordinaat - boxsize.
                        if y < kolom and y > kolom-boxsize:

                              # y_coor de waarde van y_counter geven zodat die plaats in de lijst opgezocht kan worden
                              y_coor = y_counter

                              # Rij_klaar boolean veranderen naar True zodat de zolang lussen niet doorgaan.
                              rij_niet_klaar = False

                              return y_coor, x_coor, rij, kolom

                        else:
                              # Kolom naar beneden plaatsen. Grootte is de grootte van één vierkant in dit geval 'boxsize'.
                              kolom = kolom-boxsize

                        # 1 bij y_counter optellen
                        y_counter+=1
            else:
                  # Rij naar rechts verplaatsen en opnieuw checken. Grootte is de grootte van één vierkant in dit geval 'boxsize'.
                  rij = rij+boxsize

            # 1 bij x_counter optellen
            x_counter+=1

# Functie om een vierkant te tekenen
def box(x, y, box):
      box.penup()
      box.setposition(x, y)
      box.pendown()
      box.forward(boxsize)
      box.right(90)
      box.forward(boxsize)
      box.right(90)
      box.forward(boxsize)
      box.right(90)
      box.forward(boxsize)
      box.right(90)

# Functie die het bord op het scherm tekent
def bord():
      x = rijstart
      name = turtle.Turtle()
      name.speed(0)
      name.hideturtle()
      for rij in range(0,aantalvakken):
        y = kolomstart
        for kolom in range(0,aantalvakken):
            box(x, y, name)
            y-=boxsize
        x+=boxsize


"""
Functie die de schepen plaatst.
De functie checkt waar in het bord je bent en hoe het schip geplaatst kan worden.
Dit kan horizontaal en verticaal. Ook wordt er rekening gehouden met waar de andere schepen staan.
"""
def schip_plaatser(schip, schipgrote, richting, x, y, bord):
      ######################  HORIZONTAAL  ########################
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
      elif richting ==  2:
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

# Functie om de twee dimentionale lijsten voor het spel te maken en de schepen te plaatsen.
def bordmaker(aantalboxen, players):
    bord = []

    global geraakte_schepen
    global gebruikte_bommen
    geraakte_schepen = 0
    gebruikte_bommen = 0
    
    # If statement die checkt om het spel singleplayer of multiplayer wordt.
    if players == 1:
        ############### SINGLEPLAYER ###############
        for x in range(0, aantalboxen):
            # De rijen van het bord maken aan de hand van de eerder aangegeven grootte
            bord.append([])

            for y in range(0, aantalboxen):
                # De kolommen maken met dezelfde groottte
                bord[x].append('O')
        return bord

def visual_schip_plaatser(x,y):
      print(x,y)
      x, y, rij, kolom = bordchecker(x,y)
      schip_plaatser('S', 5, 2, x, y, bord_player1)
      for row in bord_player1:
            print(row)
       
#################################### CONSOLE + MENU #####################################

# Deze functie is om cheats codes in te vullen in de console.
def cheats():
    print("{:{fill}{align}{width}}".format('CONSOLE MENU', fill='#', align='^', width=60))
    consoleinput = input('Geef een commando: ')
    if str.lower(consoleinput) == 'radar':
        print('Hacking into the mainframe...')
        print('Disabling all the algoritms...\n')
        for row in compbord:
            print(row)
    else:
        print('Onbekend Commando!!!')


# Deze functie start de singleplayer op.
def keuze_1(x,y):
    # Scherm oproepen en leegmaken
    window = turtle.Screen()
    window.clear()

    # Maak het bord, teken dit bord op het scherm en zet de onscreenclick klaar.
    global compbord
    global bombord
    compbord = bordmaker(aantalvakken, 1)
    bombord = bordmaker(aantalvakken, 1)

    # Slagschip plaatsen
    while not schip_plaatser('S', 5, random.randint(1,2), random.randint(0,aantalvakken-1), random.randint(0,aantalvakken-1), compbord):
          print()

    # Kruiser plaatsen
    while not schip_plaatser('K', 4,  random.randint(1,2), random.randint(0,aantalvakken-1), random.randint(0,aantalvakken-1), compbord):
          print()

    # Eerste fregat plaatsen
    while not schip_plaatser('F', 3,  random.randint(1,2), random.randint(0,aantalvakken-1), random.randint(0,aantalvakken-1), compbord):
          print()

    # Tweede fregat plaatsen
    while not schip_plaatser('F', 3,  random.randint(1,2), random.randint(0,aantalvakken-1), random.randint(0,aantalvakken-1), compbord):
          print()

    # Mijnenveger plaatsen
    while not schip_plaatser('M', 2,  random.randint(1,2), random.randint(0,aantalvakken-1), random.randint(0,aantalvakken-1), compbord):
          print()

    bord()
    
    global start_tijd
    start_tijd = time.time()
    window.onscreenclick(bordchecker_single)

    # Stop knop om het spel te stoppen met label
    stopknop = turtle.Turtle()
    stopknop.penup()
    stopknop.goto(350,300)
    stopknop.shape('square')
    stopknop.fillcolor('white')
    stopknop.shapesize(3,9)
    stopknop.onclick(return_naar_main)

    stopknop_label = turtle.Turtle()
    stopknop_label.penup()
    stopknop_label.hideturtle()
    stopknop_label.goto(350,287)
    stopknop_label.write('Stoppen', True, align="center", font=("Stencil", "15"))

    # Knop om het cheat menu te openen in de console
    window.onkey(cheats, "=")
    window.listen()

    # Mainloop die het spel laat wachten op een onkey of onclick
    window.mainloop()

def keuze_2(x,y):
    # Scherm oproepen en leegmaken
    window = turtle.Screen()
    window.clear()

    bord()
    global bord_player1
    bord_player1 = bordmaker(aantalvakken, 1)

    # Slagschip
    slagschip = turtle.Turtle()
    slagschip.penup()
    slagschip.speed(0)
    slagschip.goto(350,200)
    slagschip.shape('square')
    slagschip.shapesize(2,2)
    slagschip.fillcolor('red')
    slagschip.ondrag(slagschip.goto)
    slagschip.onrelease(visual_schip_plaatser)

    # Stop knop om het spel te stoppen met label
    stopknop = turtle.Turtle()
    stopknop.penup()
    stopknop.goto(350,300)
    stopknop.shape('square')
    stopknop.fillcolor('white')
    stopknop.shapesize(3,9)
    stopknop.onclick(return_naar_main)

    stopknop_label = turtle.Turtle()
    stopknop_label.penup()
    stopknop_label.hideturtle()
    stopknop_label.goto(350,287)
    stopknop_label.write('Stoppen', True, align="center", font=("Stencil", "15"))

    window.mainloop()
def return_naar_main(x,y):
      main()
      
# Functie om het spel af te sluiten.
def spelstop(x,y):
    exit()

# Main functie die het hele spel start
def main():
    # Scherm oproepen
    window = turtle.Screen()
    window.clear()
    window.title('Zeeslag menu')

    # Title voor in het scherm
    titel = turtle.Turtle()
    titel.hideturtle()
    titel.penup()
    titel.goto(0,300)
    titel.write('Zeeslag', True, align="center", font=("Stencil", "40"))

    # Menuknop 1 met de label
    menuknop_1 = turtle.Turtle()
    menuknop_1.penup()
    menuknop_1.goto(0,100)
    menuknop_1.shape('square')
    menuknop_1.fillcolor('white')
    menuknop_1.shapesize(3,9)
    menuknop_1.onclick(keuze_1)

    menuknop_1_label = turtle.Turtle()
    menuknop_1_label.penup()
    menuknop_1_label.hideturtle()
    menuknop_1_label.goto(0,88)
    menuknop_1_label.write('1 Speler', True, align="center", font=("Stencil", "15"))

    # Menuknop 2 met de label
    menuknop_2 = turtle.Turtle()
    menuknop_2.penup()
    menuknop_2.goto(0,0)
    menuknop_2.shape('square')
    menuknop_2.fillcolor('white')
    menuknop_2.shapesize(3,9)
    menuknop_2.onclick(keuze_2)

    menuknop_2_label = turtle.Turtle()
    menuknop_2_label.penup()
    menuknop_2_label.hideturtle()
    menuknop_2_label.goto(0,-12)
    menuknop_2_label.write('2 Spelers', True, align="center", font=("Stencil", "15"))

    # Stopknop met label
    Stopknop = turtle.Turtle()
    Stopknop.penup()
    Stopknop.goto(0,-100)
    Stopknop.shape('square')
    Stopknop.fillcolor('white')
    Stopknop.shapesize(3,9)
    Stopknop.onclick(spelstop)

    Stopknop_label = turtle.Turtle()
    Stopknop_label.penup()
    Stopknop_label.hideturtle()
    Stopknop_label.goto(0,-112)
    Stopknop_label.write('Afsluiten', True, align="center", font=("Stencil", "15"))
    
# If statement die de main functie oproept zodat het spel alleen vanuit dit script automatisch gestart wordt.
if __name__ == "__main__":
      main()
