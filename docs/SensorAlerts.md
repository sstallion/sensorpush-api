# SensorAlerts

Alert settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**humidity** | [**SensorAlertsHumidity**](SensorAlertsHumidity.md) |  | [optional] 
**temperature** | [**SensorAlertsTemperature**](SensorAlertsTemperature.md) |  | [optional] 

## Example

```python
from sensorpush_api.models.sensor_alerts import SensorAlerts

# TODO update the JSON string below
json = "{}"
# create an instance of SensorAlerts from a JSON string
sensor_alerts_instance = SensorAlerts.from_json(json)
# print the JSON string representation of the object
print SensorAlerts.to_json()

# convert the object into a dict
sensor_alerts_dict = sensor_alerts_instance.to_dict()
# create an instance of SensorAlerts from a dict
sensor_alerts_from_dict = SensorAlerts.from_dict(sensor_alerts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


