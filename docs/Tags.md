# Tags

Map of registered devices and their tags.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateways** | **Dict[str, List[str]]** |  | [optional] 
**sensors** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from sensorpush_api.models.tags import Tags

# TODO update the JSON string below
json = "{}"
# create an instance of Tags from a JSON string
tags_instance = Tags.from_json(json)
# print the JSON string representation of the object
print Tags.to_json()

# convert the object into a dict
tags_dict = tags_instance.to_dict()
# create an instance of Tags from a dict
tags_from_dict = Tags.from_dict(tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


