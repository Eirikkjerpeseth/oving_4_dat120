# Skriv en funksjon som tar inn ei liste med flyttall og en enkeltverdi. Funksjonen skal telle
# antall elementer i lista som er større enn eller lik den oppgitte verdien og returnere dett 


def liste(liste, x): 
    antall= 0 
    for element in list: 
        if element >= x: 
            antall += 1 
    return antall


