# TokenResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | JWT oAuth access token. Pass this token to the data services via the http header &#x27;Authorization&#x27;. Example &#x27;Authorization&#x27; : &#x27;Bearer &lt;access token&gt;&#x27; | [optional] 
**expires_in** | **float** | TTL of the token in seconds | [optional] 
**refresh_token** | **str** | JWT oAuth refresh token. Pass this token to the token service to retrieve a new access token. | [optional] 
**token_type** | **str** | Type of token returned | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

