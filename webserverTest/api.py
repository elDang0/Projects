import fastapi
from fastapi import FastAPI
import mysql.connector
from fastapi.responses import HTMLResponse
import mysql.connector

FastAPI = FastAPI()
# Connect to the database

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
