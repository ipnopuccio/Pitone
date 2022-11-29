#Inizializzo una Lista vuota per salvare i valori

#definsico la funzione

def sum_csv(file_name) :

    #memorizza i valori da sommare
    values = [] 

    # Apro e Leggo il file, Linea per Linea
    file = open(file_name,'r')  

    TF = True

    for line in file:

        # Faccio lo split di ogni riga sulla virgola
        #elements: una lista che contine 2 elementi (1 linea del file)
        elements = line.split(',') 
        
        # Se NON sto processando L'intestazione...
        #guardo se la casella 0 è diversa da date
        if elements[0] != 'Date':                                          
            
            value = elements[1]
            #facciamo diuventare un float la seconda colonna
            value = float(value) 
            #prendo il valore che sto considerato e lo inserisco in values[]
            values.append(value) 

            TF = False

    if TF == False:
        return sum(values)
    #Se il file è vuoto non returno nulla
    else: return None 

#definisco somma come dunzione che somma i valori nel file desiderato
somma=sum_csv("shampoo_sales.csv")
print("Risultato:{}" .format(somma))
