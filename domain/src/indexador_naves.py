def indexador_naves():
    numero = 0
    def siguiente_nave():
        nonlocal numero
        numero += 1
        return "nave" + str(numero) + ".md"
    return siguiente_nave
siguiente = (indexador_naves())