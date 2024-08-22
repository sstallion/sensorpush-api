# Samples

Map of registered SensorPush sensors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_time** | **datetime** | ISO date time of the last sample returned. Use this as the start_ts to query for the next page of samples. | [optional] 
**sensors** | **Dict[str, List[Sample]]** | Map of sensors and the associated samples. | [optional] 
**status** | **str** | Message describing state of the api call. | [optional] 
**total_samples** | **float** | Total number of samples across all sensors | [optional] 
**total_sensors** | **float** | Total number of sensors returned | [optional] 
**truncated** | **bool** | The query returned too many results, causing the sample list to be truncated. Consider adjusting the limit or startTime parameters. | [optional] 

## Example

```python
from sensorpush_api.models.samples import Samples

# TODO update the JSON string below
json = "{}"
# create an instance of Samples from a JSON string
samples_instance = Samples.from_json(json)
# print the JSON string representation of the object
print Samples.to_json()

# convert the object into a dict
samples_dict = samples_instance.to_dict()
# create an instance of Samples from a dict
samples_from_dict = Samples.from_dict(samples_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


