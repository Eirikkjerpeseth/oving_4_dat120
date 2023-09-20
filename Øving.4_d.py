# Skriv en funksjon som tar inn ei liste med flyttall og en enkeltverdi. Funksjonen skal telle
# antall elementer i lista som er større enn eller lik den oppgitte verdien og returnere dett 


def liste(heltall_liste, x=1): 
    antall= 0 
    for n in heltall_liste: 
        if n >= x: 
            antall += 1 
    return antall
result = liste( [1,1,1,1,2] ) 
print(result) 

