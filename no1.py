
def handshake():
    n = int(input("Count Handshake : \n"))
    Jumlah = 0
    for i in range (1, n):
        Jumlah = Jumlah + i
    print("Result : \n" + str(Jumlah))

handshake()