import mysql.connector
import datetime
from sqlalchemy import Column, VARCHAR , INTEGER, DATE, ForeignKey

class USUARIO():
    def __init__(self, username, password, database_name, host):
        self.host=host
        self.username=username
        self.password=password
        self.database_name=database_name
    
    def connect_to_db(self):
        config = {'user': self.username, 'passwd' : self.password, 'database': self.database_name, 'host': self.host}
        self.cnx = mysql.connector.connect(**config)

a = USUARIO(username='root', password='changeme', host='localhost', database_name='museo')
a.connect_to_db()