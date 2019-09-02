from flask_restful import Resource, reqparse
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
from app.dbconnection import getEngine
from flask import jsonify
from sqlalchemy.orm import Session
from app.employee import *

auth = HTTPBasicAuth()
parser = reqparse.RequestParser()
parser.add_argument("employee",type=dict,action="append")

@auth.verify_password
def verify_password(username, password):
    '''Verify login user password
    :param username:
    :param password:
    :return:
    '''
    dbpassword = None
    try:
        engine = getEngine()
        connection = engine.connect()
        result = connection.execute("select password from login where username='{0}'".format(username))
        # connection.close()
        for res in result:
            dbpassword = res[0]
        connection.close()
    except Exception as ex:
        print(ex)

    if username is not None and dbpassword is not None:
        return check_password_hash(dbpassword, password)
    return False


@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return jsonify({'message': 'Unauthorized access'})


class EmployeeView(Resource):
    decorators = [auth.login_required]

    def get(self):
        try:
            engine = getEngine()
            Base.prepare(engine, reflect=True)
            session = Session(engine)
            empschema = EmployeeSchema()
            allemp = session.query(Employee).all()
            result = empschema.dump(allemp, many=True)
            session.close()
            return {"employee": result}
        except Exception as ex:
            return jsonify({'Error':ex})


    def post(self):
        try:
            args = parser.parse_args()
            employees = args['employee']
            engine = getEngine()
            Base.prepare(engine, reflect=True)
            session = Session(engine)
            for a in employees:
                session.add(Employee(employee_name=a["employee_name"],employee_sal=a['employee_sal']))
                session.commit()
            session.close()
            return employees, 201
        except Exception as ex:
            return jsonify({'Error':ex})