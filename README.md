# recengi3
De laatste FA van structured programming: ReccomendationEngine

Runnen:
kies in de file 'RUNME.py' een van de twee filter manieren en run het programma. Er wordt gevraagd naar input, dit moet een product id zijn (van het door jou gekochte artikel)

Screenshots:
In de map screenshots staan enkele screenshots om uitkomsten te laten zien. Reden hiervoor is te lezen onder het stukje Database op regel 17.

Content filtering:
Het eerste algoritme gaat over het aanbevelen van producten op basis van content filtering. Hier wordt het gekozen artikel vergeleken met alle andere artikelen die dezelfde subcategorie hebben en dezelfde doelgroep. Maar de tweede subcategorie mag niet hetzelfde zijn. Dit is om te voorkomen dat je na het kopen van een product gelijk 4 keer hetzelfde soort product te zien krijgt.
Na het zoeken van alle vergelijkbare producten, kiest het programma hier 4 willekeurig producten uit om aan te bieden als aanbevolen. Dit is willekeurig om te zorgen dat elk artikel een keer aan bod kan komen.

Collaborative Filtering:
Het programma begint alle kijkers van het gekozen product binnen te halen. Vervolgens maak het programma een dictionary aan waarna het alle bekeken items van alle kijkers gaat toevoegen aan de dictionary, als het item al in de dictionary staat, dan wordt de waarde verhoogd met 1. Dit stuk kost het programma heel veel tijd om te runnen. Als alles in de dictionary staat dan worden de 4 meest bekeken items geselecteerd om weer te geven.

Database:
Er is gebruik gemaakt van de backup database die erg lastig te installeren was (zelfs 2 docenten tegelijk nodig om het te regelen), vandaar dat er geen instructies voor de database aanwezig zijn. Wel is er een screenshotvoorbeeld van een stukje uit de database.