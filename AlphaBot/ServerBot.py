import socket
import time
import AlphaBot
import subprocess
import sqlite3
#Inizializzazione#
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
bot = AlphaBot.AlphaBot()
comandi = {"w":bot.forward,"d":bot.left,"a": bot.right,"s":bot.backward,"q":bot.stop}
connect = sqlite3.connect("movimenti.db")
cur = connect.cursor()

def presetMovimenti(id):
    s = "SELECT movimento FROM ALPHABOT WHERE id = {id}"
    res = cur.execute(f"SELECT movimento FROM ALPHABOT WHERE id = {id}" )
    serie = res.fetchall()
    print(serie)
    serie = serie[0][0]
    print(serie)

    listaComandi = serie.split(",")
    for command in listaComandi:
        msg = command.split("|")
        comandi[msg[0]]()
        timeStart = time.time()
        tempo = True
        while tempo:
            timeNow = time.time()
            timeNow = timeNow - timeStart
            if timeNow >= float(msg[1]):
                tempo = False
        comandi["q"]()
        time.sleep(0.5)


def main():

    s.bind(("0.0.0.0",5000))
    s.listen()
    print("Via")
    connection, address = s.accept()
    """volt = subprocess.run("vcgencmd", " measure_volts", capture_output=True)
    print(volt)"""
    while True:
        msg = connection.recv(4096)
        msg = msg.decode()
        msg = msg.split("|")
        print(msg)
        
        if msg[0] == "preset":
            presetMovimenti(msg[1])
        else:
            comandi[msg[0]]()
            timeStart = time.time()
            tempo = True
            while tempo:
                timeNow = time.time()
                timeNow = timeNow - timeStart
                if timeNow >= float(msg[1]):
                    tempo = False
            comandi["q"]()

    s.close()

if __name__ == '__main__':
    main()