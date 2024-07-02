#!/bin/sh
exec swagger-codegen generate --lang python --config options.json \
    --input-spec https://api.sensorpush.com/api/v1/support/swagger/swagger-v1.json
