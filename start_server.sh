#!/bin/bash

eval "$(conda shell.bash hook)"
conda env create -f environment.yml
conda activate ml-inference

FLASK_ENV=development FLASK_APP=code/app.py flask run
