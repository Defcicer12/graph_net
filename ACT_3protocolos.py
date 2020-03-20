with open("Paquetes_Redes/ethernet_ipv4_icmp.bin", "rb") as f:
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
    # print("Direccion Mac destino:")
    for i in res:
        if res[i] != '':
            if i == 0:
                print("Version:")
                print(res[i][:4])
                print("Tamaño cabecera:")
                print(int(res[i][4:],2))
            if i == 1:
                print("Tipo de servicio:")
                print("Prioridad->")
                priority = res[i][:3]
                if priority == '000':
                    print("De rutina:",end=" ")
                if priority == '001':
                    print("Prioritario:",end=" ")
                if priority == '010':
                    print("Inmediato:",end=" ")
                if priority == '011':
                    print("Relampago:",end=" ")
                if priority == '100':
                    print("Invalidación Relámpago:",end=" ")
                if priority == '101':
                    print("Procesando llamada crítica y de emergencia:",end=" ")
                if priority == '110':
                    print("Control de trabajo de internet:",end=" ")
                if priority == '111':
                    print("Control de red:",end=" ")
                print(priority)
                print("Retardo: ",end = res[i][3]+"\n")
                print("Rendimiento: ",end = res[i][4]+"\n")
                print("Fiabilidad: ",end = res[i][5]+"\n")
                print("Retardo: ",end = res[i][6]+"\n")
                print("Retardo: ",end = res[i][7]+"\n")
            if i == 2:
                print("Longitud Total:")
                print(int(res[i],2)+int(res[i+1],2))
            if i == 4:
                print("Identificador:")
                print(int(res[i],2)+int(res[i+1],2))
            if i == 6:
                print("Banderas:")
                print("Reservado: "+res[i][0])
                print("Divisible: "+res[i][1])
                print("Fragmento: "+res[i][2])
                print("Posición de fragmento:",(int(res[i][3:],2)+int(res[i+1],2)))
            if i == 8:
                print("Tiempo de vida:",int(res[i],2))
            if i == 9:
                print("Protocolo:",int(res[i],2))
            if i == 10:
                print("Checksum:",hex(int(res[i],2)+int(res[i+1],2)))
            if i == 12:
                origin = str(int(res[i],2)+int(res[i+1],2)+int(res[i+2],2)+int(res[i+3],2))
                origin = '.'.join(origin[i:i+1] for i in range(0, len(origin), 1))
                print("Direccion IP origen:",origin+'.0.0')
            if i == 16:
                destination = str(int(res[i],2)+int(res[i+1],2)+int(res[i+2],2)+int(res[i+3],2))
                destination = '.'.join(destination[i:i+1] for i in range(0, len(destination), 1))
                print("Direccion IP destino:",destination+'.0')
            if i == 20:
                print("Tipo:",int(res[i],2))
            if i == 21:
                print("Codigo:",int(res[i],2))
            if i == 22:
                print("Checksum de ICMP:",hex(int(res[i],2)+int(res[i+1],2)))
            if i == 24:
                print("Datos (en hexadecimal):")
            if i >= 24:
                print(hex(int(res[i],2)),end="-")
            
                
    #print('\n')        
    #print("{:02x}".format(int(res[i])))
    #rep = ' '.join(format(ord(i), 'b') for i in str(res[0]))
    #print(rep)
    #print (int.from_bytes(res[0], byteorder='big'))
    #print(res)
    #print (bytesRed)
    
       