from flask import Blueprint, request, jsonify
from flask_cors import CORS
import traceback

from src.utils.Logger import Logger
from src.utils.Security import Security
from src.services.PacientesService import PacienteService

main = Blueprint('pacientes_blueprint', __name__)
CORS(main)

@main.route('/')
def get_pacientes():
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            pacientes = PacienteService.get_pacientes()
            if (len(pacientes) > 0):
                return jsonify({'pacientes': pacientes, 'message': "SUCCESS", 'success': True})
            else:
                return jsonify({'message': "NOTFOUND", 'success': True})
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

            return jsonify({'message': "ERROR", 'success': False})
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401

#TODO: Cambia los nombres de los campos para evitar un missunderstand
@main.route('/guardar', methods=['POST'])
def route_guardar_paciente():
    
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            # TODO: Validacion de valores null en numero de dui y extras..
            # Llamada al servicio para guardar el paciente
            resultado = PacienteService.guardar_paciente(
                nombre=request.json['nombre'],
                numero_registro=request.json['numeroRegistro'],
                gen_id=request.json['genId'],
                edad=request.json['edad'],
                direccion=request.json['direccion'],
                dep_id=request.json['depId'],
                mun_id=request.json['munId'],
                estado_civil=request.json['estadoCivil'],
                telefono=request.json['telefono'],
                fecha_nacimiento=request.json['fechaNacimiento'],
                numero_dui=request.json.get('numeroDui'),
                nombre_madre=request.json.get('nombreMadre'),
                nombre_padre=request.json.get('nombreMadre'),
                responsable=request.json.get('responsable'),
                tel_contacto=request.json.get('telContacto'),
                id_usuario=request.json['id_usuario']
            )

            return jsonify(resultado)

        except Exception as e:
            Logger.add_to_log("error", str(e))
            Logger.add_to_log("error", traceback.format_exc())
            return jsonify({'error': str(e)})

    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401

# ... Puedes agregar más rutas relacionadas con pacientes aquí ...

# ... Ruta para buscar al usuario por  nombre, direccion, telefono, dui ...

@main.route('/buscar', methods=['POST'])
def buscarPaciente():
    has_access = Security.verify_token(request.headers)
    busqueda = str(request.json['busqueda'])

    if has_access:
        try:
            pacientes = PacienteService.buscarPaciente(busqueda)
            if (len(pacientes) > 0):
                return jsonify({'pacientes': pacientes, 'message': "SUCCESS", 'success': True})
            else:
                return jsonify({'message': "NOTFOUND", 'success': True})
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

            return jsonify({'message': "ERROR", 'success': False})
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401

# ... Ruta para editar al usuario por id ...

#TODO: Cambia los nombres de los campos para evitar un missunderstand
@main.route('/editar', methods=['PUT'])
def route_editar_paciente():
    
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            # TODO: Validacion de valores null en numero de dui y extras..
            # Llamada al servicio para guardar el paciente
            resultado = PacienteService.editar_paciente(
                pacienteId=request.json['pacienteId'],
                nombre=request.json['nombre'],
                numero_registro=request.json['numeroRegistro'],
                gen_id=request.json['genId'],
                edad=request.json['edad'],
                direccion=request.json['direccion'],
                dep_id=request.json['depId'],
                mun_id=request.json['munId'],
                estado_civil=request.json['estadoCivil'],
                telefono=request.json['telefono'],
                fecha_nacimiento=request.json['fechaNacimiento'],
                numero_dui=request.json.get('numeroDui'),
                nombre_madre=request.json.get('nombreMadre'),
                nombre_padre=request.json.get('nombreMadre'),
                responsable=request.json.get('responsable'),
                tel_contacto=request.json.get('telContacto'),
                id_usuario=request.json['id_usuario']
            )

            return jsonify(resultado)

        except Exception as e:
            Logger.add_to_log("error", str(e))
            Logger.add_to_log("error", traceback.format_exc())
            return jsonify({'error': str(e)})

    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401

# ... Ruta para borrar el paciente por Id ...
@main.route('/borrar/<int:id_paciente>', methods=['DELETE'])
def borrarPaciente(id_paciente):
    has_access = Security.verify_token(request.headers)

    if has_access:
        try:
            resultado = PacienteService.borrarPaciente(id_paciente)

            return jsonify(resultado)
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

            return jsonify({'message': "ERROR", 'success': False})
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401


