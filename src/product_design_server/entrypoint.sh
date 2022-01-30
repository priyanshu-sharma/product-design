#!/bin/sh
touch "server_config/local_settings.py"
python manage.py migrate
python manage.py loaddata fixtures/*.yaml
exec "$@"