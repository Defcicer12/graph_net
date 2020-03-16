with open("Paquetes_Redes/ethernet_1.bin", "rb") as f:
    #variable que lee cada byte
    byte = f.read(1)
    #variable que suma los bytes leidos
    bytesRed = 0
    #arreglo donde planeo poner todo en forma hexadecimal
    res = {0: 2}
    while byte:
        #Do stuff with byte.
        byte = f.read(1)
        #transforma byte a hexadecimal de dos digitos y lo guarda en el arreglito
        res[bytesRed] = byte.hex()#''.join(format(ord(i), 'b') for i in byte)
        #suma de bytes leidos
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
    
       