def kruskal(grafo):
    #Asigna el grafo como un arreglo de ciclos(diccionario)
    assert type(grafo)==dict
    #Nodos como llaves de el arreglo aqui se asigna graph_dict
    nodos = grafo.keys()   
    #asigna arreglo solo con valores set(unicos)
    visitados = set()
    #camino que toma (guardar aristas)
    camino = []
    #siguente inicializado como vacio
    next = None
    
    costo_minimo = 0

    #mientras los nodos visitados sea menor a los nodos en el grafo
    while len(visitados) < len(nodos):
        distancia = float('inf')
        # por cada nodo 
        for s in nodos:
            #por cada arista
            for d in nodos:
                if s in visitados and d in visitados or s == d:
                    continue
                if grafo[s][d] < distancia:
                    distancia = grafo[s][d]
                    costo_minimo += distancia
                    pre = s
                    next = d

        camino.append((pre, next))
        visitados.add(pre)
        visitados.add(next)

    return { "kruskal": {"camino": camino,"visitados": visitados,"costo_minimo": costo_minimo } }

#asegurarme que la funcion de grafo ya no siga corriendo
if __name__ == '__main__':
    graph_dict = {  "s1":{"s1": 0, "s2": 6, "s3": 3, "s4": 4, "s5":3},
                    "s2":{"s1": 1, "s2": 0, "s3": 4, "s4": 3, "s5":4},
                    "s3":{"s1": 2, "s2": 6, "s3": 0, "s4":3, "s5":4},
                    "s4":{"s1": 1, "s2": 5, "s3": 2, "s4":0,"s5":2},
                    "s5":{"s1": 3, "s2": 5, "s3": 7, "s4":4,"s5":0},
    }

    camino = kruskal(graph_dict)
    print (camino)
    #costo minimo
    #conjunto de aristas