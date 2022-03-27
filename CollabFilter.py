
"""
Collaborative Filtering: Reccomendation op basis van welke producten andere nog meer bekeken
"""

#database module importeren
import psycopg2
import random

#verbinding maken met de database
con = psycopg2.connect( 
    host = 'localhost',
    database = 'RecEngine',
    user = 'postgres',
    password= 'snellestijn')
cur = con.cursor()
print("Database verbonden")

#vraag input welk product is gekocht
productid = input("wat is het ID van het gekocht product?: ")
#sla het product op in variabele
cur.execute(f"select * from products where id = \'{productid}\'")
product= cur.fetchall()
#print de naam van het product uit dat gekocht is
product = product[0]
print(f"U HEEFT GEKOCHT:\n{product[1]}\n")

#bekijk wie het product nogmeer heeft bekeken
cur.execute(f"select * from profiles_previously_viewed where prodid = \'{product[0]}\'")
kijkers = cur.fetchall()


#sla elke andere bekeken product op van de kijkers
producten = dict()
for kijker in kijkers:
    cur.execute(f"select * from profiles_previously_viewed where profid = \'{kijker[0]}\' and prodid <> \'{kijker[1]}\'")
    prods = cur.fetchall()
    for i in prods:
        if i[1] not in producten:
            producten[i[1]] = 0
        producten[i[1]] += 1

aanbevelingen = []
while len(aanbevelingen) < 4:
    if not producten:
        break
    hoogste = max(producten,key=producten.get)
    aanbevelingen.append(hoogste)
    producten.pop(hoogste)

print(aanbevelingen)