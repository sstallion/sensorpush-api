# Sample

This represents one observation recorded by a given sensor. The fields listed below (except for observed) will be populated base on the measures parameter specified in the request, and if the given sensor version collects that particular measure. For example, barometric_pressure is not available in HT1 series sensors, and thus will not be reported.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**altitude** | **float** | Value unit is feet (ft) | [optional] 
**barometric_pressure** | **float** | Value unit is inch of mercury (inHg) | [optional] 
**dewpoint** | **float** | Value unit is farenheit (°F) | [optional] 
**humidity** | **float** | Value unit is percentage (%) | [optional] 
**observed** | **datetime** | Date time when sample was observed. | [optional] 
**tags** | [**Dict[str, Tags]**](Tags.md) | List of tags associated with this device | [optional] 
**temperature** | **float** | Value unit is farenheit (°F) | [optional] 
**vpd** | **float** | Value unit is kPa | [optional] 

## Example

```python
from sensorpush_api.models.sample import Sample

# TODO update the JSON string below
json = "{}"
# create an instance of Sample from a JSON string
sample_instance = Sample.from_json(json)
# print the JSON string representation of the object
print Sample.to_json()

# convert the object into a dict
sample_dict = sample_instance.to_dict()
# create an instance of Sample from a dict
sample_from_dict = Sample.from_dict(sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


