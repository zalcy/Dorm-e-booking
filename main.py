import os
import base64
import time
from datetime import datetime

def startUp():
    global profileName
    with open("data/log.txt", "a", encoding = "utf-8") as log: # Logolás
        ido = datetime.now()
        log.write(f"[{ido.strftime('%Y-%m-%d %H:%M:%S')}] Indítás\n")
    os.system('cls')
    profileName = input("[Bejelentkezés] Felhasználónév > ")
    passwordInput = input("[Autentikáció] Adja meg a napló jelszavát > ")
    with open("data/profiles.txt", "r", encoding="utf-8") as f:
        password = f.read()
        if passwordInput == base64.b64decode(password).decode("utf-8"):
            os.system("cls")
            print("Sikeres bejelentkezés!\nFelhasználónév:",profileName)
            with open("data/log.txt", "a", encoding = "utf-8") as log: # Logolás
                ido = datetime.now()
                log.write(f"[{ido.strftime('%Y-%m-%d %H:%M:%S')}] {profileName} | Autentikáció | Sikeres bejelentkezés\n")
            time.sleep(1)
            os.system("cls")
        else:
            with open("data/log.txt", "a", encoding = "utf-8") as log: # Logolás
                ido = datetime.now()
                log.write(f"[{ido.strftime('%Y-%m-%d %H:%M:%S')}] {profileName} | Autentikáció | Sikertelen bejelentkezés\n")
            print("Hiba!")
            time.sleep(2)
            startUp()


def settings():
    global profileName
    with open("data/log.txt", "a", encoding = "utf-8") as log: # Logolás
        ido = datetime.now()
        log.write(f"[{ido.strftime('%Y-%m-%d %H:%M:%S')}] {profileName} | Beállítások | Beállítások megnyitása\n")
    print('''
     BEÁLLÍTÁSOK
    -------------
    [1] Téma választás
    ''')
    choice = input("[Választás] > ")

    while choice != "1" and choice != "":
        with open("data/log.txt", "a", encoding = "utf-8") as log: # Logolás
            ido = datetime.now()
            log.write(f"[{ido.strftime('%Y-%m-%d %H:%M:%S')}] {profileName} | Beállítások | Hibás bevitel: {choice}\n")
        print("[HIBA] Hibás bevitel! Válassz újból!")
        choice = input("[Választás] > ")

    if choice == "1":
        os.system("cls")
        with open("data/log.txt", "a", encoding = "utf-8") as log: # Logolás
            ido = datetime.now()
            log.write(f"[{ido.strftime('%Y-%m-%d %H:%M:%S')}] {profileName} | Téma választás | Téma választás megnyitása\n")

        print('''
         TÉMA VÁLASZTÁS
        ----------------
        [1] Világos téma
        [2] Sötét téma

        ''')

        choice = input("[Választás] > ")

        while choice != "1" and choice != "2" and choice != "":
            with open("data/log.txt", "a", encoding = "utf-8") as log: # Logolás
                ido = datetime.now()
                log.write(f"[{ido.strftime('%Y-%m-%d %H:%M:%S')}] {profileName} | Téma választás | Hibás bevitel: {choice}\n")

            print("[HIBA] Hibás bevitel! Válassz újból!")
            choice = input("[Választás] > ")

        if choice == "1":
            with open("data/log.txt", "a", encoding = "utf-8") as log: # Logolás
                ido = datetime.now()
                log.write(f"[{ido.strftime('%Y-%m-%d %H:%M:%S')}] {profileName} | Téma választás | Átváltás világos témába, bevitel: {choice}\n")
            os.system("color 70")
            os.system("cls")
            interface()
        if choice == "2":
            with open("data/log.txt", "a", encoding = "utf-8") as log: # Logolás
                ido = datetime.now()
                log.write(f"[{ido.strftime('%Y-%m-%d %H:%M:%S')}] {profileName} | Téma választás | Átváltás sötét témába, bevitel: {choice}\n")
            os.system("color 07")
            os.system("cls")
            interface()
        if choice == "":
            with open("data/log.txt", "a", encoding = "utf-8") as log: # Logolás
                ido = datetime.now()
                log.write(f"[{ido.strftime('%Y-%m-%d %H:%M:%S')}] {profileName} | Téma választás | Visszalépés, bevitel: {choice}\n")
            os.system("cls")
            interface()

    if choice == "":
        os.system("cls")
        interface()

def interface():
    global profileName
    with open("data/log.txt", "a", encoding = "utf-8") as log: # Logolás
        ido = datetime.now()
        log.write(f"[{ido.strftime('%Y-%m-%d %H:%M:%S')}] {profileName} | Interface | Interface megnyitása\n")
    print('''
           KOLLÉGIUM E-NAPLÓ KEZELŐFELÜLET:
    ----------------------------------------------
    [1] Megérkező emberek naplózása
    [2] Távozó emberek naplózása
    [3] Beállítások
    ''')

    choice = input("[Választás] > ")

    while choice != "1" and choice != "2" and choice != "3" and choice != "":
        with open("data/log.txt", "a", encoding = "utf-8") as log: # Logolás
            ido = datetime.now()
            log.write(f"[{ido.strftime('%Y-%m-%d %H:%M:%S')}] {profileName} | Interface | Hibás bevitel: {choice}\n")
        print("[HIBA] Hibás bevitel! Válassz újból!")
        choice = input("[Választás] > ")

    if choice == "1": # Megérkező emberek naplózása
        os.system('cls')
        print('''
         MEGÉRKEZŐ EMBEREK NAPLÓZÁSA:
        ------------------------------
        ''')

        print("\nVisszalépéshez nyomjon Enter-t!")

        megerkezoInput = None
        counter = 0

        megerkezoGyujtes = []
        while megerkezoInput != "":
            megerkezoInput = input("[Megérkező személy] > ")
            with open("data/bentlevo.txt", "a", encoding="utf-8") as f:
                if megerkezoInput == "" and counter == 0: # Visszalépés a megerkezo.txt-be baló beleírás nélkül
                    os.system("cls")
                    interface()
                if megerkezoInput == "":
                    print(f"\nSikeres naplózás! ({counter} fő)")
                    with open("data/log.txt", "a", encoding = "utf-8") as log:
                        log.write(f"[{ido.strftime('%Y-%m-%d %H:%M:%S')}] {profileName} | Megérkező naplózás | Sikeres naplózás: {megerkezoGyujtes}\n")
                    time.sleep(2)
                    os.system('cls')
                    interface()
                else:
                    megerkezoGyujtes.append(megerkezoInput)
                    f.write(megerkezoInput)
                    f.write("\n")
                    counter += 1

    if choice == "2":
        counter = 0
        os.system("cls")
        print('''
         TÁVOZÓ EMBEREK NAPLÓZÁSA:
        ---------------------------
        ''')

        print("\nVisszalépéshez nyomjon Enter-t!")

        tavozoInput = None
        counter = 0

        tavozoGyujtes = []

        while tavozoInput != "":
            tavozoInput = input("[Távozó személy] > ")
            
            tavozoGyujtes.append(tavozoInput)
            
            if tavozoInput == "" and counter == 0:
                os.system("cls")
                interface()
            if tavozoInput != "":
                with open("data/bentlevo.txt", "r", encoding="utf-8") as f_read:
                    lines = f_read.readlines()
                tisztaTavozo = []

                for i in lines:
                    tisztaTavozo.append(i.strip("\n"))

                modifikaltSorok = []

                for i in tisztaTavozo:
                    if i != tavozoInput:
                        modifikaltSorok.append(i + "\n")

                with open("data/bentlevo.txt", "w", encoding="utf-8") as f_write:
                    f_write.writelines(modifikaltSorok)
                counter += 1

            if tavozoInput == "":
                with open("data/log.txt", "a", encoding = "utf-8") as log:
                        log.write(f"[{ido.strftime('%Y-%m-%d %H:%M:%S')}] {profileName} | Távozó naplózás | Sikeres naplózás: {tavozoGyujtes}\n")
                print(f"\nSikeres naplózás! ({counter})")
                time.sleep(2)
                os.system("cls")
                interface()

    if choice == "3": # Beállítások
        os.system("cls")
        settings()

    if choice == "": # Visszalépés enterrel
        os.system("cls")
        interface()

startUp() # Kezdő felület indítás
interface()
