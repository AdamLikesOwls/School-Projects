num = int(input(": "))

def bin():
    qut = num
    binary  = ""

    while qut != 0:

        rem = str(qut % 2)
        binary += rem

        qut = int(qut / 2)

    binary = binary[::-1]
    print(binary)


bin()

