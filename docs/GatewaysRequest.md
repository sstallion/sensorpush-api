# GatewaysRequest

Request object for gateways.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | Returns the results as the specified format (csv|json). Defaults to json | [optional] 

## Example

```python
from sensorpush_api.models.gateways_request import GatewaysRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GatewaysRequest from a JSON string
gateways_request_instance = GatewaysRequest.from_json(json)
# print the JSON string representation of the object
print GatewaysRequest.to_json()

# convert the object into a dict
gateways_request_dict = gateways_request_instance.to_dict()
# create an instance of GatewaysRequest from a dict
gateways_request_from_dict = GatewaysRequest.from_dict(gateways_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


