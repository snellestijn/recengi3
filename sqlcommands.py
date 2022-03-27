"""
In deze file staan de python commands die gebruikt worden
om de SQL taken uit te voeren in de relationele database.
"""

import psycopg2

#verbinding maken met de database
con = psycopg2.connect( 
    host = 'localhost',
    database = 'RecEngine',
    user = 'postgres',
    password= 'snellestijn')
cur = con.cursor()
print("Database verbonden")

def selecteren(wat):
    cur.execute(f"select {wat} from products")
    return cur.fetchall()

print(selecteren("*"))










cur.close()
con.close()