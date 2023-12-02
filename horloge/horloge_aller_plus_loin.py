import time
heure=(23,59,57)
alarm=(13,00,10)
mode="12"
# mode="24" 
list_heure = list(heure)            # converti le tuple heure en liste
list_alarm = list(alarm)            # converti le tuple alarm en liste

def reveil():
    if list_alarm == list_heure:    # compare heure et alarme
        print("c'est l'heure")

def afficher_heure():
    while True:                     # boucle infinie

        reveil()                    # appel la fonction reveil
        
        if list_heure[0] >= 0 and  list_heure[0] <= 12:
            am_pm="AM - "           # de 0 h à 12 h = AM
        # elif list_heure[0] >= 11:
        elif list_heure[0] > 12:
            am_pm="PM - "           # + de 12 h = PM

        time.sleep(1)               # Attend 1 seconde
        list_heure[2] += 1          # Ajoute 1 seconde à l'heure

        if list_heure[2]==60:       # 60 secondes
            list_heure[2] = 0       # = 0 seconde
            list_heure[1] += 1      # + 1 minute

        if list_heure[1]==60:       # 60 minutes
            list_heure[1] = 0       # = 0 minute
            list_heure[0] += 1      # + 1 heure
        
        if list_heure[0] > 23:      # 24 heure
            list_heure[0] = 0       # = 0 heure


        if mode == "24":
            print(f"{list_heure[0]:02d}:{list_heure[1]:02d}:{list_heure[2]:02d}")

        elif mode == "12":          
            if am_pm == "PM - ":    # affiche AM ou PM
                print(f"{am_pm}{list_heure[0]-12:02d}:{list_heure[1]:02d}:{list_heure[2]:02d}")
            elif am_pm == "AM - ":  # affiche AM ou PM
                print(f"{am_pm}{list_heure[0]:02d}:{list_heure[1]:02d}:{list_heure[2]:02d}")

        
afficher_heure()