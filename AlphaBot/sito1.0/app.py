from flask import Flask,render_template, request,redirect,url_for
import socket
import time
import AlphaBot

app = Flask(__name__)
bot = AlphaBot.AlphaBot()
comandi = {"w":bot.forward,"d":bot.left,"a": bot.right,"s":bot.backward,"q":bot.stop}
@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]

        if username == "ciao":
           return redirect(url_for("index"))
   
   
@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
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
    if request.method == 'GET':
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')