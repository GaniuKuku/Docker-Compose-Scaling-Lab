import os
from flask import Flask, jsonify
import psycopg2
from datetime import datetime
import socket

app = Flask(__name__)
hostname = socket.gethostname() 

@app.route("/")
def home():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("DB_PORT"),
    )
    
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()[0]
    cursor.close()
    conn.close()


    return f"""
    <h2>Docker Compose Demo</h2>

    <p><b>Container:</b> {hostname}</p>

    <p><b>Time:</b> {datetime.now()}</p>

    <p><b>Database Connected Successfully!</b></p>

    <p>{version}</p>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
