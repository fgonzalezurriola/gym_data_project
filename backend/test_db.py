# Test db connection
from app.database import engine
try:
    connection = engine.connect()
    print("DB CONECTADA")
    connection.close()
except Exception as e:
    print(f"Error: {e}")