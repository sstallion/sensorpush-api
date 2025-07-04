# sensorpush-api
This is a swagger definition for the SensorPush public REST API. Download the definition file [here](https://api.sensorpush.com/api/v1/support/swagger/swagger-v1.json).

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1.0.20240803
- Package version: 2.1.3
- Generator version: 7.8.0
- Build package: org.openapitools.codegen.languages.PythonPydanticV1ClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import sensorpush_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import sensorpush_api
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import sensorpush_api
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
    except ApiException as e:
        print("Exception when calling ApiApi->access_token: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.sensorpush.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiApi* | [**access_token**](docs/ApiApi.md#access_token) | **POST** /oauth/accesstoken | Request a temporary oAuth access code.
*ApiApi* | [**download**](docs/ApiApi.md#download) | **POST** /reports/download | Download bulk reports.
*ApiApi* | [**gateways**](docs/ApiApi.md#gateways) | **POST** /devices/gateways | Lists all gateways.
*ApiApi* | [**list**](docs/ApiApi.md#list) | **POST** /reports/list | Lists reports available for download.
*ApiApi* | [**oauth_authorize_post**](docs/ApiApi.md#oauth_authorize_post) | **POST** /oauth/authorize | Sign in and request an authorization code
*ApiApi* | [**root_post**](docs/ApiApi.md#root_post) | **POST** / | SensorPush API status
*ApiApi* | [**samples**](docs/ApiApi.md#samples) | **POST** /samples | Queries for sensor samples.
*ApiApi* | [**sensors**](docs/ApiApi.md#sensors) | **POST** /devices/sensors | Lists all sensors.
*ApiApi* | [**tags_response**](docs/ApiApi.md#tags_response) | **POST** /tags | Updates tags on devices.
*ApiApi* | [**token**](docs/ApiApi.md#token) | **POST** /oauth/token | oAuth 2.0 for authorization, access, and refresh tokens


## Documentation For Models

 - [AccessTokenRequest](docs/AccessTokenRequest.md)
 - [AccessTokenResponse](docs/AccessTokenResponse.md)
 - [AuthorizeRequest](docs/AuthorizeRequest.md)
 - [AuthorizeResponse](docs/AuthorizeResponse.md)
 - [Error](docs/Error.md)
 - [Gateway](docs/Gateway.md)
 - [GatewaysRequest](docs/GatewaysRequest.md)
 - [ListResponse](docs/ListResponse.md)
 - [ReportListing](docs/ReportListing.md)
 - [ReportsRequest](docs/ReportsRequest.md)
 - [Sample](docs/Sample.md)
 - [Samples](docs/Samples.md)
 - [SamplesRequest](docs/SamplesRequest.md)
 - [Sensor](docs/Sensor.md)
 - [SensorAlerts](docs/SensorAlerts.md)
 - [SensorAlertsHumidity](docs/SensorAlertsHumidity.md)
 - [SensorAlertsTemperature](docs/SensorAlertsTemperature.md)
 - [SensorCalibration](docs/SensorCalibration.md)
 - [SensorsRequest](docs/SensorsRequest.md)
 - [Status](docs/Status.md)
 - [Tags](docs/Tags.md)
 - [TagsRequest](docs/TagsRequest.md)
 - [TagsResponse](docs/TagsResponse.md)
 - [TokenRequest](docs/TokenRequest.md)
 - [TokenResponse](docs/TokenResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="oauth"></a>
### oauth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header
