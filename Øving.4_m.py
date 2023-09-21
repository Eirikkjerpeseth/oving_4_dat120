
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



tall_liste = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]
resultat = sekvens_av_0(tall_liste)
print(f" Den lengste perioden uten nedbør var {resultat} dager")
