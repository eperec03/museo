class UsuarioVO:
    def __init__(self, DNI, UsuNombreCompleto, Usutfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna, UsuFecha):
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
    def __init__(self, DNI, UsuNombreCompleto, Usutfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna, UsuFecha, ObrasAdquiridas, DineroGastado, Penalizacion, TipoTarifa):
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
    def __init__(self, SSN, UsuNombreCompleto, Usutfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna, UsuFecha, Rol):
        super().__init__(SSN, UsuNombreCompleto, Usutfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna, UsuFecha)
        self.Rol = Rol
        
    def get_Rol(self):
        return self.Rol

    def set_Rol(self, Rol):
        self.Rol = Rol

