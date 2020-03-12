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
                try: 
                    if grafo[s][d] < distancia:
                        distancia = grafo[s][d]
                        costo_minimo += distancia
                        pre = s
                        next = d
                except KeyError:
                    continue

        camino.append((pre, next))
        visitados.add(pre)
        visitados.add(next)

    return { "kruskal": {"camino": camino,"visitados": visitados,"costo_minimo": costo_minimo } }

#asegurarme que la funcion de grafo ya no siga corriendo
if __name__ == '__main__':
    graph_dict = {  "s1":{"s1": 0, "s2": 1, "s4": 4},
                    "s2":{"s1": 1, "s2": 0, "s3": 2, "s4": 6, "s5":4},
                    "s3":{"s2": 2, "s3": 0, "s5":5, "s6":6},
                    "s4":{"s1": 4, "s2": 6, "s4":0,"s5":3, "s7":4},
                    "s5":{"s2": 4, "s3": 5, "s4":3,"s5":0, "s6":8, "s7":7},
                    "s6":{"s3": 6, "s7":3,"s5":8, "s6":0},
                    "s7":{"s6": 3, "s5": 7, "s4":4,"s7":0},
    }

    resp = kruskal(graph_dict)
    print (resp)
    #costo minimo
    #conjunto de aristas