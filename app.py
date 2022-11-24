from websocket import create_connection
import json
from datetime import datetime
from Database import Database

# Initialisation de la connexion à la base de données
db = Database()
db.connectDb()
db.createTable()

# Connexion au websocket
ws = create_connection("wss://stream.binance.com:9443/ws/maticusdt@ticker")

while True:
    result =  ws.recv()
    print(result)
    """
    "e": "1hTicker",    // Event type
    "E": 123456789,     // Event time
    "s": "BNBBTC",      // Symbol
    "p": "0.0015",      // Price change
    "P": "250.00",      // Price change percent
    "o": "0.0010",      // Open price
    "h": "0.0025",      // High price
    "l": "0.0010",      // Low price
    "c": "0.0025",      // Last price
    "w": "0.0018",      // Weighted average price
    "v": "10000",       // Total traded base asset volume
    "q": "18",          // Total traded quote asset volume
    "O": 0,             // Statistics open time
    "C": 86400000,      // Statistics close time
    "F": 0,             // First trade ID
    "L": 18150,         // Last trade Id
    "n": 18151          // Total number of trades
    """

    # Read json 
    json_decoded = json.loads(result)
    print(json_decoded["E"])

    # Convert time to datetime
    json_decoded["E"] = datetime.fromtimestamp(json_decoded["E"]/1000)
    print(json_decoded["E"])

    # Insert into database
    db.addPrice(json_decoded)