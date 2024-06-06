class JuegoVO:
    def __init__(self, IDJuego, Nombre, Dificultad, Descripcion=None, ruta=None):
        self._IDJuego = IDJuego
        self._Nombre = Nombre
        self._Dificultad = Dificultad
        self._Descripcion = Descripcion
        self._ruta = ruta

    def get_IDJuego(self):
        return self._IDJuego

    def set_IDJuego(self, IDJuego):
        self._IDJuego = IDJuego

    def get_Nombre(self):
        return self._Nombre

    def set_Nombre(self, Nombre):
        self._Nombre = Nombre

    def get_Dificultad(self):
        return self._Dificultad

    def set_Dificultad(self, Dificultad):
        self._Dificultad = Dificultad

    def get_Descripcion(self):
        return self._Descripcion

    def set_Descripcion(self, Descripcion):
        self._Descripcion = Descripcion

    def get_ruta(self):
        return self._ruta

    def set_ruta(self, ruta):
        self._ruta = ruta


class JuegoObraVO(JuegoVO):
    def __init__(self, IDJuegoobra, IDObra):
        self._IDJuegoobra = IDJuegoobra
        self._IDObra = IDObra

    def get_IDJuegoobra(self):
        return self._IDJuegoobra

    def set_IDJuegoobra(self, IDJuegoobra):
        self._IDJuegoobra = IDJuegoobra

    def get_IDObra(self):
        return self._IDObra

    def set_IDObra(self, IDObra):
        self._IDObra = IDObra


class JuegoSalaVO(JuegoVO):
    def __init__(self, IDJuegossalas, IDSala):
        self._IDJuegossalas = IDJuegossalas
        self._IDSala = IDSala

    def get_IDJuegossalas(self):
        return self._IDJuegossalas

    def set_IDJuegossalas(self, IDJuegossalas):
        self._IDJuegossalas = IDJuegossalas

    def get_IDSala(self):
        return self._IDSala

    def set_IDSala(self, IDSala):
        self._IDSala = IDSala
