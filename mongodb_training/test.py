import os
from pymongo import MongoClient

MONGODB_USER = "testdb"
MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD')
HOST = "ds035995.mongolab.com"
PORT = 35995

client = MongoClient(HOST, PORT)
client.testdb_mongolab.authenticate(
    MONGODB_USER, MONGODB_PASSWORD, mechanism='SCRAM-SHA-1')

db = client.testdb_mongolab
students = db.students

print(students.find_one())