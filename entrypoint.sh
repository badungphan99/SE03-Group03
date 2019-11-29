#!/bin/bash

set -e

>&2 echo "Grant permission for folders"
chmod -R 777 /app/WebData

python3 ./manage.py migrate

exec "$@"