from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from flask_api_demo import routes

api.add_resource(routes.Notes, "/api/getnotes", "/api/getnotes/<int:id>", "/api/addnote", "/api/update/<int:id>",
                 "/api/delete/<int:id>", )
