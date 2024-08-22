# SensorAlertsTemperature

alert settings for temperature

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Is enabled? | [optional] 
**max** | **float** | Max threshold for alert | [optional] 
**min** | **float** | Min threshold for alert | [optional] 

## Example

```python
from sensorpush_api.models.sensor_alerts_temperature import SensorAlertsTemperature

# TODO update the JSON string below
json = "{}"
# create an instance of SensorAlertsTemperature from a JSON string
sensor_alerts_temperature_instance = SensorAlertsTemperature.from_json(json)
# print the JSON string representation of the object
print SensorAlertsTemperature.to_json()

# convert the object into a dict
sensor_alerts_temperature_dict = sensor_alerts_temperature_instance.to_dict()
# create an instance of SensorAlertsTemperature from a dict
sensor_alerts_temperature_from_dict = SensorAlertsTemperature.from_dict(sensor_alerts_temperature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


