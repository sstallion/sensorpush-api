# Gateway


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_alert** | **datetime** | Date last alert was sent | [optional] 
**last_seen** | **datetime** | Date the gateway was last seen | [optional] 
**message** | **str** | Detailed message associated with the gateway status. | [optional] 
**name** | **str** | Name associated with a gateway | [optional] 
**paired** | **str** | Gateway is paired with a bluetooth device | [optional] 
**tags** | [**Dict[str, Tags]**](Tags.md) | List of tags associated with this device | [optional] 
**version** | **str** | Version of Sensorpush software | [optional] 

## Example

```python
from sensorpush_api.models.gateway import Gateway

# TODO update the JSON string below
json = "{}"
# create an instance of Gateway from a JSON string
gateway_instance = Gateway.from_json(json)
# print the JSON string representation of the object
print Gateway.to_json()

# convert the object into a dict
gateway_dict = gateway_instance.to_dict()
# create an instance of Gateway from a dict
gateway_from_dict = Gateway.from_dict(gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


