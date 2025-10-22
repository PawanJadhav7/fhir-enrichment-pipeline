.PHONY: all ingest dq enrich features star test

all: ingest dq enrich features star

ingest:
	PYTHONPATH=. python -m src.ingest_fhir

dq:
	PYTHONPATH=. python -m src.validate_dq

enrich:
	PYTHONPATH=. python -m src.enrich_maps

features:
	PYTHONPATH=. python -m src.model_features

star:
	PYTHONPATH=. python -m src.load_warehouse

test:
	pytest -q
assets:
	@mkdir -p assets/diagrams
	@touch assets/diagrams/.gitkeep
	@git add assets/diagrams/.gitkeep
	@git commit -m "chore: add assets/diagrams with .gitkeep" || true
	@git push origin main || true
	@echo "✅ assets/diagrams ready and pushed (if there were new changes)."