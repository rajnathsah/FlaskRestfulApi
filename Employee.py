from sqlalchemy.ext.automap import automap_base
from marshmallow import Schema, fields

Base = automap_base()

'''
Employee class to map with employee table
'''
class Employee(Base):
    __tablename__ = 'employee'

'''
Employee schema for serializing the employee table data
'''
class EmployeeSchema(Schema):
    employee_id = fields.Int()
    employee_name = fields.Str()
    employee_sal = fields.Int()
