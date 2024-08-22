# ReportsRequest

Request object for reports.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The directory path to perform this operation. | [optional] 

## Example

```python
from sensorpush_api.models.reports_request import ReportsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportsRequest from a JSON string
reports_request_instance = ReportsRequest.from_json(json)
# print the JSON string representation of the object
print ReportsRequest.to_json()

# convert the object into a dict
reports_request_dict = reports_request_instance.to_dict()
# create an instance of ReportsRequest from a dict
reports_request_from_dict = ReportsRequest.from_dict(reports_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


