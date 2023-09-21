def temperaturer(heltall_liste): 
    sommerdager= 0 
    høysommerdager= 0
    tropedager= 0
    for n in heltall_liste: 
        if 25 >= n > 20: 
            sommerdager += 1
        elif 30 >= n > 25:
            høysommerdager += 1 
        elif n > 30:
            tropedager += 1
    return sommerdager, høysommerdager, tropedager


result1, result2, result3 = temperaturer ( [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
21, 26, 21, 31, 15, 4, 1, -2] ) 

print(f" Det var {result1} sommerdager, {result2} høysommerdager, {result3} tropedager") 

