#!/bin/sh

# Redis Setup
sudo apt-get update
sudo apt-get install redis-server nano vim pgcli
echo 'supervised systemd' >> /etc/redis/redis.conf
# redis-server

# RabbitMQ Setup
sudo apt-get install rabbitmq-server
# rabbitmq-server

# Postgres Setup
sudo apt-get install postgresql postgresql-contrib
echo 'listen_addresses = "*"' >> /etc/postgresql/10/main/postgresql.conf
sudo service postgresql start
sudo -u postgres createdb product_design
# sudo -u postgres psql
# create user pd_admin with encrypted password 'password';
# grant all privileges on database product_design to pd_admin;


bash src/model_engine/entrypoint.sh
# bash src/product_design_server/entrypoint.sh