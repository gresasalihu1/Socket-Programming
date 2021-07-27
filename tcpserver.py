from socket import *
import random
from datetime import datetime
from _thread import *

print("****************************** FIEK - TCP SERVER ******************************")

servername = 'localhost'
port = 13000
server = socket(AF_INET, SOCK_STREAM)

try:
    server.bind((servername, port))
except:
    print("Nuk arritem te krijojm lidhjen!!")
print("Serveri eshte startuar ne localhost ne portin: " + str(port))
server.listen(10)

print("Serveri eshte duke pritur per ndonje kerkese:")


try:
    def gcf(a, b):
        if (a == 0):
            return b
        if (b == 0):
            return a
        if (a == b):
            return a
        if (a > b):
            return gcf(a - b, b)
        return gcf(a, b - a)

    def funksion(kerkesa, address):
        kerkesa = kerkesa.decode("UTF-8")
        kerkesa = kerkesa.upper()
        kerkesa = kerkesa.split(' ')
        pergjigja = " "
        if len(kerkesa) > 128:
            pergjigja = "Keni shenuar me shume se 128 karaktere"
        if kerkesa[0] == "IPADDRESS":
            pergjigja = "IP adresa eshte:" + address[0]
            if kerkesa[1:]:
                pergjigja="Shenoni vetem  IPADDRESS"



        elif kerkesa[0] == "PORT":
            pergjigja = "Porti eshte:" + str(address[1])
            if kerkesa[1:]:
                pergjigja = "Shenoni vetem  PORT"


        elif kerkesa[0] == "TIME":
            t = datetime.now().strftime('%Y-%m-%d %I:%M:%S:%p')
            pergjigja = "Koha tani eshte :"+str(t)
            if kerkesa[1:]:
                pergjigja = "Shenoni vetem TIME"

        elif kerkesa[0] == "GAME":
            numbers = []
            numbers = random.sample(range(1, 35), 5)
            numbers.sort()
            pergjigja = "5 Numra te sortuar ne intervalin 1-35:"+str(numbers)
            if kerkesa[1:]:
                pergjigja = "Shenoni vetem GAME"
        elif kerkesa[0] == "REVERSE":
            try:
              if kerkesa[1]:
                text = str.join(" ", kerkesa[1:])
                textreverse = text[::-1]
                textreverse=textreverse.lower()
                pergjigja = "Teksti pas metodes reverse:" + str(textreverse)
            except:
                pergjigja = "Duhet te shenosh REVERSE {hapesire} tekst"
        elif kerkesa[0] == "PALINDROME":
            try:
              if kerkesa[1]:
                text = str.join(" ", kerkesa[1:])
                textreverse = text[::-1]
                if (text == textreverse):
                    pergjigja = ("Teksti eshte palindrome")
                else:
                    pergjigja = ("Teksti nuk eshte palindrome")
            except:
                pergjigja = "Duhet te shenosh PALINDROME {hapesire} tekst"
        elif kerkesa[0] == "GCF":

         try:
            a = int(kerkesa[1])
            b = int(kerkesa[2])
            pergjigja = str(int(gcf(a,b)))
            if kerkesa[3:]:
                pergjigja = "Sheno vetem 2 numra pas komandes GCF"
         except:
             pergjigja = "Duhet te shenosh GCF {hapesire} numer {hapesire} numer"
        elif kerkesa[0] == "COUNT":
         try:
          if kerkesa[1]:

            bashtingellore = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
                           'V', 'X', 'W', 'Z']
            zanore = ['A', 'E', 'I', 'O', 'U', 'Y']
            z = 0
            b = 0
            for i in bashtingellore:
                for j in str(kerkesa[1:]):
                    if i == j:
                        b = b + 1
            for i in zanore:
                for j in str(kerkesa[1:]):
                    if i == j:
                        z = z + 1
            pergjigja = "Teksti: "+" ka "+str(z)+" zanore dhe "+str(b)+" bashktingellore"
         except:
             pergjigja = "Duhet te shenosh COUNT {hapesire} tekst"

        elif kerkesa[0] == "CONVERT":
            try:
                k = float(kerkesa[2])
                if kerkesa[1] == str('CMTOFEET'):
                    pergjigja = str(round(k * 0.032808, 2))
                elif kerkesa[1] == str('FEETTOCM'):
                    pergjigja = str(round(k / 0.032808, 2))
                elif kerkesa[1] == str('KMTOMILES'):
                    pergjigja = str(round(k * 0.62137, 2))
                elif kerkesa[1] == str('MILETOKM'):
                    pergjigja = str(round(k / 0.62137, 2))
                if kerkesa[3:]:
                    pergjigja = str("Duhet te shenoni vetem 3 argumente:CONVERT opcioni dhe numrin qe deshiron ta konvertosh")
            except:
                pergjigja = "Duhet te shenosh CONVERT {hapesire} opcioni {hapesire} numer"
        elif kerkesa[0] == "LEAPYEAR":
          try:
            year = int(kerkesa[1])
            if (year % 4 == 0) and (year % 100 != 0):
                pergjigja = str(year) + " eshte nje vit i brishte"
            else:
                pergjigja = str(year) + " nuk eshte nje vit i brishte"
            if kerkesa[2:]:
              pergjigja = "Sheno vetem 2 argumente:LEAPYEAR dhe vitin"
          except:
              pergjigja = "Duhet te shenosh LEAPYEAR {hapesire} numer"
        elif kerkesa[0] == "ENERGY":
         try:
            masa = float(kerkesa[1])
            shpejtsia = float(kerkesa[2])
            lartesia = float(kerkesa[3])
            energjiakinetike = str(round(0.5*masa*pow(shpejtsia,2),3))
            energjiapotenciale = str(round(9.81*masa*lartesia,3))
            pergjigja = "Energjia kinetike eshte = " + energjiakinetike+"\nEnergjia potenciale eshte = "+energjiapotenciale
            if kerkesa[4:]:
                pergjigja = "Shenoni vetem 4 argumentet:ENERGY,masa,shpejtesia,lartesia"
         except:
             pergjigja = "Duhet te shenosh ENERGY {hapesire} numer {hapesire} numer {hapesire} numer"
        elif kerkesa[0]=="SECONDS":
          try:
                  second=int(kerkesa[1])
                  minutes =str(int(second / 60))
                  remainingSeconds = str(int(second % 60))
                  pergjigja=kerkesa[1]+" sekonda eshte e barabarte me " +minutes+ " minuta dhe "+remainingSeconds+" sekonda"
                  if(kerkesa[2:]):
                      pergjigja="Sheno vetem SECONDS {hapesire} numer"
          except:
              pergjigja="Sheno SECONDS {hapesire} numer(sekonda)"



        else:
            pergjigja = "Shenoni njeren nga operacionet e dhena"

        return pergjigja



except:
    print("Smund ta realizojm kerkesen.")
def thread(client, address):
    while True:
        try:
            kerkesa = client.recv(1024)
            try:
                s = funksion(kerkesa,address)
                s = s.encode("UTF-8")
                client.send(s)
            except:
                client.send(str.encode("Kerkesa nuk eshte valide"))
        except:
            client.send(str.encode("Te dhenat nuk jane derguar ne server"))
            client.close()


while True:
  try:
    client, address = server.accept()
    print('Klienti u lidh me %s ne portin %s' % address)
    start_new_thread(thread, (client, address,))
  except:
    print("Lidhja me klientin :" + str(address) + "u nderpre")
    client.close()
    break
