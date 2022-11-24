# Fichier qui envoie les données au système de gestion de données
from websocket import create_connection
from kafka import KafkaProducer

# Connexion au websocket
ws = create_connection("wss://stream.binance.com:9443/ws/maticusdt@ticker")

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while(True):
    result =  ws.recv()
    print(result)
    producer.send('binance', result.encode('utf-8'))
    producer.flush()