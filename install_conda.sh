wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p /software/miniconda && rm Miniconda3-latest-Linux-x86_64.sh
eval "$(/software/miniconda/bin/conda shell.bash hook)"
conda install mamba -c conda-forge
