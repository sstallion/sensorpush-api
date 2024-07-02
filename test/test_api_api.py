# coding: utf-8

"""
    SensorPush Public API

    This is a swagger definition for the SensorPush public REST API. Download the definition file [here](https://api.sensorpush.com/api/v1/support/swagger/swagger-v1.json).  # noqa: E501

    OpenAPI spec version: v1.0.20240629
    Contact: support@sensorpush.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import sensorpush_api
from sensorpush_api.api.api_api import ApiApi  # noqa: E501
from sensorpush_api.rest import ApiException


class TestApiApi(unittest.TestCase):
    """ApiApi unit test stubs"""

    def setUp(self):
        self.api = ApiApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_access_token(self):
        """Test case for access_token

        Request a temporary oAuth access code.  # noqa: E501
        """
        pass

    def test_download(self):
        """Test case for download

        Download bulk reports.  # noqa: E501
        """
        pass

    def test_gateways(self):
        """Test case for gateways

        Lists all gateways.  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        Lists reports available for download.  # noqa: E501
        """
        pass

    def test_oauth_authorize_post(self):
        """Test case for oauth_authorize_post

        Sign in and request an authorization code  # noqa: E501
        """
        pass

    def test_root_post(self):
        """Test case for root_post

        SensorPush API status  # noqa: E501
        """
        pass

    def test_samples(self):
        """Test case for samples

        Queries for sensor samples.  # noqa: E501
        """
        pass

    def test_sensors(self):
        """Test case for sensors

        Lists all sensors.  # noqa: E501
        """
        pass

    def test_tags_response(self):
        """Test case for tags_response

        Updates tags on devices.  # noqa: E501
        """
        pass

    def test_token(self):
        """Test case for token

        oAuth 2.0 for authorization, access, and refresh tokens  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
