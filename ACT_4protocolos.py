with open("Paquetes_Redes/ethernet_arp_request.bin", "rb") as f:
    #variable que lee cada byte
    byte = f.read(1)
    #variable que suma los bytes leidos
    bytesRed = 0
    #arreglo donde planeo poner todo en forma hexadecimal
    res = {0: 2}
    while byte:
        #Do stuff with byte.
        res[bytesRed] = bin(int.from_bytes(byte, byteorder='big'))[2:].zfill(8)
        byte = f.read(1)
        #transforma byte a hexadecimal de dos digitos y lo guarda en el arreglito
        #res[bytesRed] = byte#' '.join(format(ord(i), 'b') for i in str(byte))
        #suma de bytes leidos
        bytesRed += 1
    print("Direccion Mac destino:")
    for i in res:
        if res[i] != '':
            if i == 0:
                print("Tipo de hardware:",int(res[i],2)+int(res[i+1],2))
            if i == 2:
                print("Tipo de protocolo:",hex(int(res[i],2)+int(res[i+1],2)))
            if i == 4:
                print("Longitud Direccion hardware:")
                print(int(res[i],2))
            if i == 5:
                print("Longitud Direccion protocolo:")
                print(int(res[i],2))
            if i == 6:
                print("Código operación:",int(res[i],2)+int(res[i+1],2))
            if i in range(8,12):
                if i == 8:
                    print("Dirección Hardware origen:")
                print (hex(int(res[i]))[2:4],end = ':')
            if i == 12:
                origin = str(int(res[i],2)+int(res[i+1],2)+int(res[i+2],2)+int(res[i+3],2))
                origin = '.'.join(origin[i:i+1] for i in range(0, len(origin), 1))
                print("\nDireccion IP origen:",origin+'.0.0')
            if i in range(16,20):
                if i == 16:
                    print("Dirección Hardware Receptor:")
                print (hex(int(res[i]))[2:4],end = ':')
            if i == 20:
                destination = str(int(res[i],2)+int(res[i+1],2)+int(res[i+2],2)+int(res[i+3],2))
                destination = '.'.join(destination[i:i+1] for i in range(0, len(destination), 1))
                print("\nDireccion IP Receptor:",destination+'.0.0')
                
    #print('\n')        
    #print("{:02x}".format(int(res[i])))
    #rep = ' '.join(format(ord(i), 'b') for i in str(res[0]))
    #print(rep)
    #print (int.from_bytes(res[0], byteorder='big'))
    #print(res)
    #print (bytesRed)  