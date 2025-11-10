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
    cursor.execute("SELECT 'Hello from MySQL!',NOW();")
    result = cursor.fetchone()

    # Suljetaan yhteydet
    cursor.close()
    conn.close()

    message = result[0]
    sql_time = result[1]

    return f"""<!DOCTYPE html>
        <html>
            <head>
                <title>Aika</title>
                <style>
                    body {{ font-family: Arial; background-color: #f0f8ff; text-align: center; }}
                    h1 {{ color: #2e8b57; }}
                    p {{ font-size: 18px; }}
                </style>
                </head>
                <body>
                    <h1>{message}</h1>
                    <p>🕒 SQL Server Time: {sql_time}</p>
                    <p>Kellonaika vaihtuu sivua päivittämällä!</p>
                </body>
        </html>"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
