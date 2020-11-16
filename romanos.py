simbolos = {
"M":1000,
"D":500,
"C":100,
"L":50,
"X":10,
"V":5,
"I":1
}

tipo_5 = ("V", "D", "L")
tipo_1 = ("I", "X", "C", "M")

def simbolo_a_entero(simbolo):
    if isinstance (simbolo, str) and simbolo.upper() in simbolos:
        return simbolos[simbolo.upper()]
    elif isinstance(simbolo, str):
        raise ValueError(f"Simbolo {simbolo} no permitido")
    else:
        raise ValueError(f"Parámetro {simbolo} debe ser un string")


def romano_a_entero(romano):
    if not isinstance(romano, str):
        raise ValueError(f"Parámetro {romano} debe ser un string")
    
    suma = 0
    c_repes = 0
    valoranterior = ""

    for letra in romano:
        if letra == valoranterior and letra in tipo_5:
            raise OverflowError(f"Demasiado símbolos de tipo {letra}")
        if letra == valoranterior:
            c_repes += 1
            if c_repes > 2:
                raise OverflowError(f"Demasiado símbolos de tipo {letra}")
        elif valoranterior and simbolos[letra] > simbolos[valoranterior]: 
            suma -= simbolos[valoranterior] * 2
            c_repes = 0
        else:
            c_repes = 0
            
        suma += simbolo_a_entero(letra)
        valoranterior = letra
    return suma
