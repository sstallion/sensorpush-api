# sensorpush_api.ApiApi

All URIs are relative to *https://api.sensorpush.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**access_token**](ApiApi.md#access_token) | **POST** /oauth/accesstoken | Request a temporary oAuth access code.
[**download**](ApiApi.md#download) | **POST** /reports/download | Download bulk reports.
[**gateways**](ApiApi.md#gateways) | **POST** /devices/gateways | Lists all gateways.
[**list**](ApiApi.md#list) | **POST** /reports/list | Lists reports available for download.
[**oauth_authorize_post**](ApiApi.md#oauth_authorize_post) | **POST** /oauth/authorize | Sign in and request an authorization code
[**root_post**](ApiApi.md#root_post) | **POST** / | SensorPush API status
[**samples**](ApiApi.md#samples) | **POST** /samples | Queries for sensor samples.
[**sensors**](ApiApi.md#sensors) | **POST** /devices/sensors | Lists all sensors.
[**tags_response**](ApiApi.md#tags_response) | **POST** /tags | Updates tags on devices.
[**token**](ApiApi.md#token) | **POST** /oauth/token | oAuth 2.0 for authorization, access, and refresh tokens

# **access_token**
> AccessTokenResponse access_token(body)

Request a temporary oAuth access code.

This is a simplified version of oAuth in that it only supports accesstokens and does not require a client_id. See the endpoint '/api/v1/oauth/token' for the more advanced oAuth endpoint. Once a user has been authorized, the client app will call this service to receive the access token. The access token will be used to grant permissions to data stores. An access token expires every hour. After that, request a new access token.

### Example
```python
from __future__ import print_function
import time
import sensorpush_api
from sensorpush_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sensorpush_api.ApiApi()
body = sensorpush_api.AccessTokenRequest() # AccessTokenRequest | 

try:
    # Request a temporary oAuth access code.
    api_response = api_instance.access_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessTokenRequest**](AccessTokenRequest.md)|  | 

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download**
> download(body)

Download bulk reports.

This service will download bulk generated reports.

### Example
```python
from __future__ import print_function
import time
import sensorpush_api
from sensorpush_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = sensorpush_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = sensorpush_api.ApiApi(sensorpush_api.ApiClient(configuration))
body = sensorpush_api.ReportsRequest() # ReportsRequest | 

try:
    # Download bulk reports.
    api_instance.download(body)
except ApiException as e:
    print("Exception when calling ApiApi->download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportsRequest**](ReportsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateways**
> Gateways gateways(body)

Lists all gateways.

This service will return an inventory of all registered gateways for this account.

### Example
```python
from __future__ import print_function
import time
import sensorpush_api
from sensorpush_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = sensorpush_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = sensorpush_api.ApiApi(sensorpush_api.ApiClient(configuration))
body = sensorpush_api.GatewaysRequest() # GatewaysRequest | 

try:
    # Lists all gateways.
    api_response = api_instance.gateways(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->gateways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewaysRequest**](GatewaysRequest.md)|  | 

### Return type

[**Gateways**](Gateways.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListResponse list(body)

Lists reports available for download.

This service will list all bulk generated reports available to download.

### Example
```python
from __future__ import print_function
import time
import sensorpush_api
from sensorpush_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = sensorpush_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = sensorpush_api.ApiApi(sensorpush_api.ApiClient(configuration))
body = sensorpush_api.ReportsRequest() # ReportsRequest | 

try:
    # Lists reports available for download.
    api_response = api_instance.list(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportsRequest**](ReportsRequest.md)|  | 

### Return type

[**ListResponse**](ListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_authorize_post**
> AuthorizeResponse oauth_authorize_post(body)

Sign in and request an authorization code

Sign into the SensorPush API via redirect to SensorPush logon. Then signin using email/password, or an api id. This service will return an oAuth authorization code that can be exchanged for an oAuth access token using the accesstoken service.

### Example
```python
from __future__ import print_function
import time
import sensorpush_api
from sensorpush_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sensorpush_api.ApiApi()
body = sensorpush_api.AuthorizeRequest() # AuthorizeRequest | 

try:
    # Sign in and request an authorization code
    api_response = api_instance.oauth_authorize_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->oauth_authorize_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorizeRequest**](AuthorizeRequest.md)|  | 

### Return type

[**AuthorizeResponse**](AuthorizeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_post**
> Status root_post()

SensorPush API status

This service is used as a simple method for clients to verify they can connect to the API.

### Example
```python
from __future__ import print_function
import time
import sensorpush_api
from sensorpush_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sensorpush_api.ApiApi()

try:
    # SensorPush API status
    api_response = api_instance.root_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->root_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samples**
> Samples samples(body)

Queries for sensor samples.

This service is used to query for samples persisted by the sensors. The service will return all samples after the given parameter {startTime}. Queries that produce greater than ~5MB of data will be truncated. If results return truncated, consider using the sensors parameter list. This will allow you to retrieve more data per sensor. For example, a query that does not provide a sensor list, will attempt to return equal amounts of data for all sensors (i.e. ~5MB divided by N sensors). However, if one sensor is specified, than all ~5MB will be filled for that one sensor (i.e. ~5MB divided by 1). Another option is to paginate through results by time, using {startTime} as the last date in your previous page of results.

### Example
```python
from __future__ import print_function
import time
import sensorpush_api
from sensorpush_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = sensorpush_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = sensorpush_api.ApiApi(sensorpush_api.ApiClient(configuration))
body = sensorpush_api.SamplesRequest() # SamplesRequest | 

try:
    # Queries for sensor samples.
    api_response = api_instance.samples(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SamplesRequest**](SamplesRequest.md)|  | 

### Return type

[**Samples**](Samples.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors**
> Sensors sensors(body)

Lists all sensors.

This service will return an inventory of all registered sensors for this account.

### Example
```python
from __future__ import print_function
import time
import sensorpush_api
from sensorpush_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = sensorpush_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = sensorpush_api.ApiApi(sensorpush_api.ApiClient(configuration))
body = sensorpush_api.SensorsRequest() # SensorsRequest | 

try:
    # Lists all sensors.
    api_response = api_instance.sensors(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->sensors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SensorsRequest**](SensorsRequest.md)|  | 

### Return type

[**Sensors**](Sensors.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_response**
> TagsResponse tags_response(body)

Updates tags on devices.

This service allows users to add tags to devices.

### Example
```python
from __future__ import print_function
import time
import sensorpush_api
from sensorpush_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = sensorpush_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = sensorpush_api.ApiApi(sensorpush_api.ApiClient(configuration))
body = sensorpush_api.TagsRequest() # TagsRequest | 

try:
    # Updates tags on devices.
    api_response = api_instance.tags_response(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->tags_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TagsRequest**](TagsRequest.md)|  | 

### Return type

[**TagsResponse**](TagsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token**
> TokenResponse token(body)

oAuth 2.0 for authorization, access, and refresh tokens

This is a more advanced endpoint that implements the oAuth 2.0 specification. Supports grant_types: password, refresh_token, and access_token. If grant_type is null an access_token will be returned. (see <a href=\"https://oauth.net/2/grant-types/\">oAuth Grant Types</a>). A client_id is required for this endpoint. Contact support@sensorpush.com to register your application and recieve a client_id.

### Example
```python
from __future__ import print_function
import time
import sensorpush_api
from sensorpush_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sensorpush_api.ApiApi()
body = sensorpush_api.TokenRequest() # TokenRequest | 

try:
    # oAuth 2.0 for authorization, access, and refresh tokens
    api_response = api_instance.token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenRequest**](TokenRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

