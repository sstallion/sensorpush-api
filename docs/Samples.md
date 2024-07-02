# Samples

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_time** | **datetime** | ISO date time of the last sample returned. Use this as the start_ts to query for the next page of samples. | [optional] 
**sensors** | **dict(str, list[Sample])** | Map of sensors and the associated samples. | [optional] 
**status** | **str** | Message describing state of the api call. | [optional] 
**total_samples** | **float** | Total number of samples across all sensors | [optional] 
**total_sensors** | **float** | Total number of sensors returned | [optional] 
**truncated** | **bool** | The query returned too many results, causing the sample list to be truncated. Consider adjusting the limit or startTime parameters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

