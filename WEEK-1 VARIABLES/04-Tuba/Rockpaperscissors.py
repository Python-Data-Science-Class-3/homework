pieler1 : input("Benutzer:")
passwort :input("Benutzerpasswort:")
spieler2 : input("Gastbenutzer:")
passwort :input("Gastpasswort:")
print("DasSpiel Beginnt.....Wer GlückHat, Gewinnt!!")


optionen = ["stein", "papier", "schere"]

punkt_spieler1= 0
punkt_spieler2 = 0
spiel = 1
while (spiel<=10) :
    print("punktzahl", spiel)
    spiel+=1
    spieler1 =input("spieler1:")
    
    spieler2 = input("spieler2:")
    
    
    if((spieler1 =="stein" and spieler2 == "schere")  or (spieler1 == "schere" and spieler2 == "papier") or (spieler1== "papier" and spieler2 == "stein")):
     punkt_spieler1+=1
    elif(spieler1 == spieler2):
        print("nochmal bitte")
    else:
   
     punkt_spieler2+=1
     
    print("spieler1:", punkt_spieler1 ,"spieler2:", punkt_spieler2 )

    if(punkt_spieler1 != punkt_spieler2) and (punkt_spieler1 > punkt_spieler2):
        print("GEWINNEN: SPELER1")
    else:
        print("GEWINNEN: SPILER2")
     
