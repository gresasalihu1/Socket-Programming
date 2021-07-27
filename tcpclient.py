from socket import *


print("****************************** FIEK - TCP CLIENT ******************************")
client = socket(AF_INET, SOCK_STREAM)
port=13000
hostserver='localhost'
k = input("Shtypni PO nese deshiron ta ndryshoni portin dhe ipaddressen  nese jo shtypni ndonje karakter tjeter apo enter: ")
k = k.upper()
def ndrysho():
    try:
        p = input("Jepe portin(shtyp 1 per default-13000):")
        port = int(p)
        if p == '1':
            port = int(13000)
        hostserver = input("Jepe ipaddress(shtyp 1 per default-'localhost'):")
        if hostserver == '1':
            hostserver = 'localhost'

        client.connect((hostserver, port))
    except:
        print("Lidhja ka deshtuar!Provo perseri.")
        return ndrysho()
if(k=='PO'):
   ndrysho()
else:
   client.connect((hostserver, port))
print("Operacionet: IPADRESA, PORT,COUNT {Hapësire} tekst, REVERSE {Hapësire} tekst, PALINDROME {Hapësire} tekst")
print("TIME, GAME,  GCF {Hapësire} Numër1 {Hapësire} Numër2 ")
print("CONVERT {Hapësire} Opcioni {Hapësire} Numër (***Opcionet:FeetToCm,CmToFeet,MileToKm,KmToMiles***)")
print("LEAPYEAR {Hapësire} Numër,ENERGY {Hapësire} Numër(m) Numër(v) Numër(h),SECONDS Numër(s) ")
print("Nese doni ta mbyllni programin  shtypni 0")
print("")


while True:


    p = input("Shtypni njeren nga komandat:")
    p = p.upper()
    while p == "":
        print("Ju lutem zgjedhni njerin nga funksionet.")
        p = input("Shtypni njeren nga komandat:")
    p = p.strip()
    p = p.upper()
    if len(p) > 128:
        print("Gjatesia maksimale e kerkeses(tekstit) duhet te jete 128bytes")
        continue


    try:
        client.sendall(str.encode(p))
    except:
        print("Kerkesa nuk mund te dergohet")
    respond = client.recv(1024)
    print("Pergjigjja e kthyer nga serveri:  "+respond.decode('utf-8'))

client.close()
