from flask import Flask
from flask_restful import Resource, Api
from employeeview import EmployeeView

app = Flask(__name__)
api = Api(app)

api.add_resource(EmployeeView, '/employee/api/v1.0/all')


if __name__ == '__main__':
    app.run(debug=True)
