# TokenResponse

Response object for an oAuth authorization code.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | JWT oAuth access token. Pass this token to the data services via the http header &#39;Authorization&#39;. Example &#39;Authorization&#39; : &#39;Bearer &lt;access token&gt;&#39; | [optional] 
**expires_in** | **float** | TTL of the token in seconds | [optional] 
**refresh_token** | **str** | JWT oAuth refresh token. Pass this token to the token service to retrieve a new access token. | [optional] 
**token_type** | **str** | Type of token returned | [optional] 

## Example

```python
from sensorpush_api.models.token_response import TokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenResponse from a JSON string
token_response_instance = TokenResponse.from_json(json)
# print the JSON string representation of the object
print TokenResponse.to_json()

# convert the object into a dict
token_response_dict = token_response_instance.to_dict()
# create an instance of TokenResponse from a dict
token_response_from_dict = TokenResponse.from_dict(token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


