#!/bin/sh

cd product_design_ui/
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
source ~/.profile
nvm install 17.6.0
nvm run default --version
node install