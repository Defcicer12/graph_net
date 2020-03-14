with open("Paquetes_Redes/ethernet_1.bin", "rb") as f:
    byte = f.read(1)
    bytesRed = 0
    res = {0: 2}
    while byte:
        #Do stuff with byte.
        byte = f.read(1)
        res[bytesRed] = byte.hex()#''.join(format(ord(i), 'b') for i in byte)
        bytesRed += 1
    print("Direccion Mac destino:")
    for i in res:
        if res[i] != '':
            if i in range(6):
                print (res[i],end = ':')
            if i in range(7,13):
                if i == 7:
                    print('\nDireccion origen:')
                print (res[i],end = ':')
            if i in range(15,17):
                if i == 15:
                    print('\nProtocolo:')
                print (res[i],end = '')
            if i in range(17,63):
                if i == 17:
                    print('\nResto de datos:')
                print (res[i],end = '-')
    print('\n')
                
    #print("{:02x}".format(int(res[i])))
    #print (res)
    #print (bytesRed)
    
       