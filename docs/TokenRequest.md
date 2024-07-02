# TokenRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Client Id assigned to 3rd party applications. Contact support@sensorpush.com to register you app. | [optional] 
**client_secret** | **str** | Password associated with the client_id | [optional] 
**code** | **str** | This can be an authorization, access, or refresh token. Depending on which grant_type you are using. | [optional] 
**grant_type** | **str** | Accepted values are password, refresh_token, and access_token | [optional] 
**password** | **str** | User&#x27;s password | [optional] 
**redirect_uri** | **str** | Redirection url to the 3rd party application once the user has signed into the sensorpush logon. This value should be URL encoded. | [optional] 
**refresh_token** | **str** | Refresh token used to request new access tokens. | [optional] 
**username** | **str** | Email of the user to sign in. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

