# AccessTokenResponse

Response object for an oAuth authorization code.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accesstoken** | **str** | JWT oAuth accesstoken. Pass this code to the data services via the http header &#39;Authorization&#39;. Example &#39;Authorization&#39; : &#39;Bearer &lt;access token&gt;&#39; | [optional] 

## Example

```python
from sensorpush_api.models.access_token_response import AccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenResponse from a JSON string
access_token_response_instance = AccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print AccessTokenResponse.to_json()

# convert the object into a dict
access_token_response_dict = access_token_response_instance.to_dict()
# create an instance of AccessTokenResponse from a dict
access_token_response_from_dict = AccessTokenResponse.from_dict(access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


