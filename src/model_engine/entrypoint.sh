#!/bin/sh
pip uninstall --yes tensorflow
pip install -r requirements.txt

mkdir src/model_engine/media
mkdir src/model_engine/media/handbag
mkdir src/model_engine/media/jeans
mkdir src/model_engine/media/handbag/models
mkdir src/model_engine/media/handbag/images

cp /content/gdrive/MyDrive/Colab\ Notebooks/generator_model.pkl  /content/product-design/src/model_engine/media/handbag/models/

echo "export CUDA_HOME=/usr/local/cuda" >> ~/.bashrc
echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64" >> ~/.bashrc
echo "export PATH=$PATH:$CUDA_HOME/bin" >> ~/.bashrc

source ~/.bashrc

nvcc --version