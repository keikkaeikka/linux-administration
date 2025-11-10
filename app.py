from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    # Yhdistetään MySQL/MariaDB-tietokantaan
    conn = mysql.connector.connect(
        host="localhost",
        user="eikka",                # <-- Vaihda omaksi käyttäjäksesi
        password="keikkaeikka25",  # <-- Vaihda omaksi salasanaksi
        database="exampledb"               # <-- Vaihda omaksi tietokannaksesi
    )

    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from MySQL!'")
    result = cursor.fetchone()

    # Suljetaan yhteydet
    cursor.close()
    conn.close()

    return f"<h1>{result[0]}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

