# SamplesRequest

Request object for samples.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Filters sensors by active &#x3D; (true|false). Defaults to true. | [optional] 
**bulk** | **bool** | Queries that return large results are truncated (see comments on Samples endpoint). Set this flag to true for large reports. The report request will be queued and processed within 24 hours. Upon completion, the primary account holder will recieve an email with a link for download. | [optional] 
**format** | **str** | Returns the results as the specified format (csv|json). Defaults to json | [optional] 
**limit** | **int** | Number of samples to return. | [optional] 
**measures** | **List[str]** | Specifies which measures to include (\&quot;temperature\&quot;|\&quot;humidity\&quot;|\&quot;vpd\&quot;|\&quot;barometric_pressure\&quot;|\&quot;dewpoint\&quot;). Note some measures are not available on older devices. | [optional] 
**sensors** | **List[str]** | Filters samples by sensor id. This will be the same id returned in the sensors api call. The parameter value must be a list of strings. Example: sensors: [\&quot;123.56789\&quot;]. | [optional] 
**start_time** | **str** | Start time to find samples (example: 2019-04-07T00:00:00-0400). Leave blank or zero to get the most recent samples. | [optional] 
**stop_time** | **str** | Stop time to find samples (example: 2019-04-07T10:30:00-0400). Leave blank or zero to get the most recent samples. | [optional] 
**tags** | **List[str]** | Filters samples by associated tags. | [optional] 

## Example

```python
from sensorpush_api.models.samples_request import SamplesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SamplesRequest from a JSON string
samples_request_instance = SamplesRequest.from_json(json)
# print the JSON string representation of the object
print SamplesRequest.to_json()

# convert the object into a dict
samples_request_dict = samples_request_instance.to_dict()
# create an instance of SamplesRequest from a dict
samples_request_from_dict = SamplesRequest.from_dict(samples_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


