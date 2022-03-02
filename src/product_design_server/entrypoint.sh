#!/bin/sh
touch "src/product_design_server/server_config/local_settings.py"
python src/product_design_server/manage.py migrate
python src/product_design_server/manage.py loaddata src/product_design_server/fixtures/*.yaml
exec "$@"