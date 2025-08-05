.PHONY: build_env train clean lint build run test stop package

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Prepare environment
build_env:
	uv sync

train:
	uv run python train.py --train-data "data/train_data.csv" --train-labels "data/train_labels.csv"

clean:
	uv run pyclean --verbose .
	rm -rf dist
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -f model/*.onnx
	rm -f model/*.log

lint:
	uv run ruff format 
	uv run ruff check

build:
	docker build -t inference_api .

run:
	docker run -d -p 8000:8000 --name inference_container inference_api

test:
	uv run python tests/test_api.py

## Stop test server and remove container
stop:
	docker stop inference_container
	docker rm inference_container

## Package the problem for candidates
package:
	mkdir -p candidate_package
	mkdir -p candidate_package/inference
	mkdir -p candidate_package/tests
	cp train.py.template candidate_package/train.py
	cp pyproject.toml.template candidate_package/pyproject.toml
	cp inference/api.py.template candidate_package/inference/api.py
	cp Makefile candidate_package/Makefile
	cp Dockerfile candidate_package/Dockerfile
	cp README.md candidate_package/README.md
	cp -r tests/ candidate_package/
	zip -r candidate_package.zip candidate_package
	rm -rf candidate_package
