"""
Ejercicio 15 - Entrenadores Pokémon (TDA lista de lista)

Lista principal: entrenadores (ordenada por nombre).
Cada entrenador tiene una sublista con sus Pokémons (ordenada por nombre).
Se usa el TDA lista con la función criterio, como en el capítulo VIII.
"""


# ----------------------------------------------------------------------------
# TDA LISTA (simplemente enlazada)
# ----------------------------------------------------------------------------
class nodoLista:
    """Nodo de la lista: información y puntero al siguiente."""

    info, sig = None, None


class Lista:
    """TDA lista: puntero al inicio y cantidad de elementos."""

    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def criterio(dato, campo=None):
    """Devuelve el campo del registro por el cual se compara."""
    dic = dato.__dict__ if hasattr(dato, "__dict__") else {}
    if campo in dic:
        return dic[campo]
    return dato


def insertar(lista, dato, campo=None):
    """Inserta el dato en la lista de manera ordenada."""
    nodo = nodoLista()
    nodo.info = dato
    if lista.inicio is None or criterio(lista.inicio.info, campo) > criterio(dato, campo):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while act is not None and criterio(act.info, campo) < criterio(dato, campo):
            ant = ant.sig
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamanio += 1


def lista_vacia(lista):
    """Devuelve True si la lista está vacía."""
    return lista.inicio is None


def eliminar(lista, clave, campo=None):
    """Elimina un elemento de la lista y lo devuelve si lo encuentra."""
    dato = None
    if lista.inicio is not None and criterio(lista.inicio.info, campo) == criterio(clave, campo):
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamanio -= 1
    elif lista.inicio is not None:
        anterior = lista.inicio
        actual = lista.inicio.sig
        while actual is not None and criterio(actual.info, campo) != criterio(clave, campo):
            anterior = anterior.sig
            actual = actual.sig
        if actual is not None:
            dato = actual.info
            anterior.sig = actual.sig
            lista.tamanio -= 1
    return dato


def buscar(lista, buscado, campo=None):
    """Devuelve la dirección del nodo buscado (o None si no está)."""
    aux = lista.inicio
    while aux is not None and criterio(aux.info, campo) != criterio(buscado, campo):
        aux = aux.sig
    return aux


def tamanio(lista):
    """Devuelve la cantidad de elementos de la lista."""
    return lista.tamanio


def barrido(lista):
    """Muestra el contenido de la lista."""
    aux = lista.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig


# ----------------------------------------------------------------------------
# REGISTROS
# ----------------------------------------------------------------------------
class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return (f"Pokémon: {self.nombre} | Nivel: {self.nivel} | "
                f"Tipo: {self.tipo} | Subtipo: {self.subtipo}")


class Entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons = Lista()  # sublista de Pokémons

    def __str__(self):
        return (f"Entrenador: {self.nombre} | Torneos ganados: {self.torneos_ganados} | "
                f"Batallas perdidas: {self.batallas_perdidas} | "
                f"Batallas ganadas: {self.batallas_ganadas}")


def cargar_datos(lista):
    """Carga datos de prueba."""
    datos = [
        (("Ash", 5, 20, 80), [
            ("Pikachu", 60, "electrico", "ninguno"),
            ("Charizard", 70, "fuego", "volador"),
            ("Bulbasaur", 45, "planta", "veneno"),
            ("Wingull", 30, "agua", "volador"),
        ]),
        (("Misty", 2, 30, 70), [
            ("Starmie", 55, "agua", "psiquico"),
            ("Psyduck", 40, "agua", "ninguno"),
            ("Wingull", 35, "agua", "volador"),
            ("Psyduck", 42, "agua", "ninguno"),
        ]),
        (("Brock", 1, 40, 60), [
            ("Onix", 50, "roca", "tierra"),
            ("Geodude", 38, "roca", "tierra"),
            ("Tyrantrum", 62, "roca", "dragon"),
        ]),
        (("Gary", 7, 10, 90), [
            ("Blastoise", 68, "agua", "ninguno"),
            ("Arcanine", 66, "fuego", "ninguno"),
            ("Exeggutor", 58, "planta", "psiquico"),
            ("Pikachu", 52, "electrico", "ninguno"),
        ]),
        (("Cynthia", 4, 8, 92), [
            ("Garchomp", 78, "dragon", "tierra"),
            ("Spiritomb", 70, "fantasma", "siniestro"),
            ("Terrakion", 75, "roca", "lucha"),
        ]),
        (("Red", 9, 5, 95), [
            ("Pikachu", 81, "electrico", "ninguno"),
            ("Charmander", 77, "fuego", "planta"),
            ("Venusaur", 80, "planta", "veneno"),
            ("Lapras", 79, "agua", "hielo"),
        ]),
    ]
    for datos_entrenador, pokemons in datos:
        entrenador = Entrenador(*datos_entrenador)
        for datos_pokemon in pokemons:
            insertar(entrenador.pokemons, Pokemon(*datos_pokemon), "nombre")
        insertar(lista, entrenador, "nombre")


# ----------------------------------------------------------------------------
# ACTIVIDADES a) a k)
# ----------------------------------------------------------------------------
def cantidad_pokemons(lista, nombre_entrenador):
    """a. Cantidad de Pokémons de un entrenador."""
    pos = buscar(lista, nombre_entrenador, "nombre")
    if pos is not None:
        return tamanio(pos.info.pokemons)
    return None


def entrenadores_mas_de_tres_torneos(lista):
    """b. Lista los entrenadores que ganaron más de tres torneos."""
    aux = lista.inicio
    while aux is not None:
        if aux.info.torneos_ganados > 3:
            print(f"{aux.info.nombre} ({aux.info.torneos_ganados} torneos)")
        aux = aux.sig


def pokemon_mayor_nivel(entrenador):
    """Devuelve el Pokémon de mayor nivel de un entrenador (auxiliar)."""
    mayor = None
    aux = entrenador.pokemons.inicio
    while aux is not None:
        if mayor is None or aux.info.nivel > mayor.nivel:
            mayor = aux.info
        aux = aux.sig
    return mayor


def pokemon_mayor_nivel_del_mejor_entrenador(lista):
    """c. Pokémon de mayor nivel del entrenador con más torneos ganados."""
    mejor = None
    aux = lista.inicio
    while aux is not None:
        if mejor is None or aux.info.torneos_ganados > mejor.torneos_ganados:
            mejor = aux.info
        aux = aux.sig
    if mejor is None:
        return None, None
    return mejor, pokemon_mayor_nivel(mejor)


def mostrar_entrenador(lista, nombre_entrenador):
    """d. Muestra todos los datos de un entrenador y sus Pokémons."""
    pos = buscar(lista, nombre_entrenador, "nombre")
    if pos is not None:
        print(pos.info)
        barrido(pos.info.pokemons)
    else:
        print(f"El entrenador {nombre_entrenador} no está en la lista")


def porcentaje_ganadas(entrenador):
    """Porcentaje de batallas ganadas sobre el total disputado (auxiliar)."""
    total = entrenador.batallas_ganadas + entrenador.batallas_perdidas
    if total == 0:
        return 0
    return entrenador.batallas_ganadas * 100 / total


def entrenadores_porcentaje_mayor(lista, porcentaje=79):
    """e. Entrenadores cuyo porcentaje de batallas ganadas supera el indicado."""
    aux = lista.inicio
    while aux is not None:
        p = porcentaje_ganadas(aux.info)
        if p > porcentaje:
            print(f"{aux.info.nombre} ({p:.2f} % de batallas ganadas)")
        aux = aux.sig


def entrenadores_con_tipos(lista, combinaciones):
    """f. Entrenadores con Pokémons cuya combinación (tipo, subtipo) esté en 'combinaciones'."""
    aux = lista.inicio
    while aux is not None:
        encontrados = []
        pok = aux.info.pokemons.inicio
        while pok is not None:
            if (pok.info.tipo, pok.info.subtipo) in combinaciones:
                encontrados.append(f"{pok.info.nombre} ({pok.info.tipo}/{pok.info.subtipo})")
            pok = pok.sig
        if encontrados:
            print(f"{aux.info.nombre}: {', '.join(encontrados)}")
        aux = aux.sig


def promedio_nivel(lista, nombre_entrenador):
    """g. Promedio de nivel de los Pokémons de un entrenador."""
    pos = buscar(lista, nombre_entrenador, "nombre")
    if pos is None or lista_vacia(pos.info.pokemons):
        return None
    suma = 0
    pok = pos.info.pokemons.inicio
    while pok is not None:
        suma += pok.info.nivel
        pok = pok.sig
    return suma / tamanio(pos.info.pokemons)


def tiene_pokemon(entrenador, nombre_pokemon):
    """Devuelve el Pokémon si el entrenador lo tiene, sino None (auxiliar)."""
    pos = buscar(entrenador.pokemons, nombre_pokemon, "nombre")
    return pos.info if pos is not None else None


def cantidad_entrenadores_con_pokemon(lista, nombre_pokemon):
    """h. Cuántos entrenadores tienen un determinado Pokémon."""
    cant = 0
    aux = lista.inicio
    while aux is not None:
        if tiene_pokemon(aux.info, nombre_pokemon) is not None:
            cant += 1
        aux = aux.sig
    return cant


def entrenadores_con_repetidos(lista):
    """i. Entrenadores que tienen Pokémons repetidos (por nombre)."""
    aux = lista.inicio
    while aux is not None:
        repetidos = []
        pok = aux.info.pokemons.inicio
        # la sublista está ordenada por nombre: los repetidos quedan juntos
        while pok is not None and pok.sig is not None:
            if pok.info.nombre == pok.sig.info.nombre and pok.info.nombre not in repetidos:
                repetidos.append(pok.info.nombre)
            pok = pok.sig
        if repetidos:
            print(f"{aux.info.nombre}: {', '.join(repetidos)}")
        aux = aux.sig


def entrenadores_con_alguno(lista, nombres_pokemon):
    """j. Entrenadores que tengan alguno de los Pokémons indicados."""
    aux = lista.inicio
    while aux is not None:
        tiene = []
        for nombre in nombres_pokemon:
            if tiene_pokemon(aux.info, nombre) is not None:
                tiene.append(nombre)
        if tiene:
            print(f"{aux.info.nombre}: {', '.join(tiene)}")
        aux = aux.sig


def entrenador_tiene_pokemon(lista, nombre_entrenador, nombre_pokemon):
    """k. Determina si el entrenador X tiene al Pokémon Y y muestra los datos de ambos."""
    pos = buscar(lista, nombre_entrenador, "nombre")
    if pos is None:
        print(f"El entrenador {nombre_entrenador} no está en la lista")
        return
    pokemon = tiene_pokemon(pos.info, nombre_pokemon)
    if pokemon is None:
        print(f"{pos.info.nombre} no tiene a {nombre_pokemon}")
    else:
        print(f"{pos.info.nombre} tiene a {pokemon.nombre}")
        print(pos.info)
        print(pokemon)


# ----------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    entrenadores = Lista()
    cargar_datos(entrenadores)

    print("--- Entrenadores cargados ---")
    barrido(entrenadores)

    print("\na. Cantidad de Pokémons de Ash")
    print(cantidad_pokemons(entrenadores, "Ash"))

    print("\nb. Entrenadores con más de tres torneos ganados")
    entrenadores_mas_de_tres_torneos(entrenadores)

    print("\nc. Pokémon de mayor nivel del entrenador con más torneos ganados")
    mejor, pokemon = pokemon_mayor_nivel_del_mejor_entrenador(entrenadores)
    print(f"Entrenador: {mejor.nombre} ({mejor.torneos_ganados} torneos)")
    print(pokemon)

    print("\nd. Datos de un entrenador y sus Pokémons (Ash)")
    mostrar_entrenador(entrenadores, "Ash")

    print("\ne. Entrenadores con más de 79 % de batallas ganadas")
    entrenadores_porcentaje_mayor(entrenadores, 79)

    print("\nf. Entrenadores con Pokémons fuego/planta o agua/volador")
    entrenadores_con_tipos(entrenadores, [("fuego", "planta"), ("agua", "volador")])

    print("\ng. Promedio de nivel de los Pokémons de Gary")
    print(f"{promedio_nivel(entrenadores, 'Gary'):.2f}")

    print("\nh. Cantidad de entrenadores que tienen a Pikachu")
    print(cantidad_entrenadores_con_pokemon(entrenadores, "Pikachu"))

    print("\ni. Entrenadores con Pokémons repetidos")
    entrenadores_con_repetidos(entrenadores)

    print("\nj. Entrenadores con Tyrantrum, Terrakion o Wingull")
    entrenadores_con_alguno(entrenadores, ["Tyrantrum", "Terrakion", "Wingull"])

    print("\nk. ¿El entrenador X tiene al Pokémon Y?")
    entrenador_x = input("Nombre del entrenador: ")
    pokemon_y = input("Nombre del Pokémon: ")
    entrenador_tiene_pokemon(entrenadores, entrenador_x, pokemon_y)
