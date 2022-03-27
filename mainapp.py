"""
Reccomendation op basis van vergelijkbare producten in de database.
"""
#database module importeren
import psycopg2


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
alles = cur.fetchall()

#er achter komen welk product is gekocht
productid = str(input("wat is het ID van het gekocht product?: "))
cur.execute(f"select * from products where id = \'{productid}\'")
product= cur.fetchall()
product = product[0]
print(product)



#vergelijkbare items zoeken

aanbevelingen = []
for artikel in alles:
    if artikel[1] != product[1]:
        if artikel[4] == product[4]:
            if artikel[5] == product[5]:
                if artikel[6] == product[6]:
                    if artikel[7] == product[7]:
                        aanbevelingen.append(artikel)



cur.close()
con.close()