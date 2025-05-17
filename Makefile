.PHONY: dev-up dev-down dev-logs backend-shell frontend-shell db-shell

dev-up:
	docker compose -f docker-compose.dev.yml up -d --build

dev-down:
	docker compose -f docker-compose.dev.yml down -v

dev-logs:
	docker compose -f docker-compose.dev.yml logs -f

backend-shell:
	docker compose -f docker-compose.dev.yml exec backend bash

frontend-shell:
	docker compose -f docker-compose.dev.yml exec frontend sh

db-shell:
	docker compose -f docker-compose.dev.yml exec postgres psql -U mluser -d mldb

init-db:
	docker compose -f docker-compose.dev.yml exec backend alembic upgrade head

test-pipeline:
	docker compose -f docker-compose.dev.yml run --rm pipeline-service python -m pipelines.full_pipeline