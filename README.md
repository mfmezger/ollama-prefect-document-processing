# Document Processing Pipeline with Prefect and Ollama

## Used Tools

### Ollama

Ollama is probably the Best way to deploy and use LLMs on your own pc. They are quanitized versions that run very fast on Nvidia GPUs and Apple Silicon. On cpu not that fast but still possible.

### Prefect Cloud

Prefect is a workflow orchestration tool that allows for building easy pipelines. The cloud variant is choosen in this repo because it is easier to setup than the full stack.

## Installation

First install ollama from here.
https://ollama.ai/
If you are using windows please install it via WSL2.

Then install poetry with
`pip install poetry`

Install the project with `poetry install`.


## Usage

First log into prefect cloud with `prefect cloud login`.


## Data

The dataset used is the Samples of electronic Invoices Dataset from Mendeley Data. The dataset ist available here: https://data.mendeley.com/datasets/tnj49gpmtz/2 and licenced under CC BY 4.0.