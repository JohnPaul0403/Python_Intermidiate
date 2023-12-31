#Conversion de minutos a horas
minutos_por_hora = 60
segundos_por_minuto = 60

def horas_a_minutos(minutos, segundos):
    #Funcion qeu convierte minutos a horas
    hrs = minutos//minutos_por_hora
    min = minutos%minutos_por_hora

    return hrs, min, segundos
