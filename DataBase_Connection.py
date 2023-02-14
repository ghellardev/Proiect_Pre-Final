import pymongo

# clientul local de mongodb
client = pymongo.MongoClient("mongodb://localhost:27017")
# baza de date tinta
database = client["Firma"]
# coletia din baza de date aka de unde luam datele
Date_Angajati = database["Angajati"]
