# ReportListing


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_modified** | **datetime** | Date file was last modified | [optional] 
**name** | **str** | Name of the file | [optional] 
**size** | **str** | File size | [optional] 

## Example

```python
from sensorpush_api.models.report_listing import ReportListing

# TODO update the JSON string below
json = "{}"
# create an instance of ReportListing from a JSON string
report_listing_instance = ReportListing.from_json(json)
# print the JSON string representation of the object
print ReportListing.to_json()

# convert the object into a dict
report_listing_dict = report_listing_instance.to_dict()
# create an instance of ReportListing from a dict
report_listing_from_dict = ReportListing.from_dict(report_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


