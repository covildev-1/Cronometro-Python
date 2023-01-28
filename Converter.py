from Counter import contador


def conversor(tempo):
    global horas
    global minutos
    global segundos

    if int(tempo[0]) > 0:
        horas = int(tempo[0])

        if int(tempo[1]) > 0:
            while int(tempo[1]) >= 60:
                horas += 1
                minutos = int(tempo[1]) - 60
                tempo[1] = int(tempo[1]) - 60
            else:
                minutos = int(tempo[1])
        elif int(tempo[2]) > 0:
            while int(tempo[2]) >= 60:
                minutos += 1
                segundos = int(tempo[2]) - 60
                tempo[2] = int(tempo[2]) - 60
            else:
                segundos = int(tempo[2])
    if int(tempo[1]) > 0:
        while int(tempo[1]) >= 60:
            horas += 1
            minutos = int(tempo[1]) - 60
            tempo[1] = int(tempo[1]) - 60
        else:
            minutos = int(tempo[1])

        if int(tempo[2]) > 0:
            while int(tempo[2]) >= 60:
                minutos += 1
                segundos = int(tempo[2]) - 60
                tempo[2] = int(tempo[2]) - 60
            else:
                segundos = int(tempo[2])
    if int(tempo[2]) > 0:
        while int(tempo[2]) >= 60:
            minutos += 1
            segundos = int(tempo[2]) - 60
            tempo[2] = int(tempo[2]) - 60

        else:
            segundos = int(tempo[2])
    else:
        horas = int(tempo[0])
        minutos = int(tempo[1])
        segundos = int(tempo[2])

    return contador([horas, minutos, segundos])


horas = 0
minutos = 0
segundos = 0
