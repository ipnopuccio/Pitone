
# Definisco la classe CSVFile
class CSVFile(): 

    #inizializzo attributo name
    def __init__(self, name):
        self.name = name

    #definisco la funzione get_data
    def get_data(self):
        try:
            file=open(self.name, 'r')
        except Exception as e :
            print('Errore! {} il file non esiste'.format(e))
            return None

        values = []
        dates = []
        final_list = []

        vuoto = True

        for line in file:
            elements = line.split(',')
            
            if elements[0]!='Date': 
                date = elements[0]
                value = elements[1]

                value=float(value)
                values.append(value)
                dates.append(date)

                final_list = [date, value]
                print(final_list)

                vuoto = False
            
        if vuoto == False:
            return final_list
        else:
            return None
    
my_file = CSVFile('shampoo_sales_error.csv')
#my_file.get_data()
print(my_file.get_data())