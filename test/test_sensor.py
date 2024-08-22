# coding: utf-8

"""
    SensorPush Public API

    This is a swagger definition for the SensorPush public REST API. Download the definition file [here](https://api.sensorpush.com/api/v1/support/swagger/swagger-v1.json).

    The version of the OpenAPI document: v1.0.20240803
    Contact: support@sensorpush.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sensorpush_api.models.sensor import Sensor  # noqa: E501

class TestSensor(unittest.TestCase):
    """Sensor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Sensor:
        """Test Sensor
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Sensor`
        """
        model = Sensor()  # noqa: E501
        if include_optional:
            return Sensor(
                active = True,
                address = '',
                alerts = sensorpush_api.models.sensor_alerts.Sensor_alerts(
                    humidity = sensorpush_api.models.sensor_alerts_humidity.Sensor_alerts_humidity(
                        enabled = True, 
                        max = 1.337, 
                        min = 1.337, ), 
                    temperature = sensorpush_api.models.sensor_alerts_temperature.Sensor_alerts_temperature(
                        enabled = True, 
                        max = 1.337, 
                        min = 1.337, ), ),
                battery_voltage = 1.337,
                calibration = sensorpush_api.models.sensor_calibration.Sensor_calibration(
                    humidity = 1.337, 
                    temperature = 1.337, ),
                device_id = '',
                id = '',
                name = '',
                rssi = 1.337,
                tags = {
                    'key' : sensorpush_api.models.tags.Tags(
                        gateways = {
                            'key' : [
                                ''
                                ]
                            }, 
                        sensors = {
                            'key' : [
                                ''
                                ]
                            }, )
                    },
                type = ''
            )
        else:
            return Sensor(
        )
        """

    def testSensor(self):
        """Test Sensor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
