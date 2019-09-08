from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

employee = []

class EmployeeName(Resource):

    def get(self,name):
        
        for emp in employee:
            if emp['name']==name:
                return emp
        return {'name': name + ' is not an employee yet'},404

    def post(self,name):

        emp ={'name':name}
        employee.append(emp)

        return emp

    def delete(self,name):
        for ind,emp in enumerate(employee):
            if emp['name'] ==name:
                employee.pop(ind)
                return {'note':'delete success'}
        return {'Alert':name +' does not exits to be deleted'},404

class Allnames(Resource):
    def get(self):
        return {'Employees':employee}

api.add_resource(EmployeeName,'/employee/<string:name>')
api.add_resource(Allnames,'/employees')

if __name__ == "__main__":
    app.run(debug=True)