import time
from datetime import datetime


# tuple heure
h=int(input ("Reglage de l'heure, entrez l'heure : "))
m=int(input ("Entrez les minutes : "))
s=int(input ("Entrez les secondes : "))
heure=(h, m, s)

# tuple alarm
h_alarm=int(input ("Reglage de l'alarme, entrez l'heure : "))
m_alarm=int(input ("Entrez les minutes : "))
s_alarm=int(input ("Entrez les secondes : "))
alarm=(h_alarm, m_alarm, s_alarm)


# FONCTION AFFICHER_HEURE --- début
# en paramètres le tuple heure et alarmset (voir ligne 38)
def afficher_heure(heure, alarmset):

    # le tuple heure est changé en liste
    list_heure = list(heure)

    # FONCTION ALARME --- début
    def alarm(alarm):
        # le tuple alarm est changé en liste
        list_alarm = list(alarm)
        # si les listes heure et alarm sont identique, c'est l'heure de l'alarme
        if list_alarm == list_heure:
            print("c'est l'heure")
    # FONCTION ALARME --- fin


    # boucle
    while True:
        # appel la foncion alarm avec alarmset en parametre (voir ligne 20)
        alarm(alarmset)
        #affiche l'heure
        print(f"{list_heure[0]:02d}:{list_heure[1]:02d}:{list_heure[2]:02d}")
        # Attend 1 seconde
        time.sleep(1)
        # Ajoute 1 seconde à l'heure
        list_heure[2] += 1
       
       # gère la conversion de 60 secondes en 1 minute
        if list_heure[2]==60:
            list_heure[2] = 0
            list_heure[1] += 1
            # gère la conversion de 60 minutes en 1 heure
            if list_heure[1]==60:
                list_heure[1] = 0
                list_heure[0] += 1
                # gère le passage de 24 à 0 heures
                if list_heure[0]==24:
                    list_heure[0] = 0


# FONCTION AFFICHER_HEURE --- fin


# appel la fonction AFFICHER_HEURE
afficher_heure(heure, alarm)


        
       

        




