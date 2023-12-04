
import time
import threading

print("\nRéglage de l'horloge.\nEntrez d'abord l'heure, puis les minutes, et les secondes")
h=int(input ("\nHeure : "))             #input heure
m=int(input ("Minutes : "))
s=int(input ("Secondes : "))
heure=(h, m, s)                         # tuple heure
                                        #input alarm
print("\nRéglage de l'alarme.\nEntrez d'abord l'heure, puis les minutes, et les secondes")
h_alarm=int(input ("\nAlarme, entrez l'heure : "))
m_alarm=int(input ("Alarme, entrez les minutes : "))
s_alarm=int(input ("Alarme, entrez les secondes : "))
alarm=(h_alarm, m_alarm, s_alarm)       # tuple alarm

print("\nvoulez-vous le mode AM-PM (entrez 12), ou le mode 24 h (entrez 24)\n")
mode=(input("12 ou 24 : "))            # Choix du mode 12/24 heures

while mode != '12' and mode != '24':
    print("Choix non valide. Veuillez entrer les chiffres '12' ou '24'.")
    mode = input("12 ou 24 : ")

if mode == '12':
    print("Mode 12 heures sélectionné.")

elif mode == '24':
    print("Mode 24 heures sélectionné.")


pauseHorloge = True                                 # pause activée par défaut
exitHorloge = False                                 # programme activé par défaut    

list_heure = list(heure)                            # converti le tuple heure en liste
list_alarm = list(alarm)                            # converti le tuple alarm en liste

def reveil():
    if list_alarm == list_heure:                    # compare heure et alarme
        print("c'est l'heure")

def afficher_heure():
    global am_pm, pauseHorloge, exitHorloge         # récupère la variable définie en dehors de la fonction
    while not exitHorloge:               # Tant que le programme est activé
        if not pauseHorloge:           # Tant que pause est
            reveil()                        # appel la fonction reveil

            if list_heure[0] >= 0 and  list_heure[0] <= 12:
                am_pm="AM - "               # de 0 h à 12 h = AM

            elif list_heure[0] > 12:
                am_pm="PM - "               # + de 12 h = PM

            time.sleep(1)                 
            # Attend 1 seconde
            list_heure[2] += 1              # Ajoute 1 seconde

            if list_heure[2]==60:           # 60 secondes = 1 minute
                list_heure[2] = 0           # 0 seconde
                list_heure[1] += 1          # 1 minute

            if list_heure[1]==60:           # 60 minutes = 1 heure
                list_heure[1] = 0           # 0 minute
                list_heure[0] += 1          # 1 heure
            
            if list_heure[0] > 23:          # 24 heure
                list_heure[0] = 0           # = 0 heure

            if mode == '24':                # affiche l'heure en mode 24 h
                print(f"{list_heure[0]:02d}:{list_heure[1]:02d}:{list_heure[2]:02d}")

            elif mode == '12':              # affiche l'heure en mode 24 h : 2 possibilitées
                if list_heure[0]>12:
                    if am_pm == "PM - ":    # enlève 12 heures et affiche PM
                        print(f"{am_pm}{list_heure[0]-12:02d}:{list_heure[1]:02d}:{list_heure[2]:02d}")

                elif am_pm == "AM - ":      # affiche AM sans modifier l'heure
                    print(f"{am_pm}{list_heure[0]:02d}:{list_heure[1]:02d}:{list_heure[2]:02d}")

def offHorloge():                                      # fonction de mise en pause
    global pauseHorloge
    pauseHorloge = True
    print("\nHorloge en pause.\n")

def onHorloge():                                       # fonction de remise en marche
    global pauseHorloge
    pauseHorloge = False
    print("\nHorloge activée.\n")

def switchUser():                                   # fonction d'appel des fonctions marche, pause et arret
    global pauseHorloge, exitHorloge
    while not exitHorloge:
        user=input("\nAppuyez sur 'd' et 'entrée' pour démarrer l'horloge,\nAppuyez sur 'p' et 'entrée' pour la mettre en pause,\nAppuyez sur 'q' et 'entrée' pour quitter le programme : \n\n")
        if user == 'p':
            offHorloge()
        elif user == 'd':
            onHorloge()
        elif user == 'q':
            exitHorloge = True 


# Création d'un thread pour l'horloge
thread_horloge = threading.Thread(target=afficher_heure)

# Création d'un thread pour l'entrée utilisateur
thread_switch = threading.Thread(target=switchUser)

# Démarrage des threads
thread_switch.start()
thread_horloge.start()


# Attente que le thread de l'horloge se termine
thread_horloge.join()