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
> AccessTokenResponse access_token(access_token_request)

Request a temporary oAuth access code.

This is a simplified version of oAuth in that it only supports accesstokens and does not require a client_id. See the endpoint '/api/v1/oauth/token' for the more advanced oAuth endpoint. Once a user has been authorized, the client app will call this service to receive the access token. The access token will be used to grant permissions to data stores. An access token expires every hour. After that, request a new access token.

### Example

```python
import time
import os
import sensorpush_api
from sensorpush_api.models.access_token_request import AccessTokenRequest
from sensorpush_api.models.access_token_response import AccessTokenResponse
from sensorpush_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sensorpush.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorpush_api.Configuration(
    host = "https://api.sensorpush.com/api/v1"
)


# Enter a context with an instance of the API client
async with sensorpush_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensorpush_api.ApiApi(api_client)
    access_token_request = sensorpush_api.AccessTokenRequest() # AccessTokenRequest | 

    try:
        # Request a temporary oAuth access code.
        api_response = await api_instance.access_token(access_token_request)
        print("The response of ApiApi->access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->access_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token_request** | [**AccessTokenRequest**](AccessTokenRequest.md)|  | 

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download**
> download(reports_request)

Download bulk reports.

This service will download bulk generated reports.

### Example

* Api Key Authentication (oauth):
```python
import time
import os
import sensorpush_api
from sensorpush_api.models.reports_request import ReportsRequest
from sensorpush_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sensorpush.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorpush_api.Configuration(
    host = "https://api.sensorpush.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: oauth
configuration.api_key['oauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['oauth'] = 'Bearer'

# Enter a context with an instance of the API client
async with sensorpush_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensorpush_api.ApiApi(api_client)
    reports_request = sensorpush_api.ReportsRequest() # ReportsRequest | 

    try:
        # Download bulk reports.
        await api_instance.download(reports_request)
    except Exception as e:
        print("Exception when calling ApiApi->download: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reports_request** | [**ReportsRequest**](ReportsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  -  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateways**
> Dict[str, Gateway] gateways(gateways_request)

Lists all gateways.

This service will return an inventory of all registered gateways for this account.

### Example

* Api Key Authentication (oauth):
```python
import time
import os
import sensorpush_api
from sensorpush_api.models.gateway import Gateway
from sensorpush_api.models.gateways_request import GatewaysRequest
from sensorpush_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sensorpush.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorpush_api.Configuration(
    host = "https://api.sensorpush.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: oauth
configuration.api_key['oauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['oauth'] = 'Bearer'

# Enter a context with an instance of the API client
async with sensorpush_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensorpush_api.ApiApi(api_client)
    gateways_request = sensorpush_api.GatewaysRequest() # GatewaysRequest | 

    try:
        # Lists all gateways.
        api_response = await api_instance.gateways(gateways_request)
        print("The response of ApiApi->gateways:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->gateways: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateways_request** | [**GatewaysRequest**](GatewaysRequest.md)|  | 

### Return type

[**Dict[str, Gateway]**](Gateway.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  -  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListResponse list(reports_request)

Lists reports available for download.

This service will list all bulk generated reports available to download.

### Example

* Api Key Authentication (oauth):
```python
import time
import os
import sensorpush_api
from sensorpush_api.models.list_response import ListResponse
from sensorpush_api.models.reports_request import ReportsRequest
from sensorpush_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sensorpush.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorpush_api.Configuration(
    host = "https://api.sensorpush.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: oauth
configuration.api_key['oauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['oauth'] = 'Bearer'

# Enter a context with an instance of the API client
async with sensorpush_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensorpush_api.ApiApi(api_client)
    reports_request = sensorpush_api.ReportsRequest() # ReportsRequest | 

    try:
        # Lists reports available for download.
        api_response = await api_instance.list(reports_request)
        print("The response of ApiApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reports_request** | [**ReportsRequest**](ReportsRequest.md)|  | 

### Return type

[**ListResponse**](ListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  -  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_authorize_post**
> AuthorizeResponse oauth_authorize_post(authorize_request)

Sign in and request an authorization code

Sign into the SensorPush API via redirect to SensorPush logon. Then signin using email/password, or an api id. This service will return an oAuth authorization code that can be exchanged for an oAuth access token using the accesstoken service.

### Example

```python
import time
import os
import sensorpush_api
from sensorpush_api.models.authorize_request import AuthorizeRequest
from sensorpush_api.models.authorize_response import AuthorizeResponse
from sensorpush_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sensorpush.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorpush_api.Configuration(
    host = "https://api.sensorpush.com/api/v1"
)


# Enter a context with an instance of the API client
async with sensorpush_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensorpush_api.ApiApi(api_client)
    authorize_request = sensorpush_api.AuthorizeRequest() # AuthorizeRequest | 

    try:
        # Sign in and request an authorization code
        api_response = await api_instance.oauth_authorize_post(authorize_request)
        print("The response of ApiApi->oauth_authorize_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->oauth_authorize_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorize_request** | [**AuthorizeRequest**](AuthorizeRequest.md)|  | 

### Return type

[**AuthorizeResponse**](AuthorizeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**403** | invalid user |  -  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_post**
> Status root_post()

SensorPush API status

This service is used as a simple method for clients to verify they can connect to the API.

### Example

```python
import time
import os
import sensorpush_api
from sensorpush_api.models.status import Status
from sensorpush_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sensorpush.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorpush_api.Configuration(
    host = "https://api.sensorpush.com/api/v1"
)


# Enter a context with an instance of the API client
async with sensorpush_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensorpush_api.ApiApi(api_client)

    try:
        # SensorPush API status
        api_response = await api_instance.root_post()
        print("The response of ApiApi->root_post:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samples**
> Samples samples(samples_request)

Queries for sensor samples.

This service is used to query for samples persisted by the sensors. The service will return all samples after the given parameter {startTime}. Queries that produce greater than ~5MB of data will be truncated. If results return truncated, consider using the sensors parameter list. This will allow you to retrieve more data per sensor. For example, a query that does not provide a sensor list, will attempt to return equal amounts of data for all sensors (i.e. ~5MB divided by N sensors). However, if one sensor is specified, than all ~5MB will be filled for that one sensor (i.e. ~5MB divided by 1). Another option is to paginate through results by time, using {startTime} as the last date in your previous page of results.

### Example

* Api Key Authentication (oauth):
```python
import time
import os
import sensorpush_api
from sensorpush_api.models.samples import Samples
from sensorpush_api.models.samples_request import SamplesRequest
from sensorpush_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sensorpush.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorpush_api.Configuration(
    host = "https://api.sensorpush.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: oauth
configuration.api_key['oauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['oauth'] = 'Bearer'

# Enter a context with an instance of the API client
async with sensorpush_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensorpush_api.ApiApi(api_client)
    samples_request = sensorpush_api.SamplesRequest() # SamplesRequest | 

    try:
        # Queries for sensor samples.
        api_response = await api_instance.samples(samples_request)
        print("The response of ApiApi->samples:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->samples: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **samples_request** | [**SamplesRequest**](SamplesRequest.md)|  | 

### Return type

[**Samples**](Samples.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  -  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors**
> Dict[str, Sensor] sensors(sensors_request)

Lists all sensors.

This service will return an inventory of all registered sensors for this account.

### Example

* Api Key Authentication (oauth):
```python
import time
import os
import sensorpush_api
from sensorpush_api.models.sensor import Sensor
from sensorpush_api.models.sensors_request import SensorsRequest
from sensorpush_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sensorpush.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorpush_api.Configuration(
    host = "https://api.sensorpush.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: oauth
configuration.api_key['oauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['oauth'] = 'Bearer'

# Enter a context with an instance of the API client
async with sensorpush_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensorpush_api.ApiApi(api_client)
    sensors_request = sensorpush_api.SensorsRequest() # SensorsRequest | 

    try:
        # Lists all sensors.
        api_response = await api_instance.sensors(sensors_request)
        print("The response of ApiApi->sensors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->sensors: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensors_request** | [**SensorsRequest**](SensorsRequest.md)|  | 

### Return type

[**Dict[str, Sensor]**](Sensor.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  -  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_response**
> TagsResponse tags_response(tags_request)

Updates tags on devices.

This service allows users to add tags to devices.

### Example

* Api Key Authentication (oauth):
```python
import time
import os
import sensorpush_api
from sensorpush_api.models.tags_request import TagsRequest
from sensorpush_api.models.tags_response import TagsResponse
from sensorpush_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sensorpush.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorpush_api.Configuration(
    host = "https://api.sensorpush.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: oauth
configuration.api_key['oauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['oauth'] = 'Bearer'

# Enter a context with an instance of the API client
async with sensorpush_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensorpush_api.ApiApi(api_client)
    tags_request = sensorpush_api.TagsRequest() # TagsRequest | 

    try:
        # Updates tags on devices.
        api_response = await api_instance.tags_response(tags_request)
        print("The response of ApiApi->tags_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->tags_response: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags_request** | [**TagsRequest**](TagsRequest.md)|  | 

### Return type

[**TagsResponse**](TagsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  -  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token**
> TokenResponse token(token_request)

oAuth 2.0 for authorization, access, and refresh tokens

This is a more advanced endpoint that implements the oAuth 2.0 specification. Supports grant_types: password, refresh_token, and access_token. If grant_type is null an access_token will be returned. (see <a href=\"https://oauth.net/2/grant-types/\">oAuth Grant Types</a>). A client_id is required for this endpoint. Contact support@sensorpush.com to register your application and recieve a client_id.

### Example

```python
import time
import os
import sensorpush_api
from sensorpush_api.models.token_request import TokenRequest
from sensorpush_api.models.token_response import TokenResponse
from sensorpush_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sensorpush.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorpush_api.Configuration(
    host = "https://api.sensorpush.com/api/v1"
)


# Enter a context with an instance of the API client
async with sensorpush_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensorpush_api.ApiApi(api_client)
    token_request = sensorpush_api.TokenRequest() # TokenRequest | 

    try:
        # oAuth 2.0 for authorization, access, and refresh tokens
        api_response = await api_instance.token(token_request)
        print("The response of ApiApi->token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_request** | [**TokenRequest**](TokenRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

