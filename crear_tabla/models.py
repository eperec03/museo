from orm_config import Base,engine,session
from sqlalchemy import Column, VARCHAR, INTEGER, DATE, ForeignKey, UniqueConstraint, CheckConstraint,func

class Usuarios(Base):
    __tablename__ = "USUARIOS"
    dni = Column(VARCHAR(length=9), primary_key=True)
    usuNombreCompleto = Column(VARCHAR(length=50), nullable=False)
    usuTfno = Column(VARCHAR(length=9), nullable=False)
    usuEmail = Column(VARCHAR(length=50), nullable=False)
    usuTitularMP = Column(VARCHAR(length=50))
    usuCvvMP = Column(INTEGER)
    usuCadMP = Column(DATE)
    usuContraseña = Column(VARCHAR(length=100), nullable=False)
    usuFecha = Column(DATE, nullable=False)

    __table_args__ = (
        CheckConstraint("usuEmail LIKE '%@%.com'", name="UECHECK"),
        UniqueConstraint('usuEmail', name='UQ_UsuEmail'),
        CheckConstraint("usuCvvMP BETWEEN 0 AND 999", name="UCMPCHECK")
        # CheckConstraint("UsuContraseña like '%[0-9]%[A-Z]%[a-z]'", name="UCCHECK"),
    )

    def __init__(self, dni, usuNombreCompleto, usuTfno, usuEmail, usuTitularMP, usuCvvMP, usuCadMP, usuContraseña, usuFecha):
        self.dni = dni
        self.usuNombreCompleto = usuNombreCompleto
        self.usuTfno = usuTfno
        self.usuEmail = usuEmail
        self.usuTitularMP = usuTitularMP
        self.usuCvvMP = usuCvvMP
        self.usuCadMP = usuCadMP
        self.usuContraseña = usuContraseña
        self.usuFecha = usuFecha

    def __repr__(self):
        return f"<Usuarios(dni='{self.dni}', usuNombreCompleto='{self.usuNombreCompleto}', usuTfno='{self.usuTfno}', usuEmail='{self.usuEmail}', usuTitularMP='{self.usuTitularMP}', usuCvvMP={self.usuCvvMP}, usuCadMP='{self.usuCadMP}', usuContraseña='{self.usuContraseña}', usuFecha='{self.usuFecha}')>"

Base. metadata.create_all(engine)
nuevo_usuario = Usuarios(
    dni='71345267S',
    usuNombreCompleto='Pedro Alonso Juez',
    usuTfno='651634873',
    usuEmail='pedritoalju@gmail.com',
    usuTitularMP='Pedro Alonso Juez',
    usuCvvMP=234,
    usuCadMP='2030-06-07',
    usuContraseña='25Antonio',
    usuFecha='2024-04-25'
)
session.add(nuevo_usuario)
session.commit()
session.close()
