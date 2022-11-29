#Scrivere una funzione sum_list() che sommi tutti gli elementi di una lista


number_list=[1,2,3,2.2]

def sum_list(number_list):
    
    if len(number_list)==0:             #len serve per vedere la lunghezza di una lista
        return None                     #returnare il valore vuoto 
    
    else:                               #davanti else vanno i due punti
        risultato = sum(number_list) 
        return risultato 

f=sum_list(number_list)

print("Risultato:{}" .format(f)) 
