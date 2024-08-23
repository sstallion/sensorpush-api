# SensorsRequest

Request object for sensors.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | filters sensors by active &#x3D; (true|false). Defaults to true | [optional] 
**format** | **str** | Returns the results as the specified format (csv|json). Defaults to json | [optional] 

## Example

```python
from sensorpush_api.models.sensors_request import SensorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SensorsRequest from a JSON string
sensors_request_instance = SensorsRequest.from_json(json)
# print the JSON string representation of the object
print SensorsRequest.to_json()

# convert the object into a dict
sensors_request_dict = sensors_request_instance.to_dict()
# create an instance of SensorsRequest from a dict
sensors_request_from_dict = SensorsRequest.from_dict(sensors_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


