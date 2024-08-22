# AccessTokenRequest

Request object for an oAuth accesstoken code.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | **str** | Authorization code recieved from the oauth/authorize service. | [optional] 

## Example

```python
from sensorpush_api.models.access_token_request import AccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenRequest from a JSON string
access_token_request_instance = AccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print AccessTokenRequest.to_json()

# convert the object into a dict
access_token_request_dict = access_token_request_instance.to_dict()
# create an instance of AccessTokenRequest from a dict
access_token_request_from_dict = AccessTokenRequest.from_dict(access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


