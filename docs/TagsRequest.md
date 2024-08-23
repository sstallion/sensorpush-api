# TagsRequest

Map of registered devices and their tags.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sensors** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from sensorpush_api.models.tags_request import TagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TagsRequest from a JSON string
tags_request_instance = TagsRequest.from_json(json)
# print the JSON string representation of the object
print TagsRequest.to_json()

# convert the object into a dict
tags_request_dict = tags_request_instance.to_dict()
# create an instance of TagsRequest from a dict
tags_request_from_dict = TagsRequest.from_dict(tags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


