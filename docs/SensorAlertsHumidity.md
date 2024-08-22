# SensorAlertsHumidity

alert settings for humidity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Is enabled? | [optional] 
**max** | **float** | Max threshold for alert | [optional] 
**min** | **float** | Min threshold for alert | [optional] 

## Example

```python
from sensorpush_api.models.sensor_alerts_humidity import SensorAlertsHumidity

# TODO update the JSON string below
json = "{}"
# create an instance of SensorAlertsHumidity from a JSON string
sensor_alerts_humidity_instance = SensorAlertsHumidity.from_json(json)
# print the JSON string representation of the object
print SensorAlertsHumidity.to_json()

# convert the object into a dict
sensor_alerts_humidity_dict = sensor_alerts_humidity_instance.to_dict()
# create an instance of SensorAlertsHumidity from a dict
sensor_alerts_humidity_from_dict = SensorAlertsHumidity.from_dict(sensor_alerts_humidity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


