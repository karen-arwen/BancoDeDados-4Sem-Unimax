import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",  # ajuste aqui
    "database": "ecommerce",
    "auth_plugin": "mysql_native_password",
    "port": 3306,
}

def conectar():
    return mysql.connector.connect(**DB_CONFIG)
