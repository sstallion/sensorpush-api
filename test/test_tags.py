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

from sensorpush_api.models.tags import Tags  # noqa: E501

class TestTags(unittest.TestCase):
    """Tags unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Tags:
        """Test Tags
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Tags`
        """
        model = Tags()  # noqa: E501
        if include_optional:
            return Tags(
                gateways = {
                    'key' : [
                        ''
                        ]
                    },
                sensors = {
                    'key' : [
                        ''
                        ]
                    }
            )
        else:
            return Tags(
        )
        """

    def testTags(self):
        """Test Tags"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
