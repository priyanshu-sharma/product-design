#!/bin/sh

cd src/product_design_ui/product_design_ui/
mkdir public/handbag
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
source ~/.bashrc
sleep 4
nvm --version
nvm install 17.6.0
sleep 4
nvm run default --version
node --version
npm install
npm install react-bootstrap bootstrap
sleep 4
npm start