# Testing MLOps Skills

This repository contains a Docker-based inference API for a machine learning model, built using FastAPI. The API is designed to handle requests for predictions and includes endpoints for health checks and model information. 

## Task description

The goal of this task is to build a working API that hosts a model that generates predictions in response to a CSV file. To achieve this, you'll need to create a model training script. You can use the code from the previous task or create a much simpler model; the goal isn't to achieve the best possible performance for this model. The training script (`train.py`) should save the model to a directory named `model` in a file named `model.onnx` (i.e., the full path would be `model/model.onnx`). For the model training, use data from previous task (`train_data.csv` and `train_labels.csv`). Next, you'll need to complete the `inference/api.py` file, which transforms the data sent to the API, loads the model, performs inference, and returns the result. The appropriate libraries are already imported in the file, but you can of course modify them as needed. We're assuming the file sent to the API contains only one line — a sample file (`test_api_data.csv`) is located in the `tests` directory. After writing the missing code, you should be able to build a Docker container and run it to make the API accessible. You can then run a test by issuing the "make test" command. All places where you need to insert your own code are marked with the [ADD] tag. If you feel any other code modifications are required, you can make them as needed, but please describe them when submitting your assignment.


## Candidate Tasks

The candidate should demonstrate their MLOps skills by completing the following tasks:

1. **Understand the provided code and Docker setup.**
2. **Add requirements to `pyproject.toml`** to section with **docker** optional dependencies .
3. **Fill gaps in `train.py` script** that trains a model and saves it in the `model` directory (in ONNX format).
4. **Fill gaps in `inference/api.py`** to handle model loading and prediction requests. Use the `InputProcessor` class to preprocess input data, if needed.


## Important Notes
- Environment setup:
  - run ```make build_env```
  - Create `data` directory with a sample dataset for training, namely `data/train_data.csv` and `data/train_labels.csv`. Use data from the first task you were given.
- Fill in the gaps in the provided code files marked with [ADD]
- Once you have filled the code, run:
  - ```make train```
  - ```make build```
- Test your solution by running commands:
  - ```make stop```
  - ```make run```
  - ```make test```
