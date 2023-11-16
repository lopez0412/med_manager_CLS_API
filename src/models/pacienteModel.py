class Paciente():

    def __init__(self,pacienteId ,nombre, numeroRegistro, genId, edad, direccion, depId, munId, estadoCivil, telefono, fechaNacimiento, numeroDui, nombreMadre, nombrePadre, responsable, telContacto, idUsuarioCreacion, fechaCreacion) -> None:
        self.pacienteId  = pacienteId 
        self.nombre = nombre
        self.numeroRegistro = numeroRegistro
        self.genId = genId
        self.edad = edad
        self.direccion = direccion
        self.depId = depId
        self.munId = munId
        self.estadoCivil = estadoCivil
        self.telefono = telefono
        self.fechaNacimiento = fechaNacimiento
        self.numeroDui = numeroDui
        self.nombreMadre = nombreMadre
        self.nombrePadre = nombrePadre
        self.responsable = responsable
        self.telContacto = telContacto
        self.idUsuarioCreacion = idUsuarioCreacion
        self.fechaCreacion = fechaCreacion

    def to_json(self):
        return{
            'pacienteId': self.pacienteId,
            'nombre': self.nombre,
            'numeroRegistro': self.numeroRegistro,
            'genId': self.genId,
            'edad': self.edad,
            'direccion': self.direccion,
            'depId': self.depId,
            'munId': self.munId,
            'estadoCivil': self.estadoCivil,
            'telefono': self.telefono,
            'fechaNacimiento': self.fechaNacimiento,
            'numeroDui':self.numeroDui,
            'nombreMadre': self.nombreMadre,
            'nombrePadre': self.nombrePadre,
            'responsable': self.responsable,
            'telContacto': self.telContacto,
            'idUsusarioCreacion': self.idUsuarioCreacion,
            'fechaCreacion': self.fechaCreacion
        }