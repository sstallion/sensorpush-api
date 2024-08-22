# Sensor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Is the sensor active? | [optional] 
**address** | **str** | MAC address | [optional] 
**alerts** | [**SensorAlerts**](SensorAlerts.md) |  | [optional] 
**battery_voltage** | **float** | Current battery voltage | [optional] 
**calibration** | [**SensorCalibration**](SensorCalibration.md) |  | [optional] 
**device_id** | **str** | Short device Id | [optional] 
**id** | **str** | Long device Id | [optional] 
**name** | **str** | Name of the sensor sensor | [optional] 
**rssi** | **float** | Wireless signal strength in dB at last reading | [optional] 
**tags** | [**Dict[str, Tags]**](Tags.md) | List of tags associated with this device | [optional] 
**type** | **str** | Type of device hardward | [optional] 

## Example

```python
from sensorpush_api.models.sensor import Sensor

# TODO update the JSON string below
json = "{}"
# create an instance of Sensor from a JSON string
sensor_instance = Sensor.from_json(json)
# print the JSON string representation of the object
print Sensor.to_json()

# convert the object into a dict
sensor_dict = sensor_instance.to_dict()
# create an instance of Sensor from a dict
sensor_from_dict = Sensor.from_dict(sensor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


