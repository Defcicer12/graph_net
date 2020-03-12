with open("Paquetes_Redes/ethernet_1.bin", "rb") as f:
    byte = f.read(1)
    bytesRed = 0
    res = {1: 2}
    while byte:
        #Do stuff with byte.
        byte = f.read(1)
        res[bytesRed] = ''.join(format(ord(i), 'b') for i in byte)
        bytesRed += 1
    for i in res:
        print(i,res[i])
    #print (res)
    #print (bytesRed)
    
       