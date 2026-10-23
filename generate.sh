#!/bin/sh
# Use OpenAPI Generator 7.8.0, matching .openapi-generator/VERSION.
# The REST and configuration templates preserve custom pool support and safe logging.
exec openapi-generator generate \
    --config options.json --generator-name python-pydantic-v1 \
    --template-dir templates \
    --input-spec https://api.sensorpush.com/api/v1/support/swagger/swagger-v1.json
