def prim(graph, root):
    #Asigna el grafo como un arreglo de ciclos(diccionario)
    assert type(graph)==dict
    #Nodos como llaves de el arreglo aqui se asigna graph_dict
    nodes = list(graph)
    #quita el nodo inicial
    nodes.remove(root)
    #inicializa visitados con el nodo inicial
    visited = [root]
    #camino
    path = []
    #siguente inicializado como vacio
    next = None
    #costo_minimo
    costo_minimo = 0

    #mientras haya nodos
    while nodes:
        distance = float('inf') 
        # por cada nodo visitado
        for s in visited:
            #por cada nodo en el grafo
            for d in graph[s]:
                if d in visited or s == d:
                    continue
                try:
                    if graph[s][d] < distance:
                        distance = graph[s][d]
                        costo_minimo += distance
                        pre = s
                        next = d
                except KeyError:
                    continue
        path.append((pre, next))
        visited.append(next)
        nodes.remove(next)

    return { "prim": {"camino": path,"visitados": visited,"costo_minimo": costo_minimo } }

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

    path = prim(graph_dict, 's1')
    print (path)
