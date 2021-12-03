def limpiar_BBDD(base_de_datos):
    naves = []
    for nave in base_de_datos:
        nave.pop("_id")
        naves.append(nave)
    return naves