from flask_restful import Resource
from flask import request
from .models import Vihicle, Manufacturer
from .schemas import VehicleSchema
from marshmallow import ValidationError

class VehicleResorces(Resource):
    def get(self, vehicle_id=None):
        if vehicle_id:
            result = Vihicle.objects.get(id=vehicle_id)
            return VehicleSchema().dump(result)
        else:
            result=Vihicle.objects()
            return VehicleSchema().dump(result,  many=True)

    def post(self):
        try:
            res = VehicleSchema().load(request.get_json())
            obj = Vihicle.objects.create(**res)
            return VehicleSchema().dumps(obj)

        except ValidationError as err:
            return {'error': err.messages}


    def put(self, vehicle_id):
        try:
            res = VehicleSchema().load(request.get_json())
            obj = Vihicle.objects.get(id=vehicle_id)
            res['manufacturer'] = Manufacturer.objects.get(id=res['manufacturer'])
            obj.update(**res)
            return VehicleSchema().dumps(obj.reload())

        except ValidationError as err:
            return {'error': err.messages}

    def delete(self, vehicle_id):
        Vihicle.objects.get(id=vehicle_id).delete()
        return {'status': 'delete'}


class ManufacturerResources(Resource):
    def get(self, manufacturer_id=None):
        pass

    def post(self):
        pass

    def put(self, manufacturer_id):
        pass

    def delete(self, manufacturer_id):
        pass