class UsuarioVO:
    def __init__(self, DNI=None, UsuNombreCompleto=None, Usutfno=None, UsuEmail=None, UsuTitularMP=None, UsuNumTarjMP=None, UsuCvvMP=None, UsuCadMP=None, UsuContrasenna=None, UsuFecha=None):
        self.DNI = DNI
        self.UsuNombreCompleto = UsuNombreCompleto
        self.Usutfno = Usutfno
        self.UsuEmail = UsuEmail
        self.UsuTitularMP = UsuTitularMP
        self.UsuNumTarjMP = UsuNumTarjMP
        self.UsuCvvMP = UsuCvvMP
        self.UsuCadMP = UsuCadMP
        self.UsuContrasenna = UsuContrasenna
        self.UsuFecha = UsuFecha

    def get_DNI(self):
        return self.DNI

    def set_DNI(self, DNI):
        self.DNI = DNI

    def get_UsuNombreCompleto(self):
        return self.UsuNombreCompleto

    def set_UsuNombreCompleto(self, UsuNombreCompleto):
        self.UsuNombreCompleto = UsuNombreCompleto

    def get_Usutfno(self):
        return self.Usutfno

    def set_Usutfno(self, Usutfno):
        self.Usutfno = Usutfno

    def get_UsuEmail(self):
        return self.UsuEmail

    def set_UsuEmail(self, UsuEmail):
        self.UsuEmail = UsuEmail

    def get_UsuTitularMP(self):
        return self.UsuTitularMP

    def set_UsuTitularMP(self, UsuTitularMP):
        self.UsuTitularMP = UsuTitularMP

    def get_UsuNumTarjMP(self):
        return self.UsuNumTarjMP

    def set_UsuNumTarjMP(self, UsuNumTarjMP):
        self.UsuNumTarjMP = UsuNumTarjMP

    def get_UsuCvvMP(self):
        return self.UsuCvvMP

    def set_UsuCvvMP(self, UsuCvvMP):
        self.UsuCvvMP = UsuCvvMP

    def get_UsuCadMP(self):
        return self.UsuCadMP

    def set_UsuCadMP(self, UsuCadMP):
        self.UsuCadMP = UsuCadMP

    def get_UsuContrasenna(self):
        return self.UsuContrasenna

    def set_UsuContrasenna(self, UsuContrasenna):
        self.UsuContrasenna = UsuContrasenna

    def get_UsuFecha(self):
        return self.UsuFecha

    def set_UsuFecha(self, UsuFecha):
        self.UsuFecha = UsuFecha


class ClientePremiumVO(UsuarioVO):
    def __init__(self, DNI=None, UsuNombreCompleto=None, Usutfno=None, UsuEmail=None, UsuTitularMP=None, UsuNumTarjMP=None, UsuCvvMP=None, UsuCadMP=None, UsuContrasenna=None, UsuFecha=None, ObrasAdquiridas=None, DineroGastado=None, Penalizacion=None, TipoTarifa=None):
        super().__init__(DNI, UsuNombreCompleto, Usutfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna, UsuFecha)
        self.ObrasAdquiridas = ObrasAdquiridas
        self.DineroGastado = DineroGastado
        self.Penalizacion = Penalizacion
        self.TipoTarifa = TipoTarifa

    def get_ObrasAdquiridas(self):
        return self.ObrasAdquiridas

    def set_ObrasAdquiridas(self, ObrasAdquiridas):
        self.ObrasAdquiridas = ObrasAdquiridas

    def get_DineroGastado(self):
        return self.DineroGastado

    def set_DineroGastado(self, DineroGastado):
        self.DineroGastado = DineroGastado

    def get_Penalizacion(self):
        return self.Penalizacion

    def set_Penalizacion(self, Penalizacion):
        self.Penalizacion = Penalizacion

    def get_TipoTarifa(self):
        return self.TipoTarifa

    def set_TipoTarifa(self, TipoTarifa):
        self.TipoTarifa = TipoTarifa


class EditorVO(UsuarioVO):
    def __init__(self, DNI=None, UsuNombreCompleto=None, Usutfno=None, UsuEmail=None, UsuTitularMP=None, UsuNumTarjMP=None, UsuCvvMP=None, UsuCadMP=None, UsuContrasenna=None, UsuFecha=None, Rol=None):
        super().__init__(DNI, UsuNombreCompleto, Usutfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna, UsuFecha)
        self.Rol = Rol
        
    def get_Rol(self):
        return self.Rol

    def set_Rol(self, Rol):
        self.Rol = Rol

# cliente1 = ClientePremiumVO()

# cliente1.set_DNI("12345678A")
# cliente1.set_UsuNombreCompleto("Juan Pérez")
# cliente1.set_Usutfno("123456789")
# cliente1.set_UsuEmail("juan.perez@example.com")
# cliente1.set_UsuTitularMP("Juan Pérez")
# cliente1.set_UsuNumTarjMP("1234 5678 9012 3456")
# cliente1.set_UsuCvvMP("123")
# cliente1.set_UsuCadMP("2024-12-31")  
# cliente1.set_UsuContrasenna("miContraseñaSegura")
# cliente1.set_UsuFecha("2024-06-01")  
# cliente1.set_ObrasAdquiridas(10)
# cliente1.set_DineroGastado(2500.75)
# cliente1.set_Penalizacion(0)
# cliente1.set_TipoTarifa("Reducida")

# print(cliente1.get_UsuContrasenna())