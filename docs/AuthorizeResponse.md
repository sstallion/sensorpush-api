# AuthorizeResponse

Response object for an oAuth authorization code.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | **str** | JWT oAuth authorization code. Pass this code to the oauth/accesscode service to request an access token. The [jwt](https://jwt.io/) website has a useful jwt viewer. | [optional] 

## Example

```python
from sensorpush_api.models.authorize_response import AuthorizeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizeResponse from a JSON string
authorize_response_instance = AuthorizeResponse.from_json(json)
# print the JSON string representation of the object
print AuthorizeResponse.to_json()

# convert the object into a dict
authorize_response_dict = authorize_response_instance.to_dict()
# create an instance of AuthorizeResponse from a dict
authorize_response_from_dict = AuthorizeResponse.from_dict(authorize_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


