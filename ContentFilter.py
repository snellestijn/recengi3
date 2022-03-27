"""
Content Filtering: Reccomendation op basis van vergelijkbare producten in de database.
"""
#database module importeren
import psycopg2
import random

def content():
    #verbinding maken met de database
    con = psycopg2.connect( 
        host = 'localhost',
        database = 'RecEngine',
        user = 'postgres',
        password= 'snellestijn')
    cur = con.cursor()
    print("Database verbonden")

    #lijst met alle producten vragen
    cur.execute("select * from products")
    #producten opslaan in variabele
    alles = cur.fetchall()

    #vraag naar product id
    productid = input("wat is het ID van het gekocht product?: ")
    #sla het product op in variabele
    cur.execute(f"select * from products where id = \'{productid}\'")
    product= cur.fetchall()
    #print de naam van het product uit dat gekocht is
    product = product[0]
    print(f"U HEEFT GEKOCHT:\n{product[1]}\n")


    #vergelijkbare items zoeken
    #het bepalen of een artikel aanbevolen kan worden wordt
    #bepaald om een paar kretiria
    aanbevelingen = []
    for artikel in alles:
                #de subcategoie en de doelgroep moet hetzelfde zijn
                if artikel[5] == product[5] and artikel[7] == product[7]: 
                    #de tweede subcategory mag niet hetzelfde zijn
                    if artikel[6] != product[6]:
                            #als het artikel voldoet aan de Rules, dan wordt het toegevoegd aan de lijt
                            #met potentiele aanbevelingen in een lijst opslaan
                            aanbevelingen.append(artikel)


    aanbevolen = []
    #loop 4 keer (tot er 4 aanbevelingen zijn gemaakt)
    while len(aanbevolen) <4:
        #voeg een willekeurig item uit de lijst van potentiele aanbevelingen toe
        #aan de 4 echte aanbevelingen
        aanbevolen.append(random.choice(aanbevelingen))

    #print uit wat de aanbevelingen zijn
    print("OOK AAN TE RADEN:")
    for i in aanbevolen:
        print(i[1])
        print()

    #sluit de cursur en connectie weer af
    cur.close()
    con.close()