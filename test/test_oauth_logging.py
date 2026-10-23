"""OAuth logging regressions using an in-memory HTTP transport only."""

import asyncio
import json
import logging
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from sensorpush_api import (
    AccessTokenRequest,
    ApiApi,
    ApiClient,
    AuthorizeRequest,
    Configuration,
    TokenRequest,
)
from sensorpush_api.exceptions import ApiException


OAUTH_CASES = [
    (
        'oauth_authorize_post',
        '/oauth/authorize',
        AuthorizeRequest(email='synthetic@example.invalid', password='synthetic-password'),
        {'authorization': 'synthetic-authorization-code'},
    ),
    (
        'access_token',
        '/oauth/accesstoken',
        AccessTokenRequest(authorization='synthetic-authorization-code'),
        {'accesstoken': 'synthetic-access-token'},
    ),
    (
        'token',
        '/oauth/token',
        TokenRequest(),
        {'access_token': 'synthetic-access-token', 'refresh_token': 'synthetic-refresh-token'},
    ),
]


def make_client(body, status=200):
    """Use the real API and REST clients without creating a network session."""
    response = SimpleNamespace(
        status=status,
        reason='OK' if status == 200 else 'Synthetic failure',
        headers={'content-type': 'application/json', 'x-request-id': 'synthetic-request'},
        read=AsyncMock(return_value=body),
    )
    configuration = Configuration(
        host='https://sensorpush.invalid/api/v1',
        pool_manager=SimpleNamespace(
            request=AsyncMock(return_value=response),
            close=AsyncMock(),
        ),
    )
    return ApiClient(configuration), response


def assert_safe_logs(caplog, status):
    for secret in (
        'synthetic-authorization-code',
        'synthetic-access-token',
        'synthetic-refresh-token',
        'synthetic-password',
    ):
        assert secret not in caplog.text
    assert 'response status: %s' % status in caplog.text


@pytest.mark.parametrize('method,path,request_model,payload', OAUTH_CASES)
def test_oauth_success_does_not_log_credentials(caplog, method, path, request_model, payload):
    caplog.set_level(logging.DEBUG, logger='sensorpush_api.rest')
    client, response = make_client(json.dumps(payload).encode())

    async def call():
        async with client:
            return await getattr(ApiApi(client), method)(request_model)

    result = asyncio.run(call())

    for field, value in payload.items():
        assert getattr(result, field) == value
    sent = client.configuration.pool_manager.request.call_args.kwargs
    assert sent['url'] == client.configuration.host + path
    assert sent['method'] == 'POST'
    assert json.loads(sent['data']) == request_model.to_dict()
    response.read.assert_awaited_once_with()
    client.configuration.pool_manager.close.assert_awaited_once_with()
    assert_safe_logs(caplog, 200)


@pytest.mark.parametrize('method,path,request_model,payload', OAUTH_CASES)
@pytest.mark.parametrize('status', [400, 500])
@pytest.mark.parametrize('malformed', [False, True])
def test_oauth_error_does_not_log_body(caplog, method, path, request_model, payload,
                                      status, malformed):
    caplog.set_level(logging.DEBUG, logger='sensorpush_api.rest')
    body = json.dumps(payload) if not malformed else 'invalid JSON: ' + ' '.join(payload.values())
    client, response = make_client(body.encode(), status)

    async def call():
        async with client:
            return await getattr(ApiApi(client), method)(request_model)

    with pytest.raises(ApiException) as exc_info:
        asyncio.run(call())

    assert exc_info.value.status == status
    assert exc_info.value.reason == response.reason
    assert exc_info.value.headers == response.headers
    assert exc_info.value.body == body
    assert_safe_logs(caplog, status)


def test_unread_oauth_response_is_unchanged(caplog):
    caplog.set_level(logging.DEBUG, logger='sensorpush_api.rest')
    body = b'{"authorization": "synthetic-authorization-code"}'
    client, response = make_client(body)

    async def call():
        async with client:
            return await client.rest_client.post_request(
                client.configuration.host + '/oauth/authorize', _preload_content=False
            )

    assert asyncio.run(call()) is response
    response.read.assert_not_awaited()
    assert 'synthetic-authorization-code' not in caplog.text


def test_non_oauth_response_keeps_data_and_status_diagnostic(caplog):
    caplog.set_level(logging.DEBUG, logger='sensorpush_api.rest')
    body = b'{"status": "healthy"}'
    client, response = make_client(body)

    async def call():
        async with client:
            return await client.rest_client.post_request(client.configuration.host + '/')

    result = asyncio.run(call())

    assert result.data == body
    assert result.status == response.status
    assert result.getheaders() == response.headers
    assert 'healthy' not in caplog.text
    assert 'response status: 200' in caplog.text


def test_default_pool_manager_can_be_created_and_closed():
    """Configuration and REST must also work without an injected transport."""
    async def call():
        async with ApiClient(Configuration()) as client:
            pool_manager = client.rest_client.pool_manager
            assert not pool_manager.closed
        assert pool_manager.closed

    asyncio.run(call())
