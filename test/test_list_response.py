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

from sensorpush_api.models.list_response import ListResponse  # noqa: E501

class TestListResponse(unittest.TestCase):
    """ListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListResponse:
        """Test ListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListResponse`
        """
        model = ListResponse()  # noqa: E501
        if include_optional:
            return ListResponse(
                files = [
                    sensorpush_api.models.report_listing.ReportListing(
                        last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        size = '', )
                    ]
            )
        else:
            return ListResponse(
        )
        """

    def testListResponse(self):
        """Test ListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
