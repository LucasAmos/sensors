from flask_marshmallow import Marshmallow
from models import Sensordata
from marshmallow import Schema, fields

ma = Marshmallow()


class SensordataSchema(ma.Schema):

        co2 = fields.Str(attribute="co2")
        voc = fields.Str(attribute="voc")
        date = fields.DateTime(attribute="time")
        dht22 = fields.Str(attribute="dht22")
        dht11 = fields.Str(attribute="dht11")
        device = fields.Str(attribute="DeviceID")
        humidity = fields.Str(attribute="humidity")
        light = fields.Str(attribute="light")

        model = Sensordata

Sensordata_schema = SensordataSchema()
Sensordatas_schema = SensordataSchema(many=True)

