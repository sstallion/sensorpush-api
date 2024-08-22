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


from typing import Optional

try:
    from pydantic.v1 import BaseModel, Field, StrictStr
except ImportError:
    from pydantic import BaseModel, Field, StrictStr

class ReportsRequest(BaseModel):
    """
    Request object for reports.  # noqa: E501
    """
    path: Optional[StrictStr] = Field(default=None, description="The directory path to perform this operation.")
    __properties = ["path"]

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
    def from_json(cls, json_str: str) -> ReportsRequest:
        """Create an instance of ReportsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReportsRequest:
        """Create an instance of ReportsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReportsRequest.parse_obj(obj)

        _obj = ReportsRequest.parse_obj({
            "path": obj.get("path")
        })
        return _obj


