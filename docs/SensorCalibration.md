# SensorCalibration

Calibration settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**humidity** | **float** | Humidity calibration | [optional] 
**temperature** | **float** | Temperature calibration | [optional] 

## Example

```python
from sensorpush_api.models.sensor_calibration import SensorCalibration

# TODO update the JSON string below
json = "{}"
# create an instance of SensorCalibration from a JSON string
sensor_calibration_instance = SensorCalibration.from_json(json)
# print the JSON string representation of the object
print SensorCalibration.to_json()

# convert the object into a dict
sensor_calibration_dict = sensor_calibration_instance.to_dict()
# create an instance of SensorCalibration from a dict
sensor_calibration_from_dict = SensorCalibration.from_dict(sensor_calibration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


