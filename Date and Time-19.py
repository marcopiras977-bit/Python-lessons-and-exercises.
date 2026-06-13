# Date and Time
# Il modulo datetime fornisce classi per manipolare date e orari.
# import datetime
# per creare un oggetto datetime, puoi usare la classe datetime.datetime e passare i valori per anno, mese, giorno, ora, minuto e secondo.


import datetime

# Creare un oggetto datetime
data_e_ora = datetime.datetime(2024, 6, 1, 12, 30, 45)
print(data_e_ora)  # 2024-06-01 12:30:45

# Per ottenere la data e l'ora attuali, puoi usare il metodo datetime.datetime.now()
data_e_ora_attuale = datetime.datetime.now()
print(data_e_ora_attuale)  # 2024-06-01 12:30:45.123456

# Per formattare una data e ora in una stringa, puoi usare il metodo strftime() e passare una stringa di formato.
data_e_ora_formattata = data_e_ora.strftime("%Y-%m-%d %H:%M:%S")
print(data_e_ora_formattata)  # 2024-06-01 12:30:45 

# Per creare un oggetto datetime a partire da una stringa, puoi usare il metodo datetime.datetime.strptime() e passare la stringa e la stringa di formato.
data_e_ora_da_stringa = datetime.datetime.strptime("2024-06-01 12:30:45", "%Y-%m-%d %H:%M:%S")
print(data_e_ora_da_stringa)  # 2024-06-01 12:30:45
