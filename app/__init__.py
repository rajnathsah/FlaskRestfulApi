from flask import Flask
from flask_restful import Api
from app.employeeview import EmployeeView

app = Flask(__name__)
api = Api(app)

api.add_resource(EmployeeView, '/employee/api/v1.0/all')
