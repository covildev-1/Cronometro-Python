from Converter import conversor


def main():
    entrada = input(
        "Digite o tempo a ser cronometrado (Ex.: horas, minutos, segundos):\n")

    tempo = entrada.split(",")

    conversor(tempo)


main()
