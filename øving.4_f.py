#Lag en funksjon som tar inn ei liste med tall. Funksjonen skal finne og returnere lengden til 
#den lengste sammenhengende sekvensen av 0-ere i lista.




def sekvens_av_0(liste):
    lengde=0
    gjeldende_lengde=0


    for tall in liste:
        if tall==0:
            gjeldende_lengde += 1
            lengde=max(lengde, gjeldende_lengde)
        else:
            gjeldende_lengde=0

    return lengde




tall_liste = [1, 0, 0, 2, 0, 3, 0, 0, 0, 0, 0, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 4, 7, 0, 0, 0]
resultat = sekvens_av_0(tall_liste)
print(resultat)
