from flask import Flask,render_template, request,redirect,url_for
import sqlite3
import socket
import time
import AlphaBot
import secrets
import hashlib

app = Flask(__name__)
bot = AlphaBot.AlphaBot()
comandi = {"w":bot.forward,"d":bot.left,"a": bot.right,"s":bot.backward,"q":bot.stop}
page = "/" + secrets.token_hex(16)
#print(page)
def hash(password):
    return hashlib.md5(password.encode()).hexdigest()

def validate(user,password):
    controllo = False
    con = sqlite3.connect('movimenti.db')
    cur = con.cursor()
    print(user)
    cur.execute(f"SELECT * FROM utenti WHERE user = '{user}'")
    rows = cur.fetchall()
    print(rows)
    print(hashlib.md5(password.encode()).hexdigest())
    for row in rows:
        dbUser = row[0]
        dbPass = row[1]
        if dbUser == user:
            if dbPass == hash(password):
                controllo = True
    con.close()
    return controllo

@app.route("/", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        if validate(username,password):
           return redirect(url_for("index"))
        else: 
            error = "Credenziali Errate"
    return render_template('login.html', error=error)
   
@app.route(page, methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        if request.form.get('Avanti') == 'Avanti':
            print("Avanti")
            bot.forward()
        elif  request.form.get('Indietro') == 'Indietro':
            bot.backward()
        elif  request.form.get('Destra') == 'Destra':
            bot.right()
        elif  request.form.get('Sinistra') == 'Sinistra':
            bot.left()
        elif  request.form.get('Stop') == 'Stop':
            bot.stop()
        else:
            print("Unknown")

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')