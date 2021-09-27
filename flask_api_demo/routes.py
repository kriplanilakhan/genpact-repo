from flask import request
from flask_restful import Resource

notes = [
    {
        "id": 1,
        "task": "Update node version"
    },
    {
        "id": 2,
        "task": "Buy groceries"
    }
]


class Notes(Resource):

    def get(self,id=0):
        print(id)
        data = notes
        if id:
            for item in notes:
                if item['id'] == id:
                    data = item


        return data

    def post(self):
        data = request.form.to_dict() if request.form.to_dict() else request.get_json()
        notes.append(data)
        return {"message": "Added note successfully"}, 200

    def delete(self,id):
        for item in notes:
            if id == item['id']:
                notes.remove(item)
        print(notes)
        return  notes

    def put(self,id):
        data = request.form.to_dict() if request.form.to_dict() else request.get_json()
        for item in notes:
            if id == item['id']:
                item['task'] = data['task']
                return {"message": "Added note successfully"}, 200
        return {"message": "ID not found"}, 404