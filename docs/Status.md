# Status


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployed** | **str** | Date time when this service was last updated. | [optional] 
**message** | **str** | Greeting message. | 
**ms** | **int** | Current date time on the server in milliseconds. | [optional] 
**stack** | **str** | Active stack hosting this service. | [optional] 
**status** | **str** | Current status of the api service. | [optional] 
**time** | **str** | Current date time on the server. | [optional] 
**version** | **str** | Version of this service currently deployed | [optional] 

## Example

```python
from sensorpush_api.models.status import Status

# TODO update the JSON string below
json = "{}"
# create an instance of Status from a JSON string
status_instance = Status.from_json(json)
# print the JSON string representation of the object
print Status.to_json()

# convert the object into a dict
status_dict = status_instance.to_dict()
# create an instance of Status from a dict
status_from_dict = Status.from_dict(status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


