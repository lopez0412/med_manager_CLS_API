import traceback

from src.database.db_mysql import get_connection
from src.utils.Logger import Logger
from src.models.pacienteModel import Paciente


class PacienteService():
    
    # obtener los pacientes
    @classmethod
    def get_pacientes(cls):
        try:
            connection = get_connection()
            pacientes = []
            with connection.cursor() as cursor:
                cursor.execute('call sp_listPacientes()')
                resultset = cursor.fetchall()
                for row in resultset:
                    paciente = Paciente(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17])
                    pacientes.append(paciente.to_json())
            connection.close()
            return pacientes
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

    
    #Metodo para buscar paciente
    def buscarPaciente(busqueda):
        try:
            connection = get_connection()
            pacientes = []
            with connection.cursor() as cursor:
                cursor.callproc('sp_buscarPaciente', (busqueda,))
                resultset = cursor.fetchall()
                for row in resultset:
                    paciente = Paciente(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17])
                    pacientes.append(paciente.to_json())
            connection.commit()
            return pacientes
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
        finally:
            connection.close()

    # Guardar un Paciente nuevo.
    def guardar_paciente(nombre, numero_registro, gen_id, edad, direccion, dep_id, mun_id, estado_civil,
                     telefono, fecha_nacimiento, numero_dui, nombre_madre, nombre_padre, responsable,
                     tel_contacto, id_usuario):
        try:
            #verifica valores y asigna los nulos si es necesario
            numero_dui = numero_dui if numero_dui is not None else None
            nombre_madre = nombre_madre if nombre_madre is not None else None
            nombre_padre = nombre_padre if nombre_padre is not None else None
            responsable = responsable if responsable is not None else None
            tel_contacto = tel_contacto if tel_contacto is not None else None

            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.callproc('sp_addPaciente', (
                    nombre, numero_registro, gen_id, edad, direccion, dep_id, mun_id, estado_civil,
                    telefono, fecha_nacimiento, numero_dui, nombre_madre, nombre_padre, responsable,
                    tel_contacto, id_usuario
                ))

            connection.commit()

            return {'tipo': 'success','mensaje': "Paciente agregado correctamente"}
        
        except Exception as e:
            Logger.add_to_log("error", str(e))
            return {'error': str(e)}

        finally:
            connection.close()


    # editar pacientes
    def editar_paciente(pacienteId, nombre, numero_registro, gen_id, edad, direccion, dep_id, mun_id, estado_civil,
                     telefono, fecha_nacimiento, numero_dui, nombre_madre, nombre_padre, responsable,
                     tel_contacto, id_usuario):
        try:
            connection =  get_connection()

            with connection.cursor() as cursor:
                cursor.callproc('sp_editarPaciente', (
                    pacienteId, nombre, numero_registro, gen_id, edad, direccion, dep_id, mun_id, estado_civil,
                    telefono, fecha_nacimiento, numero_dui, nombre_madre, nombre_padre, responsable,
                    tel_contacto, id_usuario
                ))

            connection.commit()
            return {'tipo': 'success','mensaje': "Paciente editado correctamente"}
        except Exception as e:
            Logger.add_to_log("error", str(e))
            return {'error': str(e)}


        finally:
            connection.close()

    
    #Metodo para borrar
    def borrarPaciente(id_paciente):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.callproc('sp_borrarPaciente', (id_paciente,))

            connection.commit()
            return {'tipo': 'success','mensaje': "Paciente borrado correctamente"}
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
        finally:
            connection.close()
    