import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from your_app import app, db, Paciente

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_borrar_paciente(self):
        # Agregar un paciente para probar el borrado
        paciente = Paciente(nombre='Juan')
        db.session.add(paciente)
        db.session.commit()

        # Realizar la solicitud de borrado
        response = self.app.delete('/borrar_paciente/1')

        # Verificar que se obtuvo una respuesta exitosa (código 200)
        self.assertEqual(response.status_code, 200)

        # Verificar que el paciente fue eliminado
        paciente_borrado = Paciente.query.get(1)
        self.assertIsNone(paciente_borrado)

if __name__ == '__main__':
    unittest.main()