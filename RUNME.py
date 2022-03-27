"""
In deze file zijn de verschillende soorten van de
reccomendation engine beschikbaar om te gebruiken
"""
import psycopg2
from CollabFilter import *
from ContentFilter import *

#True = Content Filtering
kies = True
#False = Collaborative Filtering



#hier wordt de gekoze methode afgespeeld
if kies:
    content()
else: collab()