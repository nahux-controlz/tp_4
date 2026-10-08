"""
Ejercicio 6 - Lista de superhéroes de comics (TDA lista simplemente enlazada)

Dada una lista de superhéroes de los cuales se conoce: nombre, año de aparición,
casa de comic (Marvel o DC) y biografía, se resuelven las actividades a) a i).

La lista se ordena por nombre. Se usa el TDA lista con la función criterio, tal
como se presenta en el capítulo VIII (listas enlazadas).
"""

import re


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
# REGISTRO SUPERHÉROE
# ----------------------------------------------------------------------------
class Superheroe:
    def __init__(self, nombre, anio_aparicion, casa, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia

    def __str__(self):
        return (f"Nombre: {self.nombre} | Año de aparición: {self.anio_aparicion} | "
                f"Casa: {self.casa} | Biografía: {self.biografia}")


def cargar_superheroes(lista):
    """Carga datos de prueba (ordenados por nombre)."""
    datos = [
        ("Superman", 1938, "DC", "Último hijo de Krypton, vuela y tiene superfuerza. Usa un traje azul con capa roja."),
        ("Batman", 1939, "DC", "Bruce Wayne combate el crimen en Gotham con su traje de murciélago y su ingenio."),
        ("Linterna Verde", 1940, "DC", "Hal Jordan usa un anillo de poder que crea objetos con la voluntad."),
        ("Flash", 1940, "DC", "Barry Allen obtuvo supervelocidad tras un accidente en su laboratorio."),
        ("Mujer Maravilla", 1941, "DC", "Princesa amazona Diana de Temiscira, con lazo de la verdad y brazaletes."),
        ("Aquaman", 1941, "DC", "Rey de Atlantis, se comunica con la vida marina y tiene gran fuerza."),
        ("Capitán América", 1941, "Marvel", "Steve Rogers, soldado mejorado por el suero del supersoldado, usa un escudo."),
        ("Hulk", 1962, "Marvel", "El científico Bruce Banner se transforma en un gigante verde al enojarse."),
        ("Thor", 1962, "Marvel", "Dios nórdico del trueno que empuña el martillo Mjolnir."),
        ("Spiderman", 1962, "Marvel", "Peter Parker fue picado por una araña radiactiva; viste un traje rojo y azul."),
        ("Iron Man", 1963, "Marvel", "Tony Stark, empresario genio, creó una armadura tecnológica para combatir."),
        ("Dr. Strange", 1963, "DC", "Stephen Strange, ex cirujano, es el Hechicero Supremo y usa magia."),
        ("Daredevil", 1964, "Marvel", "Matt Murdock quedó ciego de niño y desarrolló sentidos extraordinarios."),
        ("Viuda Negra", 1964, "Marvel", "Espía rusa, maestra en combate cuerpo a cuerpo, viste un traje negro."),
        ("Black Panther", 1966, "Marvel", "T'Challa, rey de Wakanda, usa un traje de vibranium."),
        ("Capitana Marvel", 1968, "Marvel", "Carol Danvers, piloto con poderes cósmicos tras una explosión Kree."),
        ("Wolverine", 1974, "Marvel", "Logan, mutante con garras de adamantium y factor de curación."),
        ("Star-Lord", 1976, "Marvel", "Peter Quill, líder de los Guardianes de la Galaxia, usa un casco y armas."),
        ("Cyborg", 1980, "DC", "Victor Stone, mitad humano y mitad máquina, integrante de la Liga de la Justicia."),
        ("Shazam", 1940, "DC", "El niño Billy Batson se transforma en héroe al pronunciar una palabra mágica."),
    ]
    for nombre, anio, casa, bio in datos:
        insertar(lista, Superheroe(nombre, anio, casa, bio), "nombre")


# ----------------------------------------------------------------------------
# ACTIVIDADES a) a i)
# ----------------------------------------------------------------------------
def eliminar_heroe(lista, nombre):
    """a. Elimina el nodo del superhéroe indicado."""
    return eliminar(lista, nombre, "nombre")


def mostrar_anio_aparicion(lista, nombre):
    """b. Muestra el año de aparición del superhéroe."""
    pos = buscar(lista, nombre, "nombre")
    if pos is not None:
        print(f"{pos.info.nombre} apareció en {pos.info.anio_aparicion}")
    else:
        print(f"{nombre} no está en la lista")


def cambiar_casa(lista, nombre, nueva_casa):
    """c. Cambia la casa de comic del superhéroe."""
    pos = buscar(lista, nombre, "nombre")
    if pos is not None:
        pos.info.casa = nueva_casa
        print(f"La casa de {pos.info.nombre} ahora es {pos.info.casa}")
    else:
        print(f"{nombre} no está en la lista")


def heroes_con_palabras(lista, palabras):
    """d. Muestra el nombre de los superhéroes cuya biografía menciona alguna de las palabras."""
    patron = re.compile(r"\b(" + "|".join(palabras) + r")\b", re.IGNORECASE)
    aux = lista.inicio
    while aux is not None:
        if patron.search(aux.info.biografia):
            print(aux.info.nombre)
        aux = aux.sig


def heroes_anteriores_a(lista, anio):
    """e. Muestra nombre y casa de los superhéroes con aparición anterior al año dado."""
    aux = lista.inicio
    while aux is not None:
        if aux.info.anio_aparicion < anio:
            print(f"{aux.info.nombre} - {aux.info.casa}")
        aux = aux.sig


def mostrar_casa(lista, nombre):
    """f. Muestra la casa de comic a la que pertenece el superhéroe."""
    pos = buscar(lista, nombre, "nombre")
    if pos is not None:
        print(f"{pos.info.nombre} pertenece a {pos.info.casa}")
    else:
        print(f"{nombre} no está en la lista")


def mostrar_informacion(lista, nombre):
    """g. Muestra toda la información del superhéroe."""
    pos = buscar(lista, nombre, "nombre")
    if pos is not None:
        print(pos.info)
    else:
        print(f"{nombre} no está en la lista")


def heroes_por_iniciales(lista, letras):
    """h. Lista los superhéroes cuyo nombre comienza con alguna de las letras dadas."""
    aux = lista.inicio
    while aux is not None:
        if aux.info.nombre[0].upper() in letras:
            print(aux.info.nombre)
        aux = aux.sig


def contar_por_casa(lista):
    """i. Determina cuántos superhéroes hay de cada casa de comic."""
    marvel = dc = 0
    aux = lista.inicio
    while aux is not None:
        if aux.info.casa == "Marvel":
            marvel += 1
        elif aux.info.casa == "DC":
            dc += 1
        aux = aux.sig
    return marvel, dc


# ----------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    superheroes = Lista()
    cargar_superheroes(superheroes)

    print("--- Lista cargada (ordenada por nombre) ---")
    barrido(superheroes)

    print("\na. Eliminar a Linterna Verde")
    eliminado = eliminar_heroe(superheroes, "Linterna Verde")
    print("Eliminado:" , eliminado.nombre if eliminado else "no se encontró")

    print("\nb. Año de aparición de Wolverine")
    mostrar_anio_aparicion(superheroes, "Wolverine")

    print("\nc. Cambiar la casa de Dr. Strange a Marvel")
    cambiar_casa(superheroes, "Dr. Strange", "Marvel")

    print('\nd. Superhéroes cuya biografía menciona "traje" o "armadura"')
    heroes_con_palabras(superheroes, ["traje", "armadura"])

    print("\ne. Superhéroes con aparición anterior a 1963 (nombre y casa)")
    heroes_anteriores_a(superheroes, 1963)

    print("\nf. Casa de Capitana Marvel y Mujer Maravilla")
    mostrar_casa(superheroes, "Capitana Marvel")
    mostrar_casa(superheroes, "Mujer Maravilla")

    print("\ng. Información de Flash y Star-Lord")
    mostrar_informacion(superheroes, "Flash")
    mostrar_informacion(superheroes, "Star-Lord")

    print("\nh. Superhéroes que comienzan con B, M y S")
    heroes_por_iniciales(superheroes, ("B", "M", "S"))

    print("\ni. Cantidad de superhéroes por casa")
    cant_marvel, cant_dc = contar_por_casa(superheroes)
    print(f"Marvel: {cant_marvel}")
    print(f"DC: {cant_dc}")
