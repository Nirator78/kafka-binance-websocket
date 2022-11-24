# Fichier qui reçoit et enregistre les données dans le système de gestion de données
from Database import Database
from kafka import KafkaConsumer
import json
from datetime import datetime

# Initialisation de la connexion à la base de données
db = Database()
db.connectDb()
db.createTable()

consumer = KafkaConsumer('binance', bootstrap_servers='localhost:9092')
for message in consumer:
    print(message.value)

     # Read json 
    json_decoded = json.loads(message.value)
    print(json_decoded["E"])

    # Convert time to datetime
    json_decoded["E"] = datetime.fromtimestamp(json_decoded["E"]/1000)
    print(json_decoded["E"])

    # Insert into database
    db.addPrice(json_decoded)