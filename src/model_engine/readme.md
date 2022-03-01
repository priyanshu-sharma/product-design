## Product Design Data Science Model

This service is responsible for all the data science related modelling.

# For installing dlib use following command

```
conda install -c conda-forge dlib
```

## Steps

```
pip install -r requirements.txt
pip install -r src/product_design_server/requirement.txt

pip uninstall tensorflow, karpe

pip install tensorflow-gpu==1.15.2

export CUDA_HOME=/usr/local/cuda
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64
export PATH=$PATH:$CUDA_HOME/bin

nvcc --version
```