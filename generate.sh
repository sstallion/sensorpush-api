#!/bin/sh
exec openapi-generator generate \
    --config options.json --generator-name python-pydantic-v1 \
    --input-spec https://api.sensorpush.com/api/v1/support/swagger/swagger-v1.json
