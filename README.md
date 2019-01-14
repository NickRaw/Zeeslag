# Zeeslag
Dit is zeeslag geprogrammeerd in Python
Mijn opdracht van school was om het spel ‘Zeeslag’ te maken in python. Vooral de mode singleplayer moest ingebouwd zijn.

De bedoeling van het spel in singleplayer modus is dat de computer 5 schepen in het veld plaatst zonder dat jij dit ziet. Jij als speler moet die schepen zien te vinden en je bommen erop gooien. Als je op een vakje klikt krijg je een zwart vakje (geen schip) of een rood vakje (een schip). Heb je alle vakjes gehad dan moet het spel je een bericht geven dat je gewonnen hebt.

Daarnaast is er een cheats/console menu. Hier kom je bij door op '=' te drukken. Met commando ‘radar’ krijg je een bord te zien met alle schepen.

###################################### CHANGELOG VERSIE 1.2 ######################################
- bord_plaats_checker functie die x en y plaats van een 2D lijst gebruikt om te checken of op die plaats een schip zit en gebaseerd op het antwoord een zwart of rood vakje maakt met de rij en kolom coordinaten.

- bordchecker_single functie die de x en y waarden voor de 2D lijst en de rij en kolom coordinaten van de bordchecker functie nemen en die doorgeven aan de bord_plaats_checker. (GEMAAKT VOOR DE SINGLEPLAYER)

- bordchecker functie aangepast. Deze geeft nu de x en y waarden voor de 2D lijst en de rij en kolom coordinaten terug nodig voor de bord_plaats_checker en het teken van de box in het bord.

- Bij de bordmaker functie zijn compbord en bombord verwijderd. Deze staan nu in de keuze_1 functie (functie die de singleplayer start). In plaats daarvan is er nu één lijst variabel met de naam 'bord'. Deze wordt 2 dimensionaal gemaakt en terug gegeven. Voortaan kan deze functie opgeroepen worden door een variabel aan te maken en de functie hierin te zetten. Voorbeeld compbord = bordmaker(10, 1). Hierin is 10 het aantalboxen die het bord horizontaal en verticaal krijgt en 1 staat voor singleplayer = 1/multiplayer = 2.

- visual_schip_plaatser functie is een functie die opgeroepen kan worden als een onrelease is getriggerd. De functie print voor nu de x en y coordinaten uit en doet een bord check met bordchecker en plaatst het de return variabelen in 4 variabelen. Deze variabelen worden in de schip_plaatser gezet zodat het schip geplaatst kan worden. Vervolgens print het programma het bord uit zodat je kunt checken of het schip in het bord geplaatst is.

- keuze_1 functie bevat zoals eerder genoemd vanaf nu compbord en bombord. Deze zijn eerst als globale variabelen opgeroepen zodat andere functies nog steeds hun werk ermee kunnen doen. Vervolgens worden deze gemaakt middels de bordmaker functie. Daarnaast staan de schip_plaatser oproepingen voor de 5 schepen in de singleplayer hier nu ook in. Deze zijn niet verandert.

- In de main functie staat nu ook al een knop voor de multiplayer. Deze brengt je naar de nog onafgemaakte multiplayer.

- NIEUWE FUNCTIE keuze_2 ofwel de multiplayer. Deze functie bevat al het bord (visueel en backend namelijk bord_player1) samen met een stopknop en een rood vakje wat één schip moet voorstellen met een ondrag(verslepen) en onrelease(visual_schip_plaatser).
