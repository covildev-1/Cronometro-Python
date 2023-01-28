import time


def contador(tempo):
    if tempo[0] > 0:
        print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
        time.sleep(1)

        if tempo[1] == 0:
            tempo[0] -= 1
            tempo[1] = 59
            tempo[2] = 59

            print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
            time.sleep(1)

        if tempo[1] > 0:
            while tempo[1] > 0 and tempo[0] > 0:
                if tempo[2] == 0:
                    tempo[1] -= 1
                    tempo[2] = 59

                    print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
                    time.sleep(1)

                if tempo[2] > 0:
                    while tempo[2] > 0 and tempo[1] > 0:
                        tempo[2] -= 1

                        print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
                        time.sleep(1)

                        if tempo[2] == 0:
                            tempo[1] -= 1
                            tempo[2] = 59

                            print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
                            time.sleep(1)

                    while tempo[2] > 0:
                        tempo[2] -= 1

                        print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
                        time.sleep(1)

                if tempo[1] == 0:
                    if tempo[0] == 0:
                        tempo[1] = 59
                        tempo[2] = 59
                    else:
                        tempo[0] -= 1
                        tempo[1] = 59
                        tempo[2] = 59

                    print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
                    time.sleep(1)

            if tempo[1] > 0:
                if tempo[2] > 0:
                    while tempo[2] > 0 and tempo[1] > 0:
                        tempo[2] -= 1

                        print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
                        time.sleep(1)

                        if tempo[2] == 0:
                            tempo[1] -= 1
                            tempo[2] = 59

                            print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
                            time.sleep(1)

                    while tempo[2] > 0:
                        tempo[2] -= 1

                        print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
                        time.sleep(1)
    elif tempo[1] > 0:
        print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
        time.sleep(1)

        if tempo[2] == 0:
            tempo[1] -= 1
            tempo[2] = 59

            print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
            time.sleep(1)

        if tempo[2] > 0:
            while tempo[2] > 0 and tempo[1] > 0:
                tempo[2] -= 1

                print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
                time.sleep(1)

                if tempo[2] == 0:
                    tempo[1] -= 1
                    tempo[2] = 59

                    print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
                    time.sleep(1)

            while tempo[2] > 0:
                tempo[2] -= 1

                print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
                time.sleep(1)
    elif tempo[2] > 0:
        print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
        time.sleep(1)

        while tempo[2] > 0:
            tempo[2] -= 1

            print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
            time.sleep(1)
    else:
        print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
        time.sleep(1)
