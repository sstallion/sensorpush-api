# coding: utf-8

"""
    SensorPush Public API

    This is a swagger definition for the SensorPush public REST API. Download the definition file [here](https://api.sensorpush.com/api/v1/support/swagger/swagger-v1.json).

    The version of the OpenAPI document: v1.0.20240803
    Contact: support@sensorpush.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union

try:
    from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr
except ImportError:
    from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class TokenResponse(BaseModel):
    """
    Response object for an oAuth authorization code.  # noqa: E501
    """
    access_token: Optional[StrictStr] = Field(default=None, description="JWT oAuth access token. Pass this token to the data services via the http header 'Authorization'. Example 'Authorization' : 'Bearer <access token>'")
    expires_in: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="TTL of the token in seconds")
    refresh_token: Optional[StrictStr] = Field(default=None, description="JWT oAuth refresh token. Pass this token to the token service to retrieve a new access token.")
    token_type: Optional[StrictStr] = Field(default=None, description="Type of token returned")
    __properties = ["access_token", "expires_in", "refresh_token", "token_type"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TokenResponse:
        """Create an instance of TokenResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TokenResponse:
        """Create an instance of TokenResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TokenResponse.parse_obj(obj)

        _obj = TokenResponse.parse_obj({
            "access_token": obj.get("access_token"),
            "expires_in": obj.get("expires_in"),
            "refresh_token": obj.get("refresh_token"),
            "token_type": obj.get("token_type")
        })
        return _obj


