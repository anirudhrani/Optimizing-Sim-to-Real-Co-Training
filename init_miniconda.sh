source ~/.bashrc

/workspace/miniconda/bin/conda info --envs

/workspace/miniconda/bin/conda install -y -c conda-forge ffmpeg

echo "Base setup done"

echo "Cloning Repo"

git clone https://github.com/anirudhrani/Optimizing-Sim-to-Real-Co-Training.git
