import mysql.connector as mc

class Database:
    # Initialisation de la connexion à la base de données
    def __init__(self):
        self.connection = mc.connect(
            host="172.26.64.191",
            port="4406",
            user="root",
            password="password"
        )
        self.cursor = self.connection.cursor(dictionary=True)
        
    # Creation de la database si elle n'existe pas
    def connectDb(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS binance")

    # Creation de la table si elle n'existe pas
    def createTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS `binance`.`price` (  `id` int NOT NULL AUTO_INCREMENT,  `time` datetime(3) NOT NULL,  `symbol` varchar(45) NOT NULL,  `open` float NOT NULL,  `close` float NOT NULL,  `low` float NOT NULL,  `high` float NOT NULL,  `total_trade` double NOT NULL,  PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=678 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;")

    # Ajout d'un price dans la base de données 
    def addPrice(self, data):
        sql = "INSERT INTO `binance`.`price` (`time`, `symbol`, `open`, `close`, `low`, `high`, `total_trade`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (data['E'], data['s'], data['o'], data['c'], data['l'], data['h'], data['n']))
        self.connection.commit()

    # Truncate des tables article et image
    def truncateTable(self):
        self.cursor.execute("TRUNCATE TABLE `binance`.`price`")

    # Fermeture de la connexion à la base de données
    def close(self):
        self.connection.close()