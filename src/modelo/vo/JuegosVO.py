class JuegosVO:
    def __init__(self, IDJuego=None, Nombre=None, Dificultad=None, Descripcion=None, ruta=None):
        self.IDJuego = IDJuego
        self.Nombre = Nombre
        self.Dificultad = Dificultad
        self.Descripcion = Descripcion
        self.ruta = ruta

    def get_IDJuego(self):
        return self.IDJuego

    def set_IDJuego(self, IDJuego):
        self.IDJuego = IDJuego

    def get_Nombre(self):
        return self.Nombre

    def set_Nombre(self, Nombre):
        self.Nombre = Nombre

    def get_Dificultad(self):
        return self.Dificultad

    def set_Dificultad(self, Dificultad):
        self.Dificultad = Dificultad

    def get_Descripcion(self):
        return self.Descripcion

    def set_Descripcion(self, Descripcion):
        self.Descripcion = Descripcion

    def get_ruta(self):
        return self.ruta

    def set_ruta(self, ruta):
        self.ruta = ruta


class JuegosObrasVO(JuegosVO):
    def __init__(self, IDJuego=None, Nombre=None, Dificultad=None, Descripcion=None, ruta=None,IDObra=None):
        super().__init__(IDJuego, Nombre, Dificultad, Descripcion, ruta)
        self.IDJuegoobra = IDJuego
        self.IDObra = IDObra

    def get_IDObra(self):
        return self.IDObra

    def set_IDObra(self, IDObra):
        self.IDObra = IDObra


class JuegosSalasVO(JuegosVO):
    def __init__(self, IDSala=None,IDJuego=None, Nombre=None, Dificultad=None, Descripcion=None, ruta=None):
        super().__init__(IDJuego, Nombre, Dificultad, Descripcion, ruta)
        self.IDJuegossalas = IDJuego
        self.IDSala = IDSala

    def get_IDSala(self):
        return self.IDSala

    def set_IDSala(self, IDSala):
        self.IDSala = IDSala
