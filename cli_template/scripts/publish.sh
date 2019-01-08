#!/usr/bin/env zsh
cd ..
rm ./dist/*
python3 setup.py bdist_wheel
sudo python3 -m twine upload dist/*