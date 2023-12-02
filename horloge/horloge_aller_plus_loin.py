import time


print("Réglage de l'horloge. Entrez d'abord l'heure, puis les minutes, et les secondes")
h=int(input ("Heure : "))
m=int(input ("Minutes : "))
s=int(input ("Secondes : "))
heure=(h, m, s)                     # tuple heure



print("Réglage de l'alarme. Entrez d'abord l'heure, puis les minutes, et les secondes")
h_alarm=int(input ("Alarme, entrez l'heure : "))
m_alarm=int(input ("Alarme, entrez les minutes : "))
s_alarm=int(input ("Alarme, entrez les secondes : "))
alarm=(h_alarm, m_alarm, s_alarm)     # tuple alarm



print("voulez-vous le mode AM-PM (entrez 12), ou le mode 24 h (entrez 24)")
mode=(input("12 ou 24 : "))            # Choix du mode 12/24 heures

while mode != '12' and mode != '24':
    print("Choix non valide. Veuillez entrer '12' ou '24'.")
    mode = input("Veuillez entrer '12' ou '24': ")

if mode == '12':
    print("Mode 12 heures sélectionné.")

elif mode == '24':
    print("Mode 24 heures sélectionné.")


 
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