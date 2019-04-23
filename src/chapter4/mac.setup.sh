#!/usr/bin/env bash

brew install mecab
brew install mecab-ipadic
brew install swig
brew install git curl xz

if [ -e $(which conda) ]; then
   pip install mecab-python3
   pip install pandas
   pip install matplotlib
fi
