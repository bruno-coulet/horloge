import time
#from datetime import datetime

heure=(12,59,57)
alarm=(12,59,59)
mode_horaire=12
am_pm = None

def reveil(alarm):
    list_alarm = list(alarm)          # converti le tuple alarm en liste
    list_heure = list(heure)          # converti le tuple heure en liste
    if list_alarm == list_heure:      # compare heure et alarme
        print("c'est l'heure")





def mode12_24():
    list_heure = list(heure)
    global am_pm
    for list_heure[0] in range (1,13):
        am_pm="AM-"
    for list_heure[0] in range (13,25):
        am_pm = "PM-"
        list_heure[0] -= 12
    if list_heure[0]==25:
        list_heure[0]=0

        

def afficher_heure(heure):
    
    list_heure = list(heure)        # converti le tuple en liste
    mode12_24()                 # appel la fonction mode12_24
    reveil(alarm)               # appel la fonction alarm

    while True:                     # boucle



        if mode_horaire==24:        #affiche l'heure suivant le mode 12 ou 24
            print(f"{am_pm}{list_heure[0]:02d}:{list_heure[1]:02d}:{list_heure[2]:02d}")
        if mode_horaire==12:
            print(f"{am_pm}{list_heure[0]:02d}:{list_heure[1]:02d}:{list_heure[2]:02d}")

        time.sleep(1)               # Attend 1 seconde
        list_heure[2] += 1          # Ajoute 1 seconde à l'heure

        if list_heure[2]==60:       # 60 secondes = 1 minute 0 seconde
            list_heure[2] = 0
            list_heure[1] += 1

    
        if list_heure[1]==60:       # 60 minutes = 1 heure 0 minute
            list_heure[1] = 0
            list_heure[0] += 1

        if list_heure[0]==24:
            list_heure[0] = 0

        mode12_24()                 # appel la fonction mode12_24
        reveil(alarm)               # appel la fonction alarm

afficher_heure(heure)
