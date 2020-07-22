from flask import Flask
from flask_restful import Api
from .resources import VehicleResorces, ManufacturerResources

app = Flask(__name__)
api = Api(app)

api.add_resource(VehicleResorces, '/vihecles', '/vihecles/<vehicle_id>')
api.add_resource(ManufacturerResources, '/manufacturers', '/manufacturers/<manufacturer_id>')