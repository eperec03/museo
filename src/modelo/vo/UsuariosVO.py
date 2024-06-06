class UsuarioVO:
    def __init__(self, DNI, UsuNombreCompleto, Usutfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna, UsuFecha):
        self._DNI = DNI
        self._UsuNombreCompleto = UsuNombreCompleto
        self._Usutfno = Usutfno
        self._UsuEmail = UsuEmail
        self._UsuTitularMP = UsuTitularMP
        self._UsuNumTarjMP = UsuNumTarjMP
        self._UsuCvvMP = UsuCvvMP
        self._UsuCadMP = UsuCadMP
        self._UsuContrasenna = UsuContrasenna
        self._UsuFecha = UsuFecha

    def get_DNI(self):
        return self._DNI

    def set_DNI(self, DNI):
        self._DNI = DNI

    def get_UsuNombreCompleto(self):
        return self._UsuNombreCompleto

    def set_UsuNombreCompleto(self, UsuNombreCompleto):
        self._UsuNombreCompleto = UsuNombreCompleto

    def get_Usutfno(self):
        return self._Usutfno

    def set_Usutfno(self, Usutfno):
        self._Usutfno = Usutfno

    def get_UsuEmail(self):
        return self._UsuEmail

    def set_UsuEmail(self, UsuEmail):
        self._UsuEmail = UsuEmail

    def get_UsuTitularMP(self):
        return self._UsuTitularMP

    def set_UsuTitularMP(self, UsuTitularMP):
        self._UsuTitularMP = UsuTitularMP

    def get_UsuNumTarjMP(self):
        return self._UsuNumTarjMP

    def set_UsuNumTarjMP(self, UsuNumTarjMP):
        self._UsuNumTarjMP = UsuNumTarjMP

    def get_UsuCvvMP(self):
        return self._UsuCvvMP

    def set_UsuCvvMP(self, UsuCvvMP):
        self._UsuCvvMP = UsuCvvMP

    def get_UsuCadMP(self):
        return self._UsuCadMP

    def set_UsuCadMP(self, UsuCadMP):
        self._UsuCadMP = UsuCadMP

    def get_UsuContrasenna(self):
        return self._UsuContrasenna

    def set_UsuContrasenna(self, UsuContrasenna):
        self._UsuContrasenna = UsuContrasenna

    def get_UsuFecha(self):
        return self._UsuFecha

    def set_UsuFecha(self, UsuFecha):
        self._UsuFecha = UsuFecha


class ClientePremiumVO(UsuarioVO):
    def __init__(self, DNI, UsuNombreCompleto, Usutfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna, UsuFecha, ObrasAdquiridas, DineroGastado, Penalizacion, TipoTarifa):
        super().__init__(DNI, UsuNombreCompleto, Usutfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna, UsuFecha)
        self._ObrasAdquiridas = ObrasAdquiridas
        self._DineroGastado = DineroGastado
        self._Penalizacion = Penalizacion
        self._TipoTarifa = TipoTarifa

    def get_ObrasAdquiridas(self):
        return self._ObrasAdquiridas

    def set_ObrasAdquiridas(self, ObrasAdquiridas):
        self._ObrasAdquiridas = ObrasAdquiridas

    def get_DineroGastado(self):
        return self._DineroGastado

    def set_DineroGastado(self, DineroGastado):
        self._DineroGastado = DineroGastado

    def get_Penalizacion(self):
        return self._Penalizacion

    def set_Penalizacion(self, Penalizacion):
        self._Penalizacion = Penalizacion

    def get_TipoTarifa(self):
        return self._TipoTarifa

    def set_TipoTarifa(self, TipoTarifa):
        self._TipoTarifa = TipoTarifa


class EditorVO(UsuarioVO):
    def __init__(self, SSN, UsuNombreCompleto, Usutfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna, UsuFecha, Horario, TipoContrato, Estudios):
        super().__init__(SSN, UsuNombreCompleto, Usutfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna, UsuFecha)
        self._Horario = Horario
        self._TipoContrato = TipoContrato
        self._Estudios = Estudios

    def get_Horario(self):
        return self._Horario

    def set_Horario(self, Horario):
        self._Horario = Horario

    def get_TipoContrato(self):
        return self._TipoContrato

    def set_TipoContrato(self, TipoContrato):
        self._TipoContrato = TipoContrato

    def get_Estudios(self):
        return self._Estudios

    def set_Estudios(self, Estudios):
        self._Estudios = Estudios
