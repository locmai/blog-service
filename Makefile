install:
	@poetry install

start-dev:
	@poetry run uvicorn blog_service.main:app --reload

test:
	@poetry run pytest