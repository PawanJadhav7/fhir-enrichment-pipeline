.PHONY: all ingest dq enrich features star test

all: ingest dq enrich features star

ingest:
	python -m src.ingest_fhir

dq:
	python -m src.validate_dq

enrich:
	python -m src.enrich_maps

features:
	python -m src.model_features

star:
	python -m src.load_warehouse

test:
	pytest -q