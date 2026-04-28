#!/bin/bash
  set -e

  apt-get install -y sudo

  cd /workspace
  curl -fsSL https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh
  bash miniconda.sh -b -p /workspace/miniconda
  rm miniconda.sh
  /workspace/miniconda/bin/conda init bash